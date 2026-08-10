class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        def backtracking(curr_str,open_count,close_count):

            if(len(curr_str)==2*n):
                result.append(curr_str)
                return
            
            if(open_count<n):
                backtracking(curr_str+"(",open_count+1,close_count)
            
            if(close_count<open_count):
                backtracking(curr_str+")",open_count,close_count+1)
        backtracking("",0,0)
        return result


        