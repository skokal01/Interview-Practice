def driver():
	g = Graph()

	for i in xrange(5):
		g.addVertex(i)

	g.addEdge(0,1)
	g.addEdge(0,4)
	g.addEdge(1,0)
	g.addEdge(1,2)
	g.addEdge(1,3)
	g.addEdge(1,4)
	g.addEdge(2,1)
	g.addEdge(2,3)
	g.addEdge(3,1)
	g.addEdge(3,2)
	g.addEdge(3,4)
	g.addEdge(4,0)
	g.addEdge(4,1)
	g.addEdge(4,3)

	for v in g:
		for w in v.getConnections():
			print("(%s, %s)" % (v.getId(), w.getId()))

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex

	def addEdge(self, fro, to, cost=0):
		if fro not in self.vertList:
			self.addVertex(fro)
		if to not in self.vertList:
			self.addVertex(to)
		self.vertList[fro].addNeighbor(self.vertList[to], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

def buildGraph(wordfile):
	d = {}
	g = Graph()
	wfile = open(wordfile, 'r')

	# create buckets of words that differ by one letter
	for line in wfile:
		# Remove the new line
		word = line[:-1]
		for i in xrange(len(word)):
			# Create buckets ex: _OPE, R_PE, RO_E, ROP_
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	return g

def backtrace(parent, start, end):
	path = [end]
	# path is a list, append parents and when the last element
	# of the path list is our source word stop and reverse the list
	while path[-1] != start:
		path.append(parent[path[-1]])

	path.reverse()
	return path

def BFS(v, targetWord):
	# Mark all the vertices as not visited
	visited = {}
	parent = {}
	source = v.getId()

	# create a queue for BFS
	queue = []

	# mark the source vertex as visited
	queue.append(v)
	visited[v.getId()] = True

	while queue:
		v = queue.pop(0)
		if v.getId() == targetWord:
			print backtrace(parent, source, targetWord)
			break

		for w in v.getConnections():
			if w.getId() not in visited:
				# store the parent of each node visited in parent dict
				parent[w.getId()] = v.getId()
				queue.append(w)
				visited[w.getId()] = True

if __name__ == "__main__":
	g = buildGraph("words.txt")
	BFS(g.vertList["FOOL"], "SAGE")
	BFS(g.vertList["FOOL"], "SOIL")
