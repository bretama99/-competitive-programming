from collections import Counter

def minSetSize(arr):
    left, res = len(arr), 0
    for element, count in Counter(arr).most_common():
        left -= count
        res += 1
        if left <= len(arr) // 2:
            return res
arr = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(arr))