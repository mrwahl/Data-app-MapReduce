#!/usr/bin/env python

import sys
import re

# Define Function to read the pos/neg words from a file into a list
# Each line contains a positive/negative word
# Ignore comment or empty lines
def readWords(wordsFile):
    words = []
    with open(wordsFile) as f:
        for line in f:
            if line.startswith(';') or line.strip()=='':
                continue
            words.append(line.strip())
    return words
 
# Read positive and negative words
# If you run the MapReduce job in the cloud
# Store the files online and pass the complete path
posWords = readWords("hu-liu-positive-words.txt")
negWords = readWords("hu-liu-negative-words.txt")


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # remove all characters except letters and spaces
    line = re.sub(r'[^a-zA-Z ]', '', line)
    # convert to lowercase
    line = line.lower()
    # split line into words
    words = line.split()
    
    # iterate through all words
    for word in words:
        # output the word if positive or negative
        if (word in posWords):
            print('%s\t%s\t%s' % (word, 1, "pos"))
        elif (word in negWords):
            print('%s\t%s\t%s' % (word, 1, "neg"))
