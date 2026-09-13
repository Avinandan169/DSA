class Solution(object):
    #Avinandan169
    def backtrack(self,t_sum,last,nums,k,ans):
        if t_sum==0 and len(nums)==k:
            ans.append(list(nums))
            return
        if t_sum<=0 or k<len(nums):
            return
        
        for i in range(last,10):
            if i<=t_sum:
                nums.append(i)
                self.backtrack(t_sum-i,i+1,nums,k,ans)
                nums.pop()
            else:
                break
            


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        nums=[]
        self.backtrack(n,1,nums,k,ans)

        return ans
    
        