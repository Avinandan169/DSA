class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first=strs[0]
        for i in range(len(first)):
            char=first[i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or char!=strs[j][i]:
                    return first[:i]
        return first
            


        