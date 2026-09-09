class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Avinandan169
        
        comma=0
        base=1000

        while n>=base:
            comma+=(n-base+1)
            base*=1000
        
        return comma

        