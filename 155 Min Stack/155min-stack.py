class MinStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((value,value))
        else:
            current_min=min(value,self.stack[-1][1])
            self.stack.append((value,current_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()