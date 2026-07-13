class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[0]
        top=0
        closing=[')','}',']']
        if s=='':
            return False
        for i in s:
            if stack[top]=='(' and i==')' and stack[top]!=0:
                stack.pop()
                top-=1
            elif stack[top]=='{' and i=='}' and stack[top]!=0:
                stack.pop()
                top-=1
            elif stack[top]=='[' and i==']' and stack[top]!=0:
                stack.pop()
                top-=1
            else:
                if i in closing:
                    return False
                else:
                    top+=1
                    stack.append(i)
        if stack[-1]==0:
            return True
        else: 
            return False
        