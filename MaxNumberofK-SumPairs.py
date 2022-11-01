import collections
from collections import Counter

def maxOperations(nums,k):
    occ = collections.defaultdict(int)
    operations = 0
    for num in nums:
        if occ[k-num]>0:
            operations+=1
            occ[k-num]-=1
        else:
            occ[num]+=1
            print(occ[num])
    print(occ)
    return operations

nums = [1,2,3,4]
k=5
n=maxOperations(nums,k)
print(n)