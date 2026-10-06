class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan
        set_num=set(nums)
        longest=0
        count=0
        for i in set_num:
            if i-1 not in set_num:
                count=1
                num=i+1
                while(num in set_num):
                    count+=1
                    num+=1
                longest=max(longest,count)
        return longest