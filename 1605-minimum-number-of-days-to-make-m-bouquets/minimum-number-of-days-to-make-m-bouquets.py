class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        #Avinandan169
        n=len(bloomDay)
        if m*k>n:
            return -1
        def possible(mid):
            count=0
            bouquet=0
            for b in bloomDay:
                if b<=mid:
                    count+=1
                    if count==k:
                        bouquet+=1
                        count=0
                else:
                    count=0

            return bouquet>=m
        
        low=min(bloomDay)
        high=max(bloomDay)

        while low<=high:
            mid=(low+high)//2
            if possible(mid):
                high=mid-1
            else:
                low=mid+1

        return low

        


                



                

