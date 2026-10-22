class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        n=len(nums)
        if n<=1:
            return 0
            
        is_forward=all(nums[(i+1)%n]==(nums[i]+1)%n for i in range(n))
        is_reversed=all(nums[(i+1)%n]==(nums[i]-1)%n for i in range(n))
        
        if not is_forward and not is_reversed:
            return -1
            
        p=nums.index(0)
        ans=float('inf')
        
        if is_forward:
            ans=min(ans,p,n-p+2)
        if is_reversed:
            ans=min(ans,((p+1)%n)+1, n-p)
            
        return ans
        