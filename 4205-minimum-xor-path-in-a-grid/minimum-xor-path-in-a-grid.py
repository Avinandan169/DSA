class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Avinandan169

        m,n=len(grid),len(grid[0])
        
        dp=[set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for c in range(1,n):
            val=grid[0][c]
            dp[c]={x ^ val for x in dp[c - 1]}
            
        for r in range(1,m):
            val0=grid[r][0]
            dp[0]={x ^ val0 for x in dp[0]}
            
            for c in range(1,n):
                val=grid[r][c]
                combined=dp[c] | dp[c - 1]
                dp[c]={x ^ val for x in combined}
                
        return min(dp[-1])
        