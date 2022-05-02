"""
Copied from: https://www.geeksforgeeks.org/find-paths-given-source-destination/
Modified to fit our use case.
Original comments included, but modified to fit our use case.
"""

from collections import defaultdict
import time


class Solver:

    def __init__(self, vertices, tree, player, graphics):
        self.V = vertices
        self.tree = tree
        self.player = player
        self.graphics = graphics
        self.solver_moves = 0

        self.real_path = []
        self.graph = defaultdict(list)
        for i in self.tree:
            self.addEdge(i[0], i[1])

    '''
    A recursive function to get all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]
    '''

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then save
        # current path[]
        if u == d:
            self.real_path = path.copy()
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] is False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Gets all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to get all paths
        self.printAllPathsUtil(s, d, visited, path)

        """
        For-loop to move player along the solution path
        Modify number in time.sleep to make it faster
        """
        for i in self.real_path:
            self.player.update_location(i)
            self.graphics.player_update_position()
            self.solver_moves += 1
            time.sleep(0.2)
