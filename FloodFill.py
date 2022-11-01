class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        in_bound = lambda row, col : 0 <= row < len(image) and 0 <= col <len(image[0])
        startColor = image[sr][sc]
        visited = set()
        DIR = [[0,1],[1,0],[0, -1],[-1,0]]
        def dfs(row,col):
            
            image[row][col] = color
            visited.add((row,col))
            for direction in DIR:
                newRow, newCol = row+direction[0], col+direction[1]
                if not (newRow,newCol) in visited and in_bound(newRow,newCol) and image[newRow][newCol]==startColor:
                    dfs(newRow,newCol)
            
        
        dfs(sr,sc)
        return image
        
