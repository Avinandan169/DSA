class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Avinandan169

        #by recursion
        '''if(n<=0):
            return False
        if(n==1):
            return True
        if(n%2==0):
            return self.isPowerOfTwo(n//2)
        return False'''

        #Bitwise
        if( n>0 and n&n-1==0):
            return True
        else:
            return False
        