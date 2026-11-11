class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        
        last_seen=[-1,-1,-1]
        ans=0
        n=len(s)
        for i in range(n):
            last_seen[ord(s[i])-ord('a')]=i
            if -1 not in last_seen:
                ans+=(1+min(last_seen))

        return ans  

        