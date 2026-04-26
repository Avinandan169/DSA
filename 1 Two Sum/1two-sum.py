class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        par_target=target
        output=[]
        for i in range(len(nums)):
            par_target=par_target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==par_target:
                    output.append(i)
                    output.append(j)
            par_target=target
        return output



        