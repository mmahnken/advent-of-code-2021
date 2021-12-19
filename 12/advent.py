from copy import copy
from collections import Counter

class Node:
	def __init__(self, name):
		self.name = name
		self.adjacent = []

	def add_connection(self, node):
		self.adjacent.append(node)

	def __repr__(self):
		return f"<Node {self.name}>"

class Graph:
	def __init__(self):
		self.nodes = []

	def find_path(self, a, b, path=None, visited=None):
		
		if not path:
			path = []
		if not visited:
			visited = set()

		if a == b:
			path.append(a)
			print('returning', ",".join([n.name for n in path]))
			return 1

		path.append(a)
		visited.add(a)
		total = 0
		for node in a.adjacent:
			# can only visit once
			if node.name.lower() == node.name:
				
				if node not in visited:                # PART 1 logic
				# if self.lowercase_cave_can_be_visited(node, visited):
					total += self.find_path(node, b, copy(path), copy(visited))
			
			# can visit multiple times
			if node.name.lower() != node.name:
				total += self.find_path(node, b, copy(path), copy(visited))
		
		return total

	def find_path_part2(self, a, b, path=None, visited=None):
		
		if not path:
			path = []
		if not visited:
			visited = {'double visit': False}

		path.append(a)

		path_pretty = ",".join([n.name for n in path])
		# if path_pretty == "start,b,A,c,A":
		# 	import pdb; pdb.set_trace()	

		if a == b:
			
			print(path_pretty)
			return 1

		
		visited[a.name] = visited.get(a.name, 0) + 1
		
		total = 0
		for node in a.adjacent:
			# can only visit once
			if node.name in ['start', 'end']:
				if node.name not in visited:
					total += self.find_path_part2(node, b, copy(path), copy(visited))


			elif node.name.lower() == node.name:
				if node.name in visited:
					if visited.get('double visit') == False:
						visited_c = copy(visited)
						visited_c['double visit'] = True
						total += self.find_path_part2(node, b, copy(path), visited_c)
					
				elif node.name not in visited:
					total += self.find_path_part2(node, b, copy(path), copy(visited))
			
			# can visit multiple times
			elif node.name.lower() != node.name:
				total += self.find_path_part2(node, b, copy(path), copy(visited))

		
		return total




def make_nodes(caves):
	lookup = {}
	g = Graph()
	for cave in caves:
		cave_node = Node(cave)
		lookup[cave] = cave_node
		g.nodes.append(cave_node)
	g.lookup = lookup
	return lookup, g

def make_connections(node_lookup, connections):
	for c in connections:
		cave1, cave2 = c

		cave1_node = node_lookup[cave1]
		cave2_node = node_lookup[cave2]

		cave2_node.add_connection(cave1_node)
		cave1_node.add_connection(cave2_node)

	return node_lookup



def process(filename):
	f = open(filename)
	caves = set()
	connections = []

	for line in f:
		cave1, cave2 = line.strip().split('-')
		caves.update([cave1, cave2])
		connections.append((cave1, cave2))

	return caves, connections


	

if __name__ == "__main__":
	caves, connections = process("input.txt")

	node_lookup, g = make_nodes(caves)
	node_lookup = make_connections(node_lookup, connections)
