class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169

        prefix_sum=0
        min_pre=0

        for num in nums:
            prefix_sum+=num
            min_pre=min(min_pre,prefix_sum)
        
        return 1-min_pre
        