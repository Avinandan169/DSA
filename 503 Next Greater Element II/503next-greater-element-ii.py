class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(2*n-1):
            idx=i%n

            while(stack and nums[idx]>nums[stack[-1]]):
                pop_idx=stack.pop()
                ans[pop_idx]=nums[idx]

            if i < n:
                stack.append(i)
        
        return ans
            



        