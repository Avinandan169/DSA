class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        #Avinandan169

        stack=[]

        for ast in asteroids:
            while stack and ast<0 and stack[-1]>0:
                diff=ast+stack[-1]

                if diff<0:
                    stack.pop()
                elif diff>0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(ast)
        return stack




