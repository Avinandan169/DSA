class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        square=sorted(x*x for x in nums)
        ans=0
        n=len(square)

        for i in range(n):

            if i<(n+1)//2:
                ans+=square[n-1-i]
            else:
                ans-=square[n-1-i]
        
        return ans
        