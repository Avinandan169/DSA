class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        n=len(s)
        num=0
        while i<n and s[i]==' ':    
            i+=1
        
        if i==n:
            return 0

        sign=1
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1

        while i<n and s[i].isdigit():
            digit=int(s[i])

            num=num*10+digit
            i+=1
        
        num*=sign

        int_min=-(2**31)
        int_max=2**31-1

        if num<int_min:
            return int_min
        if num>int_max:
            return int_max
        
        return num