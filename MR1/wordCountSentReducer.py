#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_sent = None
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count, sentiment = line.split('\t')
    #print(word)
    #print(count)
    #print(sentiment)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word, current_count, current_sent))
        current_count = count
        current_word = word
        current_sent = sentiment

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s\t%s' % (current_word, current_count, current_sent))