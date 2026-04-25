class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        start=0; end=0

        for i in range(len(s)):
            l1=self.expand(s,i,i)
            l2=self.expand(s,i,i+1)

            max_len=max(l1,l2)
            if max_len>(end-start):
                start=i-(max_len-1)//2
                end=i + max_len//2
        return s[start:end+1]


        
    def expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1




        