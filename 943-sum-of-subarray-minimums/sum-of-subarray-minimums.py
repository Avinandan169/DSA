class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        def findNSE(arr):
            nse=[n]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                nse[i]=n if not stack else stack[-1]
                stack.append(i)
            return nse
        
        def findPSEE(arr):
            pse=[-1]*n
            stack=[]
            for i in range(n):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                pse[i]=-1 if not stack else stack[-1]
                stack.append(i)
            return pse


        nse=findNSE(arr)
        pse=findPSEE(arr)
        total=0
        mod=10**9+7
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total=(total+left*right*arr[i])%mod
        return total


        