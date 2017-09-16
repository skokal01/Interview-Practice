# Problem URL
# http://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s,d,nR,nC):
        visited = [False]*(nR*nC)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                # Found the Destination
                if i == d:
                    return True
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

def isSafe(i,j,M):
    rows = len(M)
    cols = len(M[0])

    if ((i < 0 or i >= rows) or (j < 0 or j >= cols ) or M[i][j] == 0):
        return False
    return True

def findPath(M):
    rows = len(M)
    cols = len(M[0])
    s = 0
    d = 0
    k = 0

    g = Graph()

    for i in xrange(rows):
        for j in xrange(cols):
            if M[i][j] != 0:
                if isSafe(i,j+1,M):
                    g.addEdge(k, k+1)
                if isSafe(i,j-1,M):
                    g.addEdge(k, k-1)
                if isSafe(i+1,j,M):
                    g.addEdge(k, k+rows)
                if isSafe(i-1,j,M):
                    g.addEdge(k,k-rows)
            # Source index
            if M[i][j] == 1:
                s = k

            # Destination index
            if M[i][j] == 2:
                d = k
            k += 1

    print g.BFS(s,d,rows,cols)


if __name__ == "__main__":
    M =[[0,3,2],[3,3,0],[1,3,0]]
    findPath(M)
    M =[[0,3,1,0],[3,0,3,3],[2,3,0,3],[0,3,3,3]]
    findPath(M)
    M =[[0,0,1,0],[3,0,0,0],[2,3,0,3],[0,3,3,3]]
    findPath(M)
