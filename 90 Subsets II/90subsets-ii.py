class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        output=[]
        nums.sort()
        def backtracking(start_idx,path):

            result.append(list(path))
            for i in range(start_idx,len(nums)):
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()
        backtracking(0,[])
        result.sort()
        for i in range(len(result)):
            if(i==0 or result[i]!=result[i-1]):
                output.append(result[i])

        return output