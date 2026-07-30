class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows==1):
            return [[1]]
        elif(numRows==2):
            return [[1],[1,1]]
        output=[[1],[1,1]]
        prev_ans=[1,1]
        for i in range(3,numRows+1):
            curr_ans=[0]*i
            for j in range(i):
                if(j==0 or j==i-1):
                    curr_ans[j]=1
                else:
                    curr_ans[j]=prev_ans[j-1]+prev_ans[j]
            output.append(curr_ans)
            prev_ans=curr_ans
        return output



        