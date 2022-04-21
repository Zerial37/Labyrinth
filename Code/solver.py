# Copied from: https://www.geeksforgeeks.org/find-paths-given-source-destination/
# Modified to fit our use case

# Python program to print all paths from a source to destination.

from collections import defaultdict
import time


# This class represents a directed graph
# using adjacency list representation

class Solver:

    def __init__(self, vertices, tree, player, graphics):
        # No. of vertices
        self.V = vertices
        self.tree = tree
        self.player = player
        self.graphics = graphics

        self.real_path = []
        self.graph = defaultdict(list)
        for i in self.tree:
            self.addEdge(i[0], i[1])

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            self.real_path = path.copy()
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

        for i in self.real_path:
            self.player.update_location(i)
            self.graphics.player_update_position()
            time.sleep(1)
