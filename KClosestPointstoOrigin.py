import heapq
k=1
points = [[1,3],[-2,2]]
minHeap = []
for x,y in points:
    dist = x**2 + y**2
    minHeap.append([dist,x,y])
heapq.heapify(minHeap)
print(minHeap)
result = []
while k>0:
    dist,x,y = heapq.heappop(minHeap)
    result.append([x,y])
    k-=1
print(result)