class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #Avinandan169

        while len(s)>k:
            nxt=[]
            for i in range(0,len(s),k):
                total=0
                for ch in s[i:i+k]:
                    total+=int(ch)
                nxt.append(str(total))
            s="".join(nxt)
        return s
        