class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        in_bound = lambda x,y:0<=x<row and 0<=y<col
        
        def dfs(i,j):
            if not in_bound(i,j) or board[i][j]!='O':
                return 
            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and (i in [0, row-1] or j in [0,col-1]):
                    dfs(i,j)
            
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j] = 'X'
        for i in range(row):
            for j in range(col):
                if board[i][j]=='T':
                    board[i][j] = 'O'
        return board
                    
                    
