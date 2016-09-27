# Hacker Rank String to Integer Day 16

#!/bin/python

import sys


S = raw_input().strip()

try:
    i = int(S)
    print i
except ValueError:
    #Handle the exception
    print 'Bad String'