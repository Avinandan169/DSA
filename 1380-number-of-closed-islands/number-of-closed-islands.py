class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Avinandan169

        rows,cols=len(grid),len(grid[0])
        
        def is_closed(r,c):

            if r<0 or r>=rows or c<0 or c>=cols:
                return False

            if grid[r][c]==1:
                return True
                
            grid[r][c]=1  

            up=is_closed(r-1,c)
            down=is_closed(r+1,c)
            left=is_closed(r,c-1)
            right=is_closed(r,c+1)
            
            return up and down and left and right

        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    if is_closed(r,c):
                        ans+=1
        return ans
        