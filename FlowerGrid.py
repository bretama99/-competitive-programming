n=4
l = 2*n
base =64
for i in range(l):
    for j in range(l):
        a = min(i,j,l-1-i,l-1-j)
        print(chr(64+n-a), end="")
    print()