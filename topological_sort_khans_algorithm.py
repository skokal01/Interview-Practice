# http://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
# Topological Sort implemented using Kahn's algorithm
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices # Number of vertices in the graph

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):
        in_degree = [0]*(self.V)

        # Traverse adjacency lists to fill indegrees
        # of vertices. This step takes O(V+E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create a queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result to (A Topological
        # ordering of the vertices)
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        if cnt != self.V:
            print "There exists a cycle in the graph"
        else:
            print top_order


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5,2)
    g.addEdge(5,0)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)

    g.topologicalSort()
