class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        Ans=start^goal
        count=0
        while Ans:
            if Ans%2==1:
                count+=1
            Ans=Ans//2
        return count

        