class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        col = len(isConnected[0])
        is_bound = lambda x,y:0<=x<row and 0<=y<col
        number_of_provinces = 0
        visited = set()
        
        def dfs(i):
            visited.add(i)
            for j in range(row):
                if j not in visited and isConnected[i][j]:
                    dfs(j)

        for i in range(row):
            if i not in visited:
                dfs(i)
                number_of_provinces+=1
        return number_of_provinces
