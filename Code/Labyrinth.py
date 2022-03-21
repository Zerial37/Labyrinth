import random
from math import sqrt

class Labyrinth():

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

