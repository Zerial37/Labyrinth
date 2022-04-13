import random
from math import sqrt

class Labyrinth():
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
        self.tree = []
        self.loc_and_type = []
        self.columns = int(sqrt(self.V))

    def create_graph(self):
        for n in range(self.V - 1):
            y = n // self.columns
            x = n % self.columns
            if x + 1 < self.columns:
                self.addEdge(n, n + 1)
            if y + 1 < self.columns:
                self.addEdge(n, n + self.columns)

        self.add_crossing()


    def add_crossing(self):
        inner = []
        what_to_pop = []
        for x in range(self.columns - 2):
            for y in range(self.columns - 2):
                c = (x + 1) * self.columns
                inner.append(c + y + 1)

        for x in range(self.columns * 4):
            if len(inner) == 0:
                break
            one_or_two = random.randint(1, 2)
            sint = random.randint(0, len(inner) - 1)
            int = inner[sint]
            #print(int, one_or_two)
            self.loc_and_type.append([int, one_or_two])
            own_index = (int * 2) - (int // self.columns)
            if one_or_two == 1:
                what_to_pop.append(own_index)
                what_to_pop.append(own_index - 2)
                #print("What should be popped", self.graph[own_index], self.graph[own_index - 2])
                self.addEdge(int - 1, int + 1)
                #self.tree.append([int - 1, int + 1, random.randint(1, 99)])
            else:
                what_to_pop.append(own_index + 1)
                what_to_pop.append(((int - self.columns) * 2) - ((int - self.columns) // self.columns) + 1)
                #print("What should be popped", self.graph[own_index + 1], self.graph[((int - self.columns) * 2) - ((int - self.columns) // self.columns) + 1])
                self.addEdge(int - self.columns, int + self.columns)
                #self.tree.append([int - self.columns, int + self.columns, random.randint(1, 99)])

            for y in range(5):
                try:
                    if y == 0:
                        inner.remove(int)
                    elif y == 1:
                        inner.remove(int - 1)
                    elif y == 2:
                        inner.remove(int + 1)
                    elif y == 3:
                        inner.remove(int - self.columns)
                    else:
                        inner.remove(int + self.columns)
                except ValueError:
                    pass
            #self.V -= 3
        #print(self.V)

        what_to_pop.sort(reverse=True)
        for z in range(len(what_to_pop)):
            #print("What are we popping", self.graph[what_to_pop[z]])
            self.graph.pop(what_to_pop[z])



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
        #print(self.tree)
