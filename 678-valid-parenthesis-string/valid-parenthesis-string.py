class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Avinandan169
        cmin=0
        cmax=0

        for ch in s:
            if ch=="(":
                cmin+=1
                cmax+=1
            elif ch==")":
                cmin-=1
                cmax-=1
            else:
                cmin-=1
                cmax+=1
            
            if cmax<0:
                return False
            
            if cmin<0:
                cmin=0
        return cmin==0
        