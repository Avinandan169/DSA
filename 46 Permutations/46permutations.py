class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]

        def backtrack(path):
            if(len(path)==len(nums)):
                result.append(list(path))
                return
            for num in nums:
                if num in path:
                    continue
            
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return result
        
        