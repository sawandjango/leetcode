'''
A------B
|\       \
| \       \
|  \    / E
|   \  /
D----C          
'''

#https://www.youtube.com/watch?v=ynZdirmZre4&t=97s
from curses import def_prog_mode


class depthFirstSearch():
    def dfs_process(self, visited, graph, root):        
        if root not in visited:
            print(root)
            visited.add(root)
            for neighbour in graph[root]:
                self.dfs_process(visited, graph, neighbour) 


dfs  = depthFirstSearch()
visited = set()
graph = {'A':['B','C','D'], 'B':['E'],'C':['D','E'], 'D':[],'E':[]}
dfs.dfs_process(visited, graph,'A')
