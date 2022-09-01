'''
A ------⇢ B-------⇢ D
|         ⇣
|         E          
|         |
⇣         ⇣
C-------⇢ F
'''
'''
graph = {
        'A' : ['B','C'],
        'B' : ['D','E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
}
# We need visited set/array and queue
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = ' ' )

        for neighbour in graph[s]: ## ['B','C'] :: B
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'A')
#Output : A B C D E F
'''
#### Another example 
# https://www.youtube.com/watch?v=tswq532WVF4
'''
Undirected graph
0 ---------1   4
| \       /   /
|   \    /   /  
|     \ /  / 
3      2 /   
'''
import collections
from operator import ne
import queue

class breathFirstSearch:
    def bfs_process(self, graph, root):
        visited = set() # once node is visited, add here 
        #A double-ended queue, or deque, has the feature of adding and removing elements from either end
        queue = collections.deque([root]) # better than queue if you are performing inque operations

        while queue: #
            vertex = queue.popleft()
            visited.add(vertex) # Just added the 0 : print(visited)=0
            # Now time to visit all neighbour nodes of 0 key
            for neighbour in graph[vertex]: # graph[vertex] = [1,2,3], neighbour = 1 first time
                if neighbour not in visited: # if neighbour not in vistied array/set
                    queue.append(neighbour)

        print(visited)    
            


graph = {
           0 : [1,2,3],
           1 : [0,2],
           2 : [0,1,4],
           3 : [0],
           4 : [2]
       
}
bfs = breathFirstSearch()
bfs.bfs_process(graph,0) # 0 is root

# Time compexity = O(E+V)