class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169

        jumps=0
        l,r=0,0
        n=len(nums)
        while r < n-1:
            farthest=0

            for ind in range(l,r+1):
                farthest=max(ind+nums[ind],farthest)
            l=r+1
            r=farthest
            jumps+=1
        
        return jumps
