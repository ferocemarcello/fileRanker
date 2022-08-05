import os
import sys
from collections import Counter

import nltk
from nltk import FreqDist, ngrams


def pre_process_input(input_words):
    #remove stopwords
    return [word.lower() for word in input_words]


def compute_score(input_file, input_words):
    all_counts = dict()
    freq_dist = FreqDist(input_file)
    return freq_dist


def analyze_files(input_files, input_words):
    input_words_proc = pre_process_input(input_words)
    return [compute_score(input_file, input_words_proc) for input_file in input_files]


def pre_process_text_file(text_content):
    return text_content.lower()


if __name__ == '__main__':
    # https://randomtextgenerator.com/
    #pipreqs --force
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('No directory given to index')
    indexable_directory = args[0]
    files = list()
    items = os.listdir(indexable_directory)
    for item in items:
        item_path = indexable_directory + os.sep + item
        if os.path.isfile(item_path):
            with open(item_path, 'r') as file:
                data = file.read().replace('\n', '')
                data_proc = pre_process_text_file(data)
                files.append(nltk.RegexpTokenizer(r"\w+").tokenize(data_proc))
    print("There are " + str(len(files)) + " in the directory " + indexable_directory)
    scores = analyze_files(files, ["He", "eats", "apple", "enough"])
    while True:
        line = input("search> ")
    # TODO: Search indexed files for words in line

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
