class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        total_deg=0

        for ind,ch in enumerate(s,1):
            char_val=ord('z')-ord(ch)+1
            total_deg+=(ind*char_val)
        
        return total_deg
        