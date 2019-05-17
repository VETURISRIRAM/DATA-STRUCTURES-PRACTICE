# Implementing Graphs

graph = { 'A' : ['B', 'C'],
		  'B' : ['C', 'D'],
		  'C' : ['D'],
		  'D' : ['C'],
		  'E' : ['F'],
		  'F' : ['C'],
}

def findPath(graph, start, end, path=[]):

	path = path + [start]

	if start == end:
		return path

	if start not in graph:
		print("No such start node found!")
		return None

	paths = []

	for node in graph[start]:

		if node not in path:
			newPath = findPath(graph, node, end, path)
		
		if newPath: return newPath
	return None

print(findPath(graph, 'A', 'D'))