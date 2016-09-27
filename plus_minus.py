# Hacker Rank Plus Minus

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

neg = []
pos = []
zero = []

for num in arr: 
    if num > 0:
        pos.append(num) 
    elif num < 0:
        neg.append(num) 
    else:
        zero.append(num)

print len(pos)/float(n)
print len(neg)/float(n)
print len(zero)/float(n)
        
