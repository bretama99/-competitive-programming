
m=2
data = [10, 4, 8, 1]
i=0
j = m-1
temp = []
maximum = 0
while j<len(data):
    if sum(data[i:j+1])>maximum:
        maximum = max(maximum, sum(data[i:j+1]))
        temp = data[i:j+1]
    i+=1
    j+=1
print(sum(data)-sum(temp))


