import os
import sys

import nltk
from nltk import FreqDist


def pre_process_input(input_words):
    # remove stopwords
    return [word.lower() for word in input_words]


def compute_score(freq_dist_entry, input_words):
    # Not optimized
    zeros = 0
    occurences = dict()
    len_input_words = len(input_words)
    freq_dist = freq_dist_entry[1]
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
        partial_score = (freq_dist.freq(item[0])/len(input_words)) - 0.01
        partial_score_sum += partial_score
    tot_score = (len_input_words - zeros) / len_input_words + partial_score_sum
    return freq_dist_entry[0], tot_score * 100


def analyze_files(input_files, input_words):
    sorted_list = [sorted_file for sorted_file in
                   sorted([compute_score(freq_dist_entry, input_words) for freq_dist_entry in input_files.items()],
                          key=lambda t: t[1], reverse=True)[:10] if sorted_file[1] > 0]
    return sorted_list


def pre_process_text_file(text_content):
    return text_content.replace('\n', '').lower()


def tokenize_no_puntctuation(data_proc):
    return FreqDist(nltk.RegexpTokenizer(r"\w+").tokenize(data_proc))


if __name__ == '__main__':
    # https://randomtextgenerator.com/
    # pipreqs --force
    print("Welcome")
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('No directory given to index')
    indexable_directory = args[0]
    items = os.listdir(indexable_directory)
    file_dict = dict()
    for item in items:
        item_path = indexable_directory + os.sep + item
        if os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                data = file.read()
                data_proc = pre_process_text_file(data)
                file_dict[str(item)] = tokenize_no_puntctuation(data_proc)
    print("There are " + str(len(file_dict)) + " files in the directory " + indexable_directory)
    while True:
        line = input("search> ")
        if 'quit' in line:
            break
        input_proc = pre_process_input(nltk.RegexpTokenizer(r"\w+").tokenize(line))
        results = analyze_files(file_dict, input_proc)
        if len(results) == 0:
            print("No matches found")
        for res in results:
            print(res)
    print("The program is over")
