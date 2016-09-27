# Hackerrank Day 11
#!/bin/python

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
#print arr
    
total = []

limit = 6

for i, row in enumerate(arr):
    for j, col in enumerate(row):
        if i + 2 < limit and j + 2 < limit:
            
            total.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        #print i, j, total
    

    
print max(total)