class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        #Avinandan169
        m=len(mat[0])
        n=len(mat)
        def max_el(n,col):
            max_val=-1
            index=-1
            for i in range(n):
                if mat[i][col]>max_val:
                    max_val=mat[i][col]
                    index=i

            return index
        
        low=0
        high=m-1

        while(low<=high):
            mid=(high+low)//2
            row=max_el(n,mid)
            left=mat[row][mid-1] if mid-1>=0 else -1
            right=mat[row][mid+1] if mid+1<m else -1

            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        
        return [-1,-1]
            





        