class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        in_bound = lambda r,c: 0<=r<n and 0<=c<m
        visit = set()
        
        def dfs(r,c):
            if not in_bound(r,c) or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return 1+ dfs(r+1,c)+ dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1)
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j))
                print(ans,i,j)
        return ans
        
