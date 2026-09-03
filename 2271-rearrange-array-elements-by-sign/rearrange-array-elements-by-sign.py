class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Avinandan169
        output=[]
        pos_arr=[]
        neg_arr=[]
        idx=0
        n=len(nums)
        while idx<n:
            if nums[idx]>0:
                pos_arr.append(nums[idx])
            if nums[idx]<0:
                neg_arr.append(nums[idx])
            idx+=1

        for i in range(len(pos_arr)):
            output.append(pos_arr[i])
            output.append(neg_arr[i])
        
        return output