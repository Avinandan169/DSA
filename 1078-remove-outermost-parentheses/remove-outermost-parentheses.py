class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Avinandan169
        res=[]
        stack=[]

        for br in s:
            if br==')':
                stack.pop()
            if stack:
                res.append(br)
            if br=='(':
                stack.append(br)
        return "".join(res)



        