class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Avinandan169

        m=len(grid)
        n=len(grid[0])

        row_count=[sum(row) for row in grid]
        col_count=[sum(grid[r][c] for r in range(m)) for c in range(n)]

        ans=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1 and (row_count[r]>1 or col_count[c]>1):
                    ans+=1

        return ans
        