class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bounding(nums,is_bound):
            low=0
            high=len(nums)-1
            bound=-1
            while(low<=high):
                mid=low+(high-low)//2
                if(nums[mid]==target):
                    bound=mid
                    if(is_bound):
                        high=mid-1
                    else:
                        low=mid+1
                elif(nums[mid]<target):
                    low=mid+1
                else:
                    high=mid-1
            return bound

        start=bounding(nums,is_bound=True)
        if start==-1:
            return [-1,-1]
        end=bounding(nums,is_bound=False)
        return [start,end]

        

        