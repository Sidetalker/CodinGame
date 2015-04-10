import sys, math

class Node:
	def __init__(self, index):
		self.index = index
		self.links = []
		self.exit = False

	def addLink(self, index):
		self.links.append(index)

	def removeLink(self, index):
		self.links.remove(index)

	def pp(self):
		print("Node", self.index, file=sys.stderr)
		print("\tlinks:", self.links, file=sys.stderr)
		print("\texit:", self.exit, file=sys.stderr)

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in input().split()]

nodes = [Node(i) for i in range(N)]

for i in range(L):
	# N1: N1 and N2 defines a link between these nodes
	N1, N2 = [int(i) for i in input().split()]
	print("link:", N1, N2, file=sys.stderr)

	nodes[N1].addLink(N2)
	nodes[N2].addLink(N1)

for i in range(E):
	nodes[int(input())].exit = True

for node in nodes:
	node.pp()

def getExitDepth(node, depth):
	if node.exit or depth > 100:
		return depth
	else:
		for link in node.links:
			return getExitDepth(nodes[link], depth + 1)

# game loop
while 1:
	SI = int(input()) # The index of the node on which the Skynet agent is positioned this turn

	destNode = -1
	minDepth = sys.maxsize

	print("nodeCount:", len(nodes), file=sys.stderr)

	for link in nodes[SI].links:
		try:
		    exitDepth = getExitDepth(nodes[link], 0)
		except RuntimeError as e:
		    print(e, file=sys.stderr)

		print("Exit depth for link", link, "=", exitDepth, file=sys.stderr)

		if minDepth > exitDepth:
			destNode = link
			minDepth = exitDepth

	nodes[SI].removeLink(destNode)
	nodes[destNode].removeLink(SI)
	print(SI, destNode)