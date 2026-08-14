class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        max_pr=nums[0]
        min_pr=nums[0]
        maximum=nums[0]

        for i in range(1,n):
            num=nums[i]

            if num<0:
                max_pr,min_pr=min_pr,max_pr
            
            max_pr=max(num,max_pr*num)
            min_pr=min(num,min_pr*num)

            maximum=max(max_pr,maximum)
        
        return maximum

        
        