class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def time(mid):
            total_hr=0
            for i in range(len(piles)):
                total_hr+=math.ceil(float(piles[i])/mid)
            return total_hr

        low=1
        high=max(piles)
        ans=high
        while(low<=high):
            mid=(high+low)//2
            total_hr=time(mid)
            if(total_hr<=h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                
        
