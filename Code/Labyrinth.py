import random
from math import sqrt

class Labyrinth():
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
        self.tree = []
        self.columns = int(sqrt(self.V))

    def create_graph(self):
        for n in range(self.V - 1):
            y = n // self.columns
            x = n % self.columns
            if x + 1 < self.columns:
                self.addEdge(n, n + 1)
            if y + 1 < self.columns:
                self.addEdge(n, n + self.columns)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph.append([u, v, random.randint(1, 99)])

    def has_edge(self, v1, v2):
        if v1 < 0 or v2 < 0 or v1 > self.V - 1 or v2 > self.V - 1:
            return False
        for i in range(len(self.tree)):
            u, v, w = self.tree[i]
            if (u == v2 or u == v1) and (v == v1 or v == v2):
                return True
        return False

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):


        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                self.tree.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

    """
    def __init__(self, size):
        self.adjMatrix = []
        self.tree = []
        for i in range(size):
            self.tree.append([0 for i in range(size)])
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.columns = int(sqrt(len(self.adjMatrix)))

    def create_graph(self):
        for n in range(self.size - 1):
            y = n // self.columns
            x = n % self.columns
            if x + 1 < self.columns:
                self.add_edge(n, n + 1)
            if y + 1 < self.columns:
                self.add_edge(n, n + self.columns)

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        random_number = random.randint(1, 99)
        self.adjMatrix[v1][v2] = random_number
        self.adjMatrix[v2][v1] = random_number

    def has_edge(self, v1, v2):
        if v1 < 0 or v2 < 0 or v1 > self.size - 1 or v2 > self.size - 1:
            return False
        if self.tree[v1][v2] != 0:
            return True
        else:
            return False


    def prims(self):
        visited = [0] * self.columns * self.columns
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.columns * self.columns - 1:
            min = 999
            for i in range(self.columns * self.columns):
                if visited[i]:
                    for j in range(self.columns * self.columns):
                        if ((not visited[j]) and self.adjMatrix[i][j]):
                            if min > self.adjMatrix[i][j]:
                                min = self.adjMatrix[i][j]
                                s = i
                                d = j
            self.tree[s][d] = min
            self.tree[d][s] = min
            visited[d] = True
            edgeNum += 1
    """
