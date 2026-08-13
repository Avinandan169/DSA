class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans=[]
        board=[["."]*n for _ in range(n)]

        def isSafe(row,col):
            for i in range(row):
                if(board[i][col]=='Q'):
                    return False
            i=row
            j=col
            while(i>=0 and j>=0):
                if(board[i][j]=='Q'):
                    return False
                else:
                    i-=1
                    j-=1
            
            i=row
            j=col
            while(i>=0 and j<n):
                if(board[i][j]=='Q'):
                    return False
                else:
                    i-=1
                    j+=1
            return True
        
        def nQueen(row):
            if row==n:
                format_board=["".join(r) for r in board]
                ans.append(format_board)
                return 
            for col in range(n):
                if isSafe(row,col):
                    board[row][col]='Q'
                    nQueen(row+1)
                    board[row][col]='.'

        nQueen(0)
        return ans




            
        