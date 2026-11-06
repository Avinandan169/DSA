class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        #Avinandan169

        logs.sort(key=lambda item:item[1])
        sorted_queries=sorted([(q,i) for i,q in enumerate(queries)])

        ans=[0]*len(queries)
        freq=defaultdict(int)
        active=0
        l=0
        r=0
        m=len(logs)

        for q,idx in sorted_queries:
            while r<m and logs[r][1]<=q:
                sid=logs[r][0]
                if freq[sid]==0:
                    active+=1
                freq[sid]+=1
                r+=1

            while l<m and logs[l][1]<q-x:
                sid=logs[l][0]
                freq[sid]-=1
                if freq[sid]==0:
                    active-=1
                l+=1

            ans[idx]=n-active

        return ans
        