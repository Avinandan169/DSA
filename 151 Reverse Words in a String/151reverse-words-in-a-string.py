class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_str=""
        str_list=s.split()
        str_list.reverse()
        for substring in str_list:
            for i in range(len(substring)):
                reversed_str+=substring[i]
            reversed_str+=" "
        return reversed_str.strip()
        

        