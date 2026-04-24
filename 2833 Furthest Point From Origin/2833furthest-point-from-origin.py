class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        countL=moves.count('L')
        countR=moves.count('R')
        
        return abs(countL-countR)+moves.count('_')

        