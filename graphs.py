# breadth first search allows us to find the shortest 
# distance between two points

# a graph is a data structure based on connections
# graphs are made up of nodes and edges

# we need to search nodes in the order they are added
# in order to maintain breadth first search structure
# for this we use a queue

# queues only have two operations:
# enqueue and dequeue
# queues are FIFO

# ex 6.1: 2

# ex 6.2: cab --> cat --> bat

# we represent connections via a hash table

# a directed graph has connections pointing in one direction

# an undirected graph has bidirectional connections

## implementing breadth first search

# 1. keep a queue containing the nodes to check

# 2. pop a node off the queue

# 3. check if node is target and return if yes

# 4. if no, add all nodes connected by edges to the queue

# 5. repeat until target found or queue empty (no connection to target)

from collections import deque

search_queue = deque()

graph = {}
graph['rory'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue += graph['rory']

print(f"graph['rory'] : {graph['rory']}")

print(f"search_queue : {search_queue}")

print("\n-----\n")

def check_item(item):
	return item == "thing to check"

while search_queue: # while queue not empty
	item = search_queue.popleft() # get first item from queue
	if check_item(item): # check if its item we are looking for
		print(f"found item : {item}")
		return item
	else:
		search_queue += graph[item] # add edges from popped item

	print(f"item not found in graph")
	return False
