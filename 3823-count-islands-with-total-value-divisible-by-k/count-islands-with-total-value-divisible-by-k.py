class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        #Avinandan169
        
        rows=len(grid)
        cols=len(grid[0])
        ans=0
        dirs=((-1, 0), (1, 0), (0, -1), (0, 1))
        
        for r in range(rows):

            for c in range(cols):

                if grid[r][c]>0:
                    curr_sum=grid[r][c]
                    grid[r][c]=0
                    stack=[(r, c)]
                    
                    while stack:
                        cr, cc=stack.pop()

                        for dr, dc in dirs:
                            nr, nc=cr+dr, cc+dc

                            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]>0:
                                curr_sum+=grid[nr][nc]
                                grid[nr][nc]=0
                                stack.append((nr,nc))
                                
                    if curr_sum%k==0:
                        ans+=1
                        
        return ans
        