array = [6, 5, 12, 10, 9, 1]

def merge(L, R, array):
    i = j = k = 0
    while i < len(R) and j < len(L):
        if R[i] < L[j]:
            array[k] = R[i]
            i += 1
        elif L[j] < R[i]:
            array[k] = L[j]
            j += 1
        k += 1
    while i < len(R):
        array[k] = R[i]
        k += 1
        i += 1
    while j < len(L):
        array[k] = L[j]
        k += 1
        j += 1
    return array

def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        merged = merge(L,R,array)
        return merged
print(mergeSort(array))