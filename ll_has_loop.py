"""
Given a linked list, check to see if the list contains a loop.
Returns True if there is a loop; returns False otherwise
"""

from linkedlist import LinkedList

# Using a list but using a dictionary will have a faster lookup time
def has_loop(ll):
    """
    >>> ll = LinkedList()
    >>> ll.add(1)
    >>> ll.add(2)
    >>> ll.add(3)
    >>> has_loop(ll)
    False
    """

    visited = []

    curr = ll.head

    while curr:
        if curr in visited:
            return True
        return False
        visited.append(curr)
        curr = curr.next

# Ideal way by traversing the linked list
def has_loop2(ll):
    """
    >>> ll = LinkedList()
    >>> ll.add(1)
    >>> ll.add(2)
    >>> ll.add(3)
    >>> has_loop2(ll)
    False

    >>> ll = LinkedList()
    >>> has_loop2(ll)
    False

    """


    if ll is None:
        return False

    # Traverse using two pointers
    slow = ll.head
    fast = ll.head

    # Slow will be incrementing by one while fast will be incrementing by two
    while slow != None or fast != None:
        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

        # If there is an overlap, there is a cycle
        if slow == fast:
            return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"