from collections import defaultdict

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
c=defaultdict(list)
for path in paths:
    path = path.split(" ")
    folder = path[0]
    for s in path[1:]:
        s=s.split(".txt")
        name  = s[0]
        content = s[1]
        c[content].append((folder,name))

output = []
for k,v in c.items():
    print(v)
    if len(v)>1:
        temp = []
        for path,name in v:
            temp.append(path+'/'+name+'.txt')
        output.append(temp)
print(output)










print(c)











