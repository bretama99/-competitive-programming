from collections import Counter
def minSetSize(A):
    left, res = len(A), 0
    print(Counter(A).most_common())
    for element, count in Counter(A).most_common():
        left -= count
        res += 1
        if left <= len(A) // 2:
            return res
A = [72,18,36,6,12,97,41,82,44,75,82,42,75,48,63,9,61,50,11,91,24,26,3,65,31,67,15,76,54,59,4,27,33,26,17,60,100,19,90,6,80,82,48,70,85,99,69,2,78,94,15,29,75,17,9,79,99,88,26,73,88,100,9,95,2,56,63,31,25,40,8,100,56,44,36,42,21,96,63,38,96,78,60,22,21,81]

print(minSetSize(A))