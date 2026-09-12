from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Avinandan169
        count=Counter(s)

        sorted_chr=sorted(count.items(),key=lambda x:x[1],reverse=True)

        return "".join(ch*freq for ch,freq in sorted_chr)


        
        