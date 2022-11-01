# class Graph:
#     def __init__(self, num_nodes, edges):
#         self.num_nodes = num_nodes
#         self.data = [[] for x in range(num_nodes)]
#         for n1,n2 in edges:
#             self.data[n1].append(n2)
#             self.data[n2].append(n1)
#     def add(self,node):
#         return self.data.append(node)
#
#     def __repr__(self):
#         return "\n".join(["{}:{}".format(n, neighbours) for n,neighbours in enumerate(self.data)])
#     def __str__(self):
#         return self.__repr__()
# num_nodes = 5
# edges = [[0,1],[0,4],[1,2],[1,3],[1,4],[2,3],[3,4]]
# g = Graph(num_nodes,edges)
# a = g.add([3,5])
# print(a)
# for x in enumerate(g.data):
#     print(x)
from collections import Counter, defaultdict, OrderedDict
# d = {}
# nums = ["88 98 77", "66 88 90", "66 88 44"]
# for i in range(len(nums)):
#     arr = nums[i].split(' ')
#     for j in arr[:2]:
#         if int(j) not in d:
#             d[int(j)] = 1
#         else:
#             d[int(j)]+=1
# # for i, j in d.items():
# #     print(str(i)+" "+str(j))
# aa = sorted(d.items(), key=lambda kv:-kv[1])
# for i in aa:
#     print(str(i[0])+' '+str(i[1]))

# Online Python - IDE, Editor, Compiler, Interpreter
nums = [[1,2,3,4],[5,6,7,8],[9,10,11,22]]
print(nums[0])
level = 0


def dfs(node):
    global level
    if level==len(node):
        return
    level += 1
    dfs(node)



dfs(nums)
print(level)