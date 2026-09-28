class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        ans=0
        
        for i in range(32):
            bit_sum=0
            for num in nums:
                bit_sum+=(num >> i)&1              
            if bit_sum%3:
                ans|=(1<<i)                
        if ans>=(1<<31):
            ans-=(1<<32)
            
        return ans