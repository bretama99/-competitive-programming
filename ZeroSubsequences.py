# A Python program to print all
# combinations of given length
from itertools import combinations
count =0
def combi(arr, n):
    global count
    if n==0:
        return 0
    comb = combinations(arr,n)
    for i in comb:
        check = min(i)*max(i)
        if check==0:
            count+=1
    return combi(arr,n-1)
n = 5
arr=[0,2,0,1,-1]
aa = combi(arr,n)
print(count)