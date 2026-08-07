class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        def backtrack(remain_target,path,start_idx):
            if(remain_target==0):
                result.append(list(path))
                return
            if remain_target<0:
                return
            
            for i in range(start_idx,len(candidates)):
                if i>start_idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remain_target:
                    break
                path.append(candidates[i])
                backtrack(remain_target-candidates[i],path,i+1)
                path.pop()
        backtrack(target,[],0)
        return result
                
        