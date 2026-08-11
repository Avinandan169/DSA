class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]

        def backtrack(index,path):
            output.append(list(path))
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return output

        