import math

class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_strength = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                g = math.gcd(nums[i], nums[j])
                curr_strength = (nums[i] * nums[j]) // (g * g)
                
                if curr_strength > max_strength:
                    max_strength = curr_strength
                    
        return max_strength