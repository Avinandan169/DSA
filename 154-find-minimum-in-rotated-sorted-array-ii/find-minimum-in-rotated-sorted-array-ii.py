class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        n=len(nums)
        low=0
        high=n-1

        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid
            else:
                high-=1
        
        return nums[low]