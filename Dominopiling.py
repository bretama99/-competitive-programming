def Domino(n,m):
    result = int((m*n)/2)
    return result

n=int(input("Enter N"))
m=int(input("Enter M"))
domino = Domino(n,m)
print(domino)