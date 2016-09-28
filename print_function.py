# Hacker Rank Print Function

from __future__ import print_function

n = int(raw_input())

# map(func, seq)
# i.e.  map(lambda x,y:x+y, a,b)
# lambda argument_list: expression 
# i.e. f = lambda x, y : x + y
map(lambda x: print(x+1,end=''),range(n))