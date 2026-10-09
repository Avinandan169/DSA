class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169

        insertion=0
        req_close=0

        for br in s:

            if br=="(":
                if req_close%2!=0:
                    insertion+=1
                    req_close-=1
                req_close+=2

            else:
                req_close-=1
                if req_close<0:
                    insertion+=1
                    req_close=1

        return insertion + req_close