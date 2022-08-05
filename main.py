# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #https://randomtextgenerator.com/
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('No directory given to index')
    indexable_directory = args[0]
    files = list()
    items = os.listdir(indexable_directory)
    for f in items:
        item = indexable_directory+os.sep+f
        if os.path.isfile(item):
            files.append(item)
    print("There are "+str(len(files))+ " in the directory "+indexable_directory)
    while True:
        line = input("search> ")
    # TODO: Search indexed files for words in line

# See PyCharm help at https://www.jetbrains.com/help/pycharm/