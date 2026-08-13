class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        
        s=list(s)
        right=len(s)-1

        while(left<right):
            if(s[left].isalpha() and s[right].isalpha()):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            if not (s[left].isalpha()):
                left+=1
            if not (s[right].isalpha()):
                right-=1
        
        return "".join(s)


        