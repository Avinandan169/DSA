class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Avinandan169

        count={}
        res=0
        left=0
        max_freq=0
        n=len(s)

        for right in range(n):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])

            if (right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            
            res=max(res,right-left+1)

        return res

        