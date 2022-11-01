
# s = "Hello World!"
# start=end=max_len=0
# d = {}
# while end<len(s):
#     if s[end] in d and d[s[end]] >=start:
#         start = d[s[end]] + 1
#     max_len = max(max_len,end-start+1)
#     d[s[end]] = end
#     end+=1
#     print(end)
# print(max_len)
# s="SSPPSPS"
# a = [i for i, c in enumerate(s) if c == 'S']
# print(a)
# res = 1
# for i in range(1, len(a) - 1, 2):
#     res *= a[i + 1] - a[i]
# print(res % (10 ** 9 + 7) * (len(a) % 2 == 0 and len(a) >= 2))
# maxCount,start,zeroCount = 0,0,0
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# for end in range(len(nums)):
#     if nums[end] == 0:
#         zeroCount+=1
#     while zeroCount>k:
#         if nums[start]==0:
#             zeroCount-=1
#         start+=1
#     maxCount = max(end-start+1,maxCount)
# print(maxCount)

# for r,n in enumerate(nums):
#     k-=(1-n)
#     print(r,n,k)
#     if k<0:
#         k+=(1-nums[l])
#         l+=1
#     mx = max(r-l+1,mx)
# print(mx)
# differences = [1,-3,4]
# lower = 1
# upper = 6
# num = 0
# minimum = 0
# maximum = 0
# for difference in differences:
#     num += difference
#     minimum = min(minimum, num)
#     maximum = max(maximum, num)
# print(minimum, maximum)
# from collections import defaultdict, Counter
# max_l=0
# start=0
# fruits = [3,3,3,1,2,1,1,2,3,3,4]
# d = {}
# for i in range(len(fruits)):
#     d[fruits[i]] = i
# 
#     if len(d)>=3:
#         minV = min(d.values())
#         del d[fruits[minV]]
#         start = minV+1
# 
#     max_l = max(max_l,i-start+1)
#     print(max_l)

# employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
# id = 1
# impEmployee = {}
# subEmployee = {}
# for employee in employees:
#     impEmployee[employee[]]
# from collections import deque
#
#
# def bfs(graph, root):
#     visited, queue = set(), deque([root])
#     visited.add(root)
#     while queue:
#         vertex = queue.popleft()
#         for nighbour in graph[vertex]:
#             if nighbour not in visited:
#                 visited.add(nighbour)
#                 queue.append(nighbour)
#     print(visited)
#     print(queue)
#
# graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
# print("Following is Breadth First Traversal: ")
# bfs(graph, 0)
a="brhane"
b = "brhaoe"
arr = ["mmm","bbbb","vvvv"]
aa = "nnnn"
print(arr+[aa])
# arr = ['a','b','c']
# print(arr.index('o'))