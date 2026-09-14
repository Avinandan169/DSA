class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        #Avinandan169
        x=rec1[0]<rec2[2] and rec2[0]<rec1[2]
        y=rec1[1]<rec2[3] and rec2[1]<rec1[3]

        return x and y
        
        