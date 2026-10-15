class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        ans=0
        n=len(nums)
        for i in range(n):
            seen=set()
            for j in range(i,n):
                seen.add(nums[j])
                distinct_count=len(seen)
                ans+=distinct_count*distinct_count
        return ans