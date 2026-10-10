class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        #Avinandan169

        k=k1+k2
        diffs=[abs(a-b) for a,b in zip(nums1,nums2)]
        
        if sum(diffs)<=k:
            return 0
            
        max_diff=max(diffs)
        buckets=[0]*(max_diff+1)
        
        for d in diffs:
            buckets[d]+=1
            
        for current_diff in range(max_diff,0,-1):
            if buckets[current_diff]>0:
                take=min(k,buckets[current_diff])
                
                buckets[current_diff]-=take
                buckets[current_diff-1]+=take
                
                k-=take
          
                if k==0:
                    break
                    
        ans=sum(count*(d*d) for d,count in enumerate(buckets) if count>0)
        
        return ans
        