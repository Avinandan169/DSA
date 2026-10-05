class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        stack=[0]
        innerlevel=0
        for br in s:
            if br=="(":
                stack.append(0)
            else:
                innerlevel=stack.pop()
                resolved=max(2*innerlevel,1)
                stack[-1]+=resolved
        return stack[0]
        