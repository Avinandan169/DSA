class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan 
        #used previous smallest and greater and next smallest and greater
        
        n=len(nums)

        def getsumarray(is_max):
            total=0
            stack=[]
            for i in range(n+1):
                while stack and (i==n or (nums[stack[-1]]<nums[i] if is_max else nums[stack[-1]]>nums[i])):
                    mid=stack.pop()
                    left=stack[-1] if stack else -1
                    right=i
                    total+=nums[mid]*(mid-left)*(right-mid)
                stack.append(i)
            return total
        
        return getsumarray(True)-getsumarray(False)

        