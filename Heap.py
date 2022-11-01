import heapq


def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r=2*i+2
    if l<n and arr[largest]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[largest],arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def insert(arr,key):
    size = len(arr)
    if size ==0:
        arr.append(key)
    else:
        arr.append(key)
        for i in range((size//2),-1,-1):
            heapify(arr, size, i)
def delete(arr, key):
    i = 0
    for i in range(0,len(arr)):
        if key == arr[i]:
            break
    arr[i],arr[len(arr)-1] = arr[len(arr)-1], arr[i]
    arr.remove(key)
    for i in range(len(arr)//2, -1,-1):
        heapify(arr,len(arr),i)


arr = []
insert(arr,0)
insert(arr,30)
insert(arr,20)
insert(arr,10)
insert(arr,5)
delete(arr,10)
print(arr)

nums = [9,8,3,4,5,6,1,2]
heapq.heapify(nums)
print(nums)