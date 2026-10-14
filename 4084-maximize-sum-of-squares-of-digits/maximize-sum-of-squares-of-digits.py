class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        #Avinandan169 
        
        if sum>9*num:
            return ""
        
        ans=[]

        for _ in range(num):
            digit=min(9,sum)
            ans.append(str(digit))
            sum-=digit
        
        return ''.join(ans)




        