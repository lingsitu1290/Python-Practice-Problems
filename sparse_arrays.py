# Hacker Rank Sparce Array
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

words = []

for i in range(0,n):
    word = raw_input()
    words.append(word)
    
q = int(raw_input())

counts = [] 

for i in range(0,q):
    # Get query word
    query = raw_input()
    # Count the number of time query appears in words
    count = 0
    for word in words: 
        if query == word:
            count += 1

    counts.append(count)
# print count 

for count in counts:
    print count
    