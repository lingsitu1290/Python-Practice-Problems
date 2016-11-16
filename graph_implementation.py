# vertex (node) : can have a name ('key') and additional info ('payload')
# edge : connects two vertices
# directed: if the edges in a graph are all one-way
# weight: value associated to edges
# 1. Adjacency matrix: Using a 2-d matrix to implement a graph. Each row and column represent a vertex in a graph. 
    # Intersection between the row and column indicates that there is an edge from one vertex to the other.
    # Sparse matrix because most cells are empty unless the number of edges is large
# 2. Adjacancy list: Keep master list of all the vertices in the Graph object 
    # and then each vertex object in the graph maintains a list of the other vertices that it is connected to
    # In this implementation, using a dictionary. Dictionary keys are the vertices and values are the weights

# Implementation of a vertex
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

# Implementation of a graph as an adjacancy list 
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # Adds an instance of Vertex to the graph
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # Adds a new weight and directed edge to the graph
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # Returns a list of all vertices in the graph
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self,n):
        return n in self.vertList

# Testing

g = Graph()
for i in range(6):
    g.addVertex(i)

g.vertList
g.addEdge(0,1,2)

for vertex in g:
    print vertex
    print vertex.getConnections()
