class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findCombination(index,candidates,target,ans,ds):
            if index==len(candidates) :
                if target==0 :
                    ans.append(list(ds))
                return 
    
            if candidates[index]<=target :
                ds.append(candidates[index])
                findCombination(index,candidates,target-candidates[index],ans,ds)
                ds.pop()

            findCombination(index+1,candidates,target,ans,ds) 

        ans=[]
        ds=[]
        findCombination(0,candidates,target,ans,ds)
        return ans

        