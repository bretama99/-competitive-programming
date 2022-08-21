import math
def theatreSquare(n,m,a):
    flagstoneL1 = math.ceil(n/a)
    flagstoneIter = math.ceil(m/a)
    return  flagstoneL1 + flagstoneIter
n = int(input("Enter the 1st side"))
m = int(input("Enter the 2nd side"))
a = int(input("Enter the flagstones dimention"))

result = theatreSquare(n,m,a)
print(result)