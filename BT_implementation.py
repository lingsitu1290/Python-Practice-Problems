# OOP implementation of Trees

class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        >>> r = BinaryTree('a')
        >>> r.insertLeft('c')
        >>> print r.getLeftChild().getRootVal()
        c
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """
        >>> r = BinaryTree('a')
        >>> r.insertRight('d')
        >>> print r.getRightChild().getRootVal()
        d
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """
        >>> r = BinaryTree('a')
        >>> r.insertRight('b')
        >>> print r.getRightChild().getRootVal()
        b
        """
        return self.rightChild

    def getLeftChild(self):
        """
        >>> r = BinaryTree('a')
        >>> r.insertLeft('b')
        >>> print r.getLeftChild().getRootVal()
        b
        """

        return self.leftChild 

    def setRootVal(self, obj):
        """
        >>> r = BinaryTree('a')
        >>> r.insertLeft('b')
        >>> r.setRootVal('c')
        >>> print r.getRootVal()
        c
        """
        self.key = obj 

    def getRootVal(self):
        """
        >>> r = BinaryTree('a')
        >>> r.getRootVal()
        'a'
        """

        return self.key


# Tree Implementation using a list of a list
def BinaryTreeL(r):
    """
    >>> r = BinaryTreeL(3)
    >>> print r
    [3, [], []]
    """
    # construct the root node with two empty lists and children
    return [r,[],[]]

def insertLeftL(root, newBranch):
    """
    >>> r = BinaryTreeL(3)
    >>> insertLeftL(r, 4)
    [3, [4, [], []], []]
    """
    # the first index will be the left branch
    t = root.pop(1)

    # if there is already a list there 
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRightL(root, newBranch):
    """
    >>> r = BinaryTreeL(3)
    >>> insertRightL(r, 4)
    [3, [], [4, [], []]]
    """
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

def getRootValL(root):
    """
    >>> r = BinaryTreeL(3)
    >>> r = insertRightL(r, 4)
    >>> getRootValL(r)
    3
    """
    return root[0]

def getLeftChildL(root):
    """
    >>> r = BinaryTreeL(3)
    >>> r = insertLeftL(r, 4)
    >>> getLeftChildL(r)
    [4, [], []]
    """
    return root[1]

def getRightChildL(root):
    """
    >>> r = BinaryTreeL(3)
    >>> r = insertLeftL(r, 4)
    >>> right = getRightChildL(r)
    >>> print right
    []
    """
    return root[2]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"

