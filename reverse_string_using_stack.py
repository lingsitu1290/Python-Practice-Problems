class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def reverse(string):
    """
    Given string. Reverse using a stack. 
    >>> reverse("Hello")
    'olleH'

    >>> reverse("moose")
    'esoom'
    """


    output = ""
    word_stack = Stack()

    for char in string:
        word_stack.push(char)

    while not word_stack.isEmpty():
        output += word_stack.pop()

    return output


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
