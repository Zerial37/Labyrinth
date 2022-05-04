import random
from math import sqrt

"""
A class to build our labyrinth. First it creates a graph of given size, then adds the amount of crossings wanted and 
lastly creates a MST using Kruskal which represents our labyrinth.

KruskalMST, union and find copied from: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
Afterwards modified a little bit to fit our purpose.
"""


class Labyrinth:
    def __init__(self, vertices, weaves):
        self.V = vertices
        self.graph = []
        self.weaves = weaves
        self.tree = []
        self.loc_and_type = []
        self.columns = int(sqrt(self.V))

    def create_graph(self):
        """
        Here we create a graph of a wanted size, from which we later create our MST.
        Simple function which links tiles to the ones on the right and below, until every tile is linked to its
        neighbours.
        In the end we call add_crossing to create crossing before we run the graph through Kruskal.
        """
        for n in range(self.V - 1):
            y = n // self.columns
            x = n % self.columns
            if x + 1 < self.columns:
                self.addEdge(n, n + 1)
            if y + 1 < self.columns:
                self.addEdge(n, n + self.columns)

        self.add_crossing()

    def save_to_file(self):
        """
        Lets us save our MST, which represent our labyrinth, to a file called CS-A1121_lab-txt.
        """
        with open('CS-A1121_Lab.txt', 'w') as file:
            file.write(str(self.tree))

    def add_crossing(self):
        """
        Here we create crossings.
        First we decide the number of crossings wanted based on players wishes
        """
        if self.weaves == "None":
            rounds = 0
        elif self.weaves == "A few":
            rounds = self.columns
        elif self.weaves == "Many":
            rounds = random.randint(self.columns, self.V / 2)
        else:
            rounds = self.V

        """
        Then we build a list, that has all the possible tiles, which can serve as a middle of the crossing.
        In short we get every tile expect the tiles from the outer most rows and columns.
        """
        inner = []
        what_to_pop = []
        for x in range(self.columns - 2):
            for y in range(self.columns - 2):
                c = (x + 1) * self.columns
                inner.append(c + y + 1)

        """
        For-loop which takes a random tile from the list inner and makes a crossing below it. It is either from up to
        bottom or from left to right.
        For example, if we want a crossing below tile number 5 from left to right, we remove its links to tiles 4 and 6,
        and create a link between tiles 4 and 6.
        """
        for x in range(rounds):
            if len(inner) == 0:
                break
            one_or_two = random.randint(1, 2)
            sint = random.randint(0, len(inner) - 1)
            int = inner[sint]
            self.loc_and_type.append([int, one_or_two])
            own_index = (int * 2) - (int // self.columns)
            if one_or_two == 1:
                what_to_pop.append(own_index)
                what_to_pop.append(own_index - 2)
                self.addEdge(int - 1, int + 1)
            else:
                what_to_pop.append(own_index + 1)
                what_to_pop.append(((int - self.columns) * 2) - ((int - self.columns) // self.columns) + 1)
                self.addEdge(int - self.columns, int + self.columns)

            """
            The most time consuming part in our code currently, because it calls remove 5 times per loop.
            It is used to remove tiles from inner in order to keep the forming of illegal crossings and in order to know
            when our labyrinth can not fit crossing anymore.
            """
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
        """
        Here we remove all the links that have become unusable due to crossings.
        """
        what_to_pop.sort(reverse=True)
        for z in range(len(what_to_pop)):
            self.graph.pop(what_to_pop[z])

    def addEdge(self, u, v):
        """
        Part of the code copied.
        Added random.
        Used to add an edge to graph
        """
        self.graph.append([u, v, random.randint(1, 99)])

    def has_edge(self, v1, v2):
        """
        Tells us if two tiles are linked
        """
        if v1 < 0 or v2 < 0 or v1 > self.V - 1 or v2 > self.V - 1:
            return False

        if [v1, v2] in self.tree or [v2, v1] in self.tree:
            return True
        return False

    def find(self, parent, i):
        """
        Part of the code copied.
        Not modified.
        Comments from original: A utility function to find set of an element i (uses path compression technique)
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        Part of the code copied.
        Not modified.
        Original comments included
        """
        # A function that does union of two sets of x and y
        # (uses union by rank)
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

    def KruskalMST(self):
        """
        Part of the code copied.
        Modified to fit our purpose. Mainly in the way the MST is stored.
        Original comments included.
        Used to create a MST from graph using Kruskal's algorithm
        """

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

            # If including this edge doesn't
            #  cause cycle, include it in result
            #  and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                self.tree.append([u, v])
                self.union(parent, rank, x, y)
