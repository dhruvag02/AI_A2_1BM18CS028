from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        # No of vertices
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform depth limited search from a given source
    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False


if __name__ == '__main__':
    n = int(input("Enter number of points in the graph "))
    g = Graph(n)
    for i in range(n-1):
        u = int(input("Enter Source vertex "))
        v = int(input("Enter adjacent vertex "))
        g.addEdge(u, v)

    target = int(input("Enter Target "))
    maxDepth = int(input("Enter Maximum Depth "))
    src = 0

    if g.IDDFS(src, target, maxDepth):
        print("Target is reachable from source " + "Within max depth")
    else:
        print("Target is not reachable from source " + "Within max depth")