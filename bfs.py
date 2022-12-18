from collections import defaultdict
#BFS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v) 
    def BFS(self,s):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
g = Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
g.BFS(2)

#DFS
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def DFSutil(self,v,visited):
        visited.add(v)
        print(v,end=" ")
        for i in self.graph[v]:
            if i not in visited:
                self.DFSutil(i,visited)
    def DFS(self,v):
        visited = set()
        self.DFSutil(v,visited)

g = Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
g.DFS(2)

#DIFD
path_list = []
def DLS(graph, src, target, max_depth):
    if src == target:
        return True
    if max_depth <= 0:
        return False
    for i in graph[src]:
        path_list.append(i)
        if (DLS(graph, i, target, max_depth - 1)):
            return True
    return False
def IDDFS(graph, src, target, max_depth):
    for i in range(max_depth):
        path_list.clear()
        if (DLS(graph, src, target, i)):
            return True
        return False
nodes = int(input('Enter the number of nodes: '))
graph = {}
for i in range(0, nodes):
    node_name = input(f'Enter {i + 1} node name: ')
    connected = int(input(f'Enter number of nodes connected to node {node_name}: '))
    connected_nodes = []
    if connected != 0:
        print('Enter the nodes: ')
    for j in range(0, connected):
        connected_nodes.append(input())
    graph[node_name] = connected_nodes
source_node = input('Enter the source node: ')
goal_node = input('Enter the goal node: ')
max_depth = int(input('Enter the max depth: '))
if IDDFS(graph, source_node, goal_node, max_depth) == True:
    print ("Target is reachable from source within max depth")
else :
    print ("Target is NOT reachable from source within max depth")
print('The path is: ', end = '')
for i in range(len(path_list)):
    print(path_list[i], end = '')
    if i != len(path_list) - 1:
        print('->', end = '')