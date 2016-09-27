# Hacker Rank Day 14 Scrope

class Difference:
    def __init__(self, a):
        self.__elements = a

        # Add your code here
    def computeDifference(self):
        maximumDifference = max(self.__elements) - min(self.__elements)
        print maximumDifference


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference