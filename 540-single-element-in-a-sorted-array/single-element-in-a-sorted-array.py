class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:
                high=mid
        return nums[low]
        