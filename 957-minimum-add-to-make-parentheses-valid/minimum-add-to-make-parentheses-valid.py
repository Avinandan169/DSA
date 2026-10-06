class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Avinandan169
        '''stack=list(s)
        no_op_br=stack.count("(")
        no_cl_br=stack.count(")")
        output=no_op_br-no_cl_br
        return output if output>0 else -output'''
        #the above code fails in ")(" it gives 0 where as the answer would be 2
        open_req=0
        close_req=0
        for br in s:
            if br=="(":
                close_req+=1
            else:
                if close_req>0:
                    close_req-=1
                else:
                    open_req+=1
        return open_req+close_req

        