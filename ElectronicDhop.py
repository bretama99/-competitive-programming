# calculating H-Index
def H_index(citations):
    citations.sort()
    for i, cited in enumerate(citations):
        result = len(citations) - i
        if result <= cited:
            return result
    return 0
citation = [3,5,6,1,0]
print(H_index(citation))