# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #https://randomtextgenerator.com/
    print_hi('PyCharm')
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('No directory given to index')
    indexable_directory = args[0]

    print("arg 1 = "+args[0])
    # TODO: Index all files in indexable_directory
    while True:
        line = input("search> ")
    # TODO: Search indexed files for words in line

# See PyCharm help at https://www.jetbrains.com/help/pycharm/