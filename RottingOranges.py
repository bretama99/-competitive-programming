class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row, col = len(grid),len(grid[0])
        fresh, time  = 0,0
        in_bound = lambda x,y:0<=x<row and 0<=y<col
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])
                    
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for i,j in directions:
                    newRow, newCol = r+i,c+j
                    if not in_bound(newRow, newCol) or grid[newRow][newCol]!=1:
                        continue
                    grid[newRow][newCol] = 2
                    q.append([newRow,newCol])
                    fresh -= 1
            time +=1
        if fresh==0:
            return time
        return -1
