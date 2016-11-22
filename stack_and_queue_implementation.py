# Implementation of abstract data types Stack and Queue
# Stack - LIFO 
# Queue - FIFO 

class Stack: 
    """
    >>> s = Stack()
    >>> print s.size()
    0

    >>> s = Stack()
    >>> s.push('hello')
    >>> s.push('true')
    >>> s.peek()
    'true'

    >>> s = Stack()
    >>> s.isEmpty()
    True

    >>> s = Stack()
    >>> s.push('hello')
    >>> s.push('true')
    >>> s.size()
    2

    >>> s = Stack()
    >>> s.push('hello')
    >>> s.push('true')
    >>> s.pop()
    'true'

    """
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

class Queue():
    """
    >>> q = Queue()
    >>> print q.size()
    0

    >>> q = Queue()
    >>> q.isEmpty()
    True

    >>> q = Queue()
    >>> q.enqueue('hello')
    >>> q.enqueue('true')
    >>> q.size()
    2

    >>> q = Queue()
    >>> q.enqueue('hello')
    >>> q.enqueue('true')
    >>> q.dequeue()
    'hello'

    """
    def __init__(self):
        self.items = []

    #return true if it is an empty list
    def isEmpty(self):
        return self.items == [] 

    # appending to the end of the list
    def enqueue(self, item):
        self.items.append(item)
        # another possiblity:
        # self.items.insert(0,item)

    # popping from the beginning of the list FIFO
    def dequeue(self):
        return self.items.pop(0)
        # another possibility if insert was used above 
        # return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"