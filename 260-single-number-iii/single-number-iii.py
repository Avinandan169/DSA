class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Avinandan169
        set_hash=set()
        for num in nums:
            if num in set_hash:
                set_hash.remove(num)
            else:
                set_hash.add(num)
        
        return list(set_hash)
        