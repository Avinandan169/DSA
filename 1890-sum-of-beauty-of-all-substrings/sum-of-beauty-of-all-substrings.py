class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        
        total=0
        n=len(s)

        for i in range(n):
            freq={}
            for j in range(i,n):
                freq[s[j]]=freq.get(s[j],0)+1
                values=freq.values()
                maxi=max(values)
                mini=min(values)

                total+=(maxi-mini)
        return total
        