class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        target=max(nums)
        ans=0
        for num in nums:
            ans+=(target-num)

        return ans
        