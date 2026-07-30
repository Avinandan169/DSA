class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans= set()
        for i in nums:
            if(i not in ans):
                ans.add(i)
            else:
                return True
        return False


        