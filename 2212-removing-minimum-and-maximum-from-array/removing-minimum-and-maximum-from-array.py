class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 1
        
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        i,j=min(min_idx,max_idx),max(min_idx,max_idx)
        return min(j+1,n-i,(i+1)+(n-j))
        