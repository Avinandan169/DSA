class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #Avinandan169
        
        matrix=[[0]*n for _ in range(n)]
        top=left=0
        right=bottom=n-1

        val=1

        while val<= n*n:
            for col in range(left,right+1):
                matrix[top][col]=val
                val+=1
            top+=1

            for row in range(top,bottom+1):
                matrix[row][right]=val
                val+=1
            right-=1
            for col in range(right,left-1,-1):
                matrix[bottom][col]=val
                val+=1
            bottom-=1
            for row in range(bottom,top-1,-1):
                matrix[row][left]=val
                val+=1
            left+=1
        return matrix