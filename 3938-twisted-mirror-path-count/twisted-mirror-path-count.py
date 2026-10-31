class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Avinandan169

        MOD=10**9+7
        m=len(grid)
        n=len(grid[0])
        down=[0]*n

        for r in range(m):
            right=0
            row=grid[r]
            for c in range(n):
                if r==0 and c==0:
                    right=1
                    down[0]=1
                    continue
                d=down[c]
                if row[c]==0:
                    ways=(right+d)%MOD
                    if r==m-1 and c==n-1:
                        return ways
                    right=ways
                    down[c]=ways
                else:
                    down[c]=right
                    right=d

        return 0
        