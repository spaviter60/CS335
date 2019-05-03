#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

  
import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###
def sort(item):
    return item[-1]

def build(filename):
    f = open(filename, 'rU')
    words = f.read().split()
    count = {}

    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()

    return count

def print_words(filename):
    dict = build(filename)

    for word in sorted(dict.keys()):
        print word, dict[word]

def print_top(filename):
    count = build(filename)
    i = 0

    items = sorted(count.items(), key=sort, reverse=True)
    for item in items[:20]:
        print item[0] + ': ' + str(item[1]) + ' times'
        i += 1

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
