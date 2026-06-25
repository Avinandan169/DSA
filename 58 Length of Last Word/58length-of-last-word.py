class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        n=len(l)-1
        return len(l[n])

        