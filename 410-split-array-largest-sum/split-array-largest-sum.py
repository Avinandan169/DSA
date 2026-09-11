class Solution(object):
    #Avinandan169
    def partitionFx(self,nums,max_sum):
        sub_sum=0
        partition=1
        for num in nums:
            if sub_sum+num<=max_sum:
                sub_sum+=num
            else:
                partition+=1
                sub_sum=num
        return partition
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2
            partition=self.partitionFx(nums,mid)
            if partition>k:
                low=mid+1
            else:
                high=mid-1

        return low

        