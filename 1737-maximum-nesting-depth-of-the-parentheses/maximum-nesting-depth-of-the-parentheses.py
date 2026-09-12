class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        stack=[]
        max_count=0
        count=0
        for chr in s:
            if "("==chr:
                stack.append(chr)
                count+=1
            elif ")"==chr:
                stack.pop()
                count-=1
            max_count=max(max_count,count)

        return max_count




        