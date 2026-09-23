class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        #Avinandan169
        curr_sum=sum(cardPoints[:k])
        max_sum=curr_sum

        for i in range(1,k+1):
            curr_sum-=cardPoints[k-i]
            curr_sum+=cardPoints[-i]
            max_sum=max(curr_sum,max_sum)
        return max_sum
        