class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        #Avinandan169
        n=len(nums)
        def possible(mid):
            sum=0
            for num in nums:
                sum+=((num+mid-1)//mid)
            
            return sum<=threshold
        
        low=1
        high=max(nums)
        ans=high

        while low<=high:
            mid=(low+high)//2
            if possible(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
        