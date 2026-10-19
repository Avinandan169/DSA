class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Avinandan169 
        
        nums.sort()
        n=len(nums)
        def lower_bound():
            low=0
            high=n
            while low<high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    high=mid
                else:
                    low=mid+1
            return low
        def upper_bound():
            low=0
            high=n
            while low<high:
                mid=(low+high)//2
                if nums[mid]>target:
                    high=mid
                else:
                    low=mid+1
            return low

        left=lower_bound()
        right=upper_bound()

        return range(left,right)
        


                
                


        