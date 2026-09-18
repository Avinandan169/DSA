class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        curr_ones=0
        max_ones=0
        for num in nums:
            if num==1:
                curr_ones+=1
                if curr_ones>max_ones:
                    max_ones=curr_ones
            if num==0:
                curr_ones=0
                
        return max_ones

        