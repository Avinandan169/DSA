class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        #Avinandan169
        def possible(mid):
            day=1
            sack=0
            for w in weights:
                if sack+w<=mid:
                    sack+=w
                else:
                    day+=1
                    sack=w
            return day<=days
        
        low=max(weights)
        high=sum(weights)

        while low<=high:
            mid=(low+high)//2
            if possible(mid):
                high=mid-1
            else:
                low=mid+1
        
        return low

        
        
        
        