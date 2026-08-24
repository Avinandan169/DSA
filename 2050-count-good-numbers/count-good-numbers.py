class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        Mod=10**9+7

        def power(base,exp):
            if exp==0:
                return 1
            
            half=power(base,exp//2)
            half_sq=(half*half)%Mod

            if exp%2==1:
                return (base*half_sq)%Mod
            else:
                return half_sq
        
        even_count=(n+1)//2
        odd_count=n//2

        even_way=power(5,even_count)
        odd_way=power(4,odd_count)

        return (even_way*odd_way)%Mod

            

        