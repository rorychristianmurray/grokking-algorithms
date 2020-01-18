from collections import deque

graph = {} # instantiate graph
graph['rory'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

bfs_queue = deque() # create queue

print(graph['rory'])

bfs_queue += graph['rory'] # add first node to graph

# pop first node off queue

# check if mango seller

# if yes, return that seller

# if not add their edges to graph and repeat

# if nothing found return not found

def bfs_mango():
    while bfs_queue.length > 0:
        # pop first node off queue
        seller = bfs_queue.popleft()
        if seller == "mango seller":
            return seller
        else:
            # if not add their edges to graph and repeat
    
    return "no mango seller"


