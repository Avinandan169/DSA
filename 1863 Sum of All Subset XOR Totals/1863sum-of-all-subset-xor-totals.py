class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def back(index,curr_XOR):

            if index==len(nums):
                return curr_XOR
            
            exclude_sum=back(index+1,curr_XOR)
            include_sum=back(index+1,curr_XOR^nums[index])

            return exclude_sum+include_sum
        
        return back(0,0)

        