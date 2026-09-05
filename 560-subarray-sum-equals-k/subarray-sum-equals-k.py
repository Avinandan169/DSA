class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Avinandan169
        count=0
        curr_sum=0

        prefix={0 :1}

        for num in nums:
            curr_sum+=num

            if curr_sum-k in prefix:
                count+=prefix[curr_sum-k]
            prefix[curr_sum]=prefix.get(curr_sum,0)+1
        return count
        