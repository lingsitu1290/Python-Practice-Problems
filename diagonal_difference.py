# Hacker Rank Diagonal Difference 

# Grab matrix size
N = int(raw_input())
difference = 0

for i in xrange(N):
    row = raw_input().split()
    # difference will be the addition of the difference of the matrix 
    difference += (int(row[i]) - int(row[N-1-i]))

# Print absolute of the difference
print abs(difference)
