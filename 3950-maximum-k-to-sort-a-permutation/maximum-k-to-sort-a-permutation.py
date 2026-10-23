class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        ans=None
        for i,x in enumerate(nums):
            if x!=i:
                if ans is None:
                    ans=x
                else:
                    ans&=x

        return ans if ans is not None else 0
        