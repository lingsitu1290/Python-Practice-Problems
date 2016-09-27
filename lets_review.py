# HackerRank Day 6 

t=input()
for i in range(0,t):
    s_even = ""
    s_odd = ""
    string =raw_input()
    for i, char in enumerate(string):
        if i % 2 == 0: 
            s_even += char
        else:
            s_odd += char
    
    print s_even + " " + s_odd