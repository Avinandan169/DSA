class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX=2**31-1
        INT_MIN=-2**31
        if dividend==INT_MIN and divisor==-1:
            return INT_MAX

        if dividend==divisor:
            return 1
        sign=True
        if (dividend>=0 and divisor<0):
            sign=False
        if (divisor>0 and dividend<0):
            sign=False
        
        n=abs(dividend)
        d=abs(divisor)
        ans=0
        while n>=d:
            count=0
            while n>=(d<<(count+1)):
                count+=1
            ans+=(1<<count)
            n-=(d<<count)
        ans=ans if sign else -ans

        return max(INT_MIN,min(INT_MAX,ans))


        