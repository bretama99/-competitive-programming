def partition(data, low, high):
    piv = data[high]
    i = low-1
    for j in range(low,high):
        if data[j]<=piv:
            i+=1
            data[i], data[j] = data[j], data[i]
    data[i+1],data[high] = data[high],data[i+1]
    return i+1


def quickSort(data,low,high):
    if low < high:
        piv = partition(data,low,high)
        quickSort(data,low,piv-1)
        quickSort(data,piv+1,high)

data = [9,0,7,6,8,4,5]
size = len(data)-1
quickSort(data,0,size)
print(data)