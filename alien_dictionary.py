'''
http://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
Given a sorted dictionary of an alien language, find order of characters
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
'''
from collections import defaultdict
class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)

    def addEdge(self,u,v):
        self.g[u].append(v)

    def buildGraph(self,vocab):
        for i in xrange(len(vocab)-1):
            w1,w2 = vocab[i],vocab[i+1]
            for j in xrange(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    self.addEdge(w1[j],w2[j])
                    break

    def topologicalSortutil(self,u,visited,stack):
        visited.add(u)

        for v in self.g[u]:
            if v not in visited:
                self.topologicalSortutil(v,visited,stack)

        stack.insert(0,u)

    def topologicalSort(self):
        visited = set()
        stack = []

        for u in self.g.keys():
            if u not in visited:
                self.topologicalSortutil(u,visited,stack)

        return stack

if __name__ == "__main__":
    g = Graph()
    g.buildGraph(vocab = ["baa", "abcd", "abca", "cab", "cad"])
    print g.topologicalSort()

    h = Graph()
    h.buildGraph(vocab=["caa", "aaa", "aab"])
    print h.topologicalSort()
