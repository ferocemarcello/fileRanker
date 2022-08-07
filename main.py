import os
import sys

import nltk
from nltk import FreqDist, PorterStemmer
from nltk.corpus import stopwords

portStemmer = PorterStemmer()
stop_words_set = set()


def pre_process_input(input_words, lower=True, stemming=False, remove_stopwords=False):
    return set(tokenize_no_puntctuation(input_words, lower=lower, stemming=stemming, remove_stopwords=remove_stopwords))


def compute_score(freq_dist, input_words):
    zeros = 0
    len_input_words = len(input_words)
    if all(elem in (freq_dist.keys())  for elem in input_words):
        return 100
    for input_word in input_words:
        if freq_dist.get(input_word) is None:
            zeros += 1
    partial_score_sum = 0
    for word in input_words:
        if freq_dist.get(word) is not None and freq_dist.get(word) > 1:
            partial_score_sum += freq_dist.freq(word) / len_input_words - 1 / freq_dist.N()  # avoiding the sum to be 1
    return round(((len_input_words - zeros) / len_input_words + partial_score_sum) * 100, 2)


def analyze_files(input_files, input_words):
    sorted_list = [(sorted_file[0], str(sorted_file[1]) + "%") for sorted_file in
                   sorted([(freq_dist_entry[0], compute_score(freq_dist_entry[1], input_words))
                           for freq_dist_entry in input_files.items()], key=lambda t: t[1], reverse=True)[:10]
                   if sorted_file[1] > 0]
    return sorted_list


def pre_process_text_file(text_content, lower=True, stemming=False, remove_stopwords=False):
    return FreqDist(tokenize_no_puntctuation(text_content.replace('\n', ''), lower=lower, stemming=stemming,
                                             remove_stopwords=remove_stopwords))


def tokenize_no_puntctuation(data_proc, lower=True, stemming=False, remove_stopwords=False):
    global stop_words_set
    if remove_stopwords:
        try:
            stop_words_set = set(stopwords.words('english'))
        except LookupError:
            print("No stopwords found. Downloading...")
            try:
                nltk.download('stopwords')
                stop_words_set = set(stopwords.words('english'))
            except Exception as e:
                print(e)
                print("Error while downloading stopwords")
                stop_words_set = set()
            print("Stopwords downloaded")
    if stemming:
        return [portStemmer.stem(w, to_lowercase=lower) for w in nltk.RegexpTokenizer(r"\w+").tokenize(data_proc)
                if w.lower() not in stop_words_set]
    if lower:
        return [w.lower() for w in nltk.RegexpTokenizer(r"\w+").tokenize(data_proc) if w.lower() not in stop_words_set]
    return [w for w in nltk.RegexpTokenizer(r"\w+").tokenize(data_proc) if w.lower() not in stop_words_set]


def fetch_files(indexable_directory, lower=True, stemming=False, remove_stopwords=False):
    items = os.listdir(indexable_directory)
    file_dict = dict()
    for item_name in items:
        item_path = indexable_directory + os.sep + item_name
        if os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                file_dict[str(item_name)] = pre_process_text_file(file.read(), lower=lower, stemming=stemming,
                                                                  remove_stopwords=remove_stopwords)
    print("There are " + str(len(file_dict)) + " files in the directory " + indexable_directory)
    return file_dict


def get_user_input_loop(file_dict, lower=True, stemming=False, remove_stopwords=False):
    while True:
        line = input("search> ")
        if 'quit' == line:
            print("The program is over")
            return 0
        try:
            input_proc = pre_process_input(line, lower=lower, stemming=stemming, remove_stopwords=remove_stopwords)
            print("User input processed to " + str(input_proc))
            results = analyze_files(file_dict, input_proc)
        except:
            print("An exception occured")
            return 1
        if len(results) == 0:
            print("No matches found")
        for res in results:
            print(res)


def main(args):
    # https://randomtextgenerator.com/
    # pipreqs --force
    print("Welcome")
    if len(args) == 0:
        print('No directory given to index')
        return 1
    stemming = False
    remove_stopwords = False
    if input("Do you want to stem the input files and the word input?(press Y/y for yes, or any other key for no)") \
            .lower() == "y":
        stemming = True
    if input("Do you want to remove stopwords from the input files and the word input?"
             "(press Y/y for yes, or any other key for no)").lower() == "y":
        remove_stopwords = True
    indexable_directory = args[0]
    file_dict = fetch_files(indexable_directory, lower=True, stemming=stemming, remove_stopwords=remove_stopwords)
    if len(file_dict) == 0:
        print("The program quits since there are no files to be analyzed")
        return 1
    return get_user_input_loop(file_dict, lower=True, stemming=stemming, remove_stopwords=remove_stopwords)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
