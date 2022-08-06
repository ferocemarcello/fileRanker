import os
import sys

import nltk
from nltk import FreqDist


def pre_process_input(input_words, stemming=False, stopwords=False):
    # remove stopwords and punctuation and lower
    return set([word.lower() for word in tokenize_no_puntctuation(input_words)])


def compute_score(freq_dist, input_words):
    # Not optimized
    zeros = 0
    occurences = dict()
    len_input_words = len(input_words)
    for input_word in input_words:
        occ = freq_dist.get(input_word)
        if occ is None:
            zeros += 1
            occurences[input_word] = 0
        else:
            occurences[input_word] = occ
    if zeros == len(occurences):
        return 0
    elif zeros == 0:
        return 100
    partial_score_sum = 0
    for item in occurences.items():
        partial_score = (freq_dist.freq(item[0]) / len(input_words)) - 0.01
        partial_score_sum += partial_score
    tot_score = (len_input_words - zeros) / len_input_words + partial_score_sum
    return (tot_score * 100).__round__(2)


def analyze_files(input_files, input_words):
    sorted_list = [(sorted_file[0], str(sorted_file[1]) + "%") for sorted_file in
                   sorted([(freq_dist_entry[0], compute_score(freq_dist_entry[1], input_words))
                           for freq_dist_entry in input_files.items()], key=lambda t: t[1], reverse=True)[:10]
                   if sorted_file[1] > 0]
    return sorted_list


def pre_process_text_file(text_content, stemming=False, stopwords=False):
    return FreqDist(tokenize_no_puntctuation(text_content.replace('\n', '').lower()))


def tokenize_no_puntctuation(data_proc):
    return nltk.RegexpTokenizer(r"\w+").tokenize(data_proc)


def fetch_files(indexable_directory, stemming=False, stopwords=False):
    items = os.listdir(indexable_directory)
    file_dict = dict()
    for item_name in items:
        item_path = indexable_directory + os.sep + item_name
        if os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                file_dict[str(item_name)] = pre_process_text_file(file.read(), stemming=stemming, stopwords=stopwords)
    print("There are " + str(len(file_dict)) + " files in the directory " + indexable_directory)
    return file_dict


def get_user_input_loop(file_dict, stemming=False, stopwords=False):
    while True:
        line = input("search> ")
        if 'quit' == line:
            print("The program is over")
            return 0
        try:
            input_proc = pre_process_input(line, stemming, stopwords)
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
    stopwords = False
    if input("Do you want to stem the input files and the word input?(press Y/y for yes, or any other key for no)") \
            .lower() == "y":
        stemming = True
    if input("Do you want to remove stopwords from the input files and the word input?"
             "(press Y/y for yes, or any other key for no)").lower() == "y":
        stopwords = True
    indexable_directory = args[0]
    file_dict = fetch_files(indexable_directory, stemming=stemming, stopwords=stopwords)
    if len(file_dict) == 0:
        print("The program quits since there are no files to be analyzed")
        return 1
    return get_user_input_loop(file_dict, stemming=stemming, stopwords=stopwords)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
