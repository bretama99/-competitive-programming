# class Graph:
#     def __init__(self, edges):
    #     self.V = vertices
    #     self.graph = []
    #
    # def add_edge(self, u, v, w):
    #     self.graph.append([u,v,w])
    # def display(self):
    #     for i in self.graph:
    #         print(i)
    # def find(self,parent, i):
    #     if parent[i] == i:
    #         return i
    #     return self.find(parent,parent[i])

# g = Graph(6)
# g.add_edge(0, 1, 4)
# g.display()
# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
dfs(graph, '0')