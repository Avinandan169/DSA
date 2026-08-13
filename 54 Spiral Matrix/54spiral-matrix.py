class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        output=[]
        n=len(matrix)
        m=len(matrix[0])

        top=0
        bottom=n-1
        left=0
        right=m-1

        while top<=bottom and left<=right:
            for i in range(left,right+1):
                output.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                output.append(matrix[i][right])
            right-=1
            if not (left<=right and top<=bottom):
                break
            for i in range(right,left-1,-1):
                output.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                output.append(matrix[i][left])
            left+=1
        return output



        
        