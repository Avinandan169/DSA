class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Avinandan169
        output=[0]*len(nums)
        pos_idx=0
        neg_idx=1
        for num in nums:
            if num>0:
                output[pos_idx]=num
                pos_idx+=2
            else:
                output[neg_idx]=num
                neg_idx+=2
        return output