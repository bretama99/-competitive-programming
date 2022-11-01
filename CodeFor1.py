n=10
l = 3
r=10
arr = [n]
def calculate(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]!=1 and arr[i]!=0:
            count=1
            temp = [arr[i]//2,arr[i]%2,arr[i]//2]
            arr = arr[:i]+ temp + arr[i+1:]
    if count==0:
        return arr
    return calculate(arr)

a = calculate(arr)
print(a[l:r+1].count(1))
