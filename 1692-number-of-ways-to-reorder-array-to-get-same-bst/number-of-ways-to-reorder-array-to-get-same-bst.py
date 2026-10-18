class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinanfan169

        MOD=10**9+7
        n=len(nums)

        combination=[[0]*n for _ in range(n)]
        for i in range(n):
            combination[i][0]=1
            for j in range(1,i+1):
                combination[i][j]=(combination[i-1][j-1] + combination[i-1][j])%MOD

        def dfs(arr):
            if len(arr)<=2:
                return 1
                
            root=arr[0]
            left=[x for x in arr if x<root]
            right=[x for x in arr if x>root]

            l_len=len(left)
            r_len=len(right)
            
            ways_left=dfs(left)
            ways_right=dfs(right)

            res=(combination[l_len+r_len][l_len]*ways_left)%MOD
            res=(res*ways_right)%MOD
            
            return res
        return (dfs(nums)-1)%MOD