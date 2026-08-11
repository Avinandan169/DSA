class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)-1):
            par_diff=ord(s[i])-ord(s[i+1])
            if(par_diff>=0):
                sum+=par_diff
            else:
                par_diff=-par_diff
                sum+=par_diff
        return sum

            



        