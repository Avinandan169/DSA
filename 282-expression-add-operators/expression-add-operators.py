class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        #Avinandan169
        res=[]
        n=len(num)

        def backtrack(idx,eval_n,prev,expr):
            if idx==n:
                if eval_n==target:
                    res.append("".join(expr))
                return
            
            for j in range(idx+1,n+1):
                part=num[idx:j]

                if len(part)>1 and part[0]=='0':
                    break
                
                curr=int(part)

                if idx==0:
                    expr.append(part)
                    backtrack(j,curr,curr,expr)
                    expr.pop()
                else:
                    expr.append('+')
                    expr.append(part)
                    backtrack(j,eval_n+curr,curr,expr)
                    expr.pop()
                    expr.pop()

                    expr.append('-')
                    expr.append(part)
                    backtrack(j,eval_n-curr,-curr,expr)
                    expr.pop()
                    expr.pop()

                    expr.append('*')
                    expr.append(part)
                    backtrack(j,eval_n-prev+(prev*curr),prev*curr,expr)
                    expr.pop()
                    expr.pop()
                    
        backtrack(0,0,0,[])
        return res


                

        