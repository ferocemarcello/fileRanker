# fileRanker

The xercise is to write a command line driven text search engine, usage being:

```
$ scala mainClassFile pathToDirectoryContainingTextFiles

$ java mainClassFile pathToDirectoryContainingTextFiles

$ python main.py pathToDirectoryContainingTextFiles
```

This should read all the text files in the given directory, build an in-memory representation of the files and their contents, and then give a command prompt at which interactive searches can be performed.

An example session might look like:

```
$ scala test.SimpleSearch /foo/bar

14 files read in directory /foo/bar

search>

search> to be or not to be

filename1 : 100%

filename2 : 95%

search>

search> cats

no matches found

search> :quit

$
```

I.e. the search should take the words given on the command prompt and return a list of the top 10 (max) matching filenames in rank order, giving the rank score against each match.

Note: treat the above as an outline spec; you don’t need to exactly reproduce the above output. Don’t spend too much time on input handling, just assume sane input.

Ranking

● The rank score must be 100% if a file contains all the words

● It must be 0% if it contains none of the words

● It should be between 0 and 100 if it contains only some of the words but the exact ranking

formula is up to you to choose and implement

Things to consider in your implementation

● What constitutes a word

● What constitutes two words being equal (and matching)

● Data structure design: the in memory representation to search against

● Ranking score design: start with something basic then iterate as time allows

● Testability

Deliverables

● Code to implement a version of the above

● A README containing instructions so that we know how to build and run your code



# Usage

● Go to the project folder with the command line

● Install requirements with pip install -r requirements.txt

● Run the program with python main.py {folder_absolute_path}

● End with "quit"


If the input contains duplicates, those are reduced to one entry



Tests are available https://github.com/mferoce/fileRanker/blob/main/file_tester.py and can be run using pyTest
