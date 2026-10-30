import heapq
class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        #Avinandan169

        if n==1:
            return 0

        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))

        min_cnt=[k+1]*n
        best={(0,1):0}
        pq=[(0,0,1)]

        while pq:
            d,u,cnt=heapq.heappop(pq)
            if u==n-1:
                return d
            if cnt>=min_cnt[u]:
                continue
            min_cnt[u]=cnt

            lu=labels[u]
            for v,w in adj[u]:
                nc=cnt+1 if labels[v]==lu else 1
                if nc<=k and nc<min_cnt[v]:
                    nd=d+w
                    state=(v,nc)
                    if nd<best.get(state,float('inf')):
                        best[state]=nd
                        heapq.heappush(pq,(nd,v,nc))

        return -1
        