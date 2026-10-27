class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid=[['#' for _ in range(n)] for _ in range(m)]
        valid_i=0
        valid_j=0
        while valid_j<n:
            grid[valid_i][valid_j]='.'
            valid_j+=1
        valid_j-=1
        while valid_i<m:
            grid[valid_i][valid_j]='.'
            valid_i+=1

        return ["".join(row) for row in grid]



