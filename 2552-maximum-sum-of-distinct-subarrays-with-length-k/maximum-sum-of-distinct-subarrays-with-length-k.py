class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Avinandan169
        """ans=0
        n=len(nums)
        for i in range(n-k+1):
            window=nums[i:i+k]
            if len(set(window))==k:
                ans=max(ans,sum(window))
        return ans"""

        freq={}
        win_sum=0
        ans=0
        left=0

        for right in range(len(nums)):
            x=nums[right]
            win_sum+=x
            freq[x]=freq.get(x,0)+1

            if right-left+1>k:
                out=nums[left]
                win_sum-=out
                freq[out]-=1
                if freq[out]==0:
                    del freq[out]
                left+=1
            if right-left+1==k and len(freq)==k:
                ans=max(ans,win_sum)
        return ans


        