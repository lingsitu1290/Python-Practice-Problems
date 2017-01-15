# Given Node class
class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def check_cycle_v2(node):
    """Given a singly linked list, write a function which takes in the first node
    in a singly linked list and returns a boolean indicating if the linked list
    contains a "cycle" (aka is a circular linked list).
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(3)
    >>> a.next = b
    >>> b.next = c
    >>> c.next = a
    >>> check_cycle_v2(a)
    True
    >>> x = Node(1)
    >>> y = Node(2)
    >>> z = Node(3)
    >>> x.next = y
    >>> y.next = z
    >>> check_cycle_v2(x)
    False
    """

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next != None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
