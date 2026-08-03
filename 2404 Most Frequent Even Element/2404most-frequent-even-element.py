class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=[0]*((max(nums))+1)
        for i in range(len(nums)):
            if(nums[i]%2==0):
                freq[nums[i]]+=1
        max_freq=max(freq)
        if(max_freq==0):
            return -1
        for j in range(0,len(freq),2):
            if(freq[j]==max_freq):
                return j
        return -1

            
            


        