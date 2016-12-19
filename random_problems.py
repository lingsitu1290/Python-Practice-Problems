#!/usr/bin/python
# -*- coding: utf-8 -*-

# Write a program that asks the user to enter 10 
# words, one at a time. The program should then 
# display all 10 words in alphabetical order. Write 
# this program using a loop so that you don't have to 
# write any additional lines of code if you were to 
# change the program to ask the user for 100 words. 
# That is, you'd only need to make one simple change, 
# and not have to write any new lines of code.

def return_sorted_nums(num):

    result = [] 

    for i in range(num):
        word = raw_input("Please give me a word:")
        result.append(word)

    for word in sorted(result):
        print word


# return_sorted_nums(10)


# Create a program that calculates the median of 
# this array of odd numbers: [1, 3, 4, 7, 12] which 
# should output “4”, the median. Be sure your 
# program can determine the median of any array 
# having an odd number of elements. To check, 
# replace the array above with [1, 2, 5, 9, 12, 13, 17] 
# where the median “9” should be returned.

import math

def return_median(lst):
    """
    >>> return_median([1,3,4,7,12])
    4
    >>> return_median([1,2,5,9,12,13,17])
    9
    """

    return lst[int(math.ceil(len(lst)/2))]


# Find the intersection of two sorted arrays. Can assume numbers are unique """

def intersection(list1, list2):
    """
    >>> intersection([1,2,3,4,5,6],[5,6,7,8,9])
    [5, 6]
    >>> intersection([7,8,9],[5,6,7,8,9])
    [7, 8, 9]
    """

    num_set = set()
    result = []

    for num in list1:
        num_set.add(num)

    for num in list2:
        if num in num_set:
            result.append(num)

    return result


if __name__ == "__main__":
    import doctest
    if not doctest.testmod().failed:
        print "\n*** ALL TESTS PASS; YOU MUST BE JUMPING WITH JOY\n"