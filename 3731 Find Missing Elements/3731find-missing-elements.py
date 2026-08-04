class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_n=min(nums)
        max_n=max(nums)
        nums=sorted(nums)
        output=[]
        for i in range(min_n+1,max_n):
            if(i not in nums):
                output.append(i)
        return output

            
        