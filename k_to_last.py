""" 
Cracking the Coding Interview LinkedList

Implement an algorithm to find the kth to last element of a singly linked list. 
"""

# Time: O(n)
# Space: O(1)

def k_to_last(node, k):
    """
    Finds and returns the kth to last element

    >>> from linkedlist import *

    >>> ll_example = LinkedList()
    >>> ll_example.data_to_list([1,2,3,4,5,6,7,8,9,10])
    >>> ll_example_result = k_to_last(ll_example.head, 3)
    >>> ll_example_result
    Node(8)

    >>> ll_example2 = LinkedList()
    >>> ll_example2.data_to_list([1,2,3,4])
    >>> ll_example_result2 = k_to_last(ll_example2.head, 6)
    >>> ll_example_result2
    """

    node_list = []
    curr = node

    while curr is not None:
        node_list.append(curr)
        curr = curr.next

    if k < len(node_list):
        return node_list[-k]


if __name__ == "__main__":
    import doctest
    doctest.testmod()