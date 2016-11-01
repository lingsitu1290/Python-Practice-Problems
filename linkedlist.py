# Implement linked list with methods add, delete, length, and reverse

class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    # Adding to the end of the list
    def add(self, data):
        """
        >>> ll = LinkedList()
        >>> ll.add(1)
        >>> ll.add(2)
        >>> print ll
        [1, 2]
        """

        new_node = Node(data)
        curr = self.head 

        if curr: 
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node

    # Adding in the front of the list 
    def insert(self, data):
        """
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> print ll
        [2, 1]
        """

        new = Node(data)
        new.next = self.head
        self.head = new

    def length(self):
        """
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.length()
        2
        """

        count = 0
        curr = self.head 

        while curr is not None:
            count += 1 
            curr = curr.next
        return count

    def delete(self, data):
        """
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.insert(3)
        >>> ll.delete(2)
        >>> print ll
        [3, 1]
        """

        curr = self.head
        prev = None
        found = False

        # while there is a node and data is in the list
        while curr and not found: 
            if curr.data == data:
                found = True
                # Case where the head node is the node to be deleted
                if prev == None: 
                    self.head = curr.next
                else: 
                    prev.next = curr.next
            # didn't find node yet continue to traverse list
            else: 
                prev = curr
                curr = curr.next

    def reverse(self):
        """
        >>> ll = LinkedList()
        >>> ll.add(1)
        >>> ll.add(2)
        >>> ll.add(3)
        >>> ll.reverse()
        >>> print ll
        [3, 2, 1]
        """
        curr = self.head 
        prev = None 

        while curr:
            # set next to the node after current
            next = curr.next
            # point current point to the previous node
            curr.next = prev
            # reset previous to current
            prev = curr
            # reset current to the next node
            curr = next
        # reset head to prev (first node)
        self.head = prev

    def data_to_list(self):
        data_list= []
        curr = self.head

        while curr:
            data_list.append(curr.data)
            curr = curr.next
        return data_list

    def __repr__(self):
        data_list = self.data_to_list()
        return str(data_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()