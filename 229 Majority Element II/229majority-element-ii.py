class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        maximum=max(nums)
        freq_dict={}
        for i in nums:
            freq_dict[i]=freq_dict.get(i,0)+1
        target=n/3
        ans=[]
        for key,val in freq_dict.items():
            if(target<val):
                ans.append(key)
        return ans

            

            
        


        
        