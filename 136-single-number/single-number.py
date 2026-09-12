class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        result=0
        for i in nums:
            result^=i
        
        return result
        