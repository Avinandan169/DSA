class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169 

        nums.sort()
        return sum(nums[~i]-nums[i] for i in range(len(nums)//2))