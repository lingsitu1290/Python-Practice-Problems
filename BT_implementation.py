# OOP implementation of Trees

class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild 

    def setRootVal(self, obj):
        self.key = obj 

    def getRootVal(self):
        return self.key


# Tree Implementation using a list of a list
def BinaryTree(r):
    # construct the root node with two empty lists and children
    return [r,[],[]]

def insertLeft(root, newBranch):
    # the first index will be the left branch
    t = root.pop(1)

    # if there is already a list there 
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

def getRootVal(root):
    return root[0]

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

