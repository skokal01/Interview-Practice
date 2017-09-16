from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V = V # Number of vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSortutil(self,v,visited,stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortutil(i,visited,stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited = [False]*self.V
        stack = []

        for i in xrange(self.V):
            if visited[i] == False:
                self.topologicalSortutil(i,visited,stack)

        print stack

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5,0)
    g.addEdge(5,2)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)

    g.topologicalSort()
