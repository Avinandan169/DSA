class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        #Avinandan169
        char=list(palindrome)
        n=len(palindrome)
        if n==1:
            return ""
        for i in range(n//2):
            if char[i]!='a':
                char[i]="a"
                return "".join(char)
        char[-1]="b"

        return "".join(char)



        