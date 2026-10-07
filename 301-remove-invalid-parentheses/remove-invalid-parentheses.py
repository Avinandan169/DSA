class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #Avinandan169

        l_rem=0
        r_rem=0

        for i in s:
            if i=="(":
                l_rem+=1
            elif i==")":
                if l_rem>0:
                    l_rem-=1
                else:
                    r_rem+=1
        
        res=[]

        def is_valid(string):
            count=0
            for i in string:
                if i =="(":
                    count+=1
                elif i==")":
                    count-=1
                if count<0:
                    return False
            return count==0
        
        def backtrack(s_curr,start,l_rem,r_rem):
            if l_rem==0 and r_rem==0:
                if is_valid(s_curr):
                    res.append(s_curr)
                return 
            
            for i in range(start ,len(s_curr)):
                if i!=start and s_curr[i]==s_curr[i-1]:
                    continue

                if s_curr[i]=='(' and l_rem>0:
                    backtrack(s_curr[:i]+s_curr[i+1:],i,l_rem-1,r_rem)
                elif s_curr[i]==')' and r_rem>0:
                    backtrack(s_curr[:i]+s_curr[i+1:],i,l_rem,r_rem-1)
        
        backtrack(s,0,l_rem,r_rem)
        return res




        