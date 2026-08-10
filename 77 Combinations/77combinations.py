class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        def back(start_val,path):
            if len(path)==k:
                result.append(list(path))
                return
            
            for i in range(start_val,n+1):
                path.append(i)
                back(i+1,path)
                path.pop()
        back(1,[])
        return result



        