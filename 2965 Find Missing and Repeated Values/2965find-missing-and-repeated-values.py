class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        check_set=set()
        n=len(grid)
        repeating=0;missing=0;actual_sum=0
        expected_sum=((n**2) * ((n**2)+1)) / 2
        for i in range(n):
            for j in range(n):
                actual_sum+=grid[i][j]
                if(grid[i][j] in check_set):
                    repeating=grid[i][j]
                else:
                    check_set.add(grid[i][j])
        missing = expected_sum + repeating - actual_sum
        return [repeating,missing]

        