class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        #Avinandan169

        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent=[-1]*n
        depth=[0]*n
        size=[1]*n
        heavy=[-1]*n

        order=[0]
        for u in order:
            p=parent[u]

            for v in adj[u]:

                if v!=p:
                    parent[v]=u
                    depth[v]=depth[u]+1
                    order.append(v)

        for i in range(n-1,-1,-1):
            u=order[i]
            max_sz=0

            for v in adj[u]:
                if v!=parent[u]:
                    size[u]+=size[v]
                    if size[v]>max_sz:
                        max_sz=size[v]
                        heavy[u]=v

        tin=[0]*n
        tout=[0]*n
        head=[0]*n
        timer=1
        stack=[(0,0,0)]

        while stack:
            u,h,state=stack.pop()
            if state==0:
                head[u]=h
                tin[u]=timer
                timer+=1
                stack.append((u,h,1))
                hv=heavy[u]
                for v in adj[u]:
                    if v!=parent[u] and v!=hv:
                        stack.append((v,v,0))
                if hv!=-1:
                    stack.append((hv,h,0))
            else:
                tout[u]=timer-1

        bit=[0]*(n+2)
        masks=[1<<(ord(c)-97) for c in s]

        for u in range(n):
            m=masks[u]
            bit[tin[u]]^=m
            bit[tout[u]+1]^=m

        for i in range(1,n+2):
            j=i+(i&-i)
            if j<=n+1:
                bit[j]^=bit[i]

        def get_root_xor(idx):
            res=0
            while idx>0:
                res^=bit[idx]
                idx-=idx&-idx
            return res

        def get_lca(u,v):
            while head[u]!=head[v]:
                if depth[head[u]]<depth[head[v]]:
                    u,v=v,u
                u=parent[head[u]]
            return u if depth[u]<depth[v] else v

        ans=[]
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                u=int(parts[1])
                new_mask=1<<(ord(parts[2])-97)
                diff=masks[u]^new_mask
                if diff:
                    masks[u]=new_mask
                    idx=tin[u]
                    while idx<=n+1:
                        bit[idx]^=diff
                        idx+=idx&-idx
                    idx=tout[u]+1
                    while idx<=n+1:
                        bit[idx]^=diff
                        idx+=idx&-idx
            else:
                u=int(parts[1])
                v=int(parts[2])
                w=get_lca(u,v)
                path_mask=get_root_xor(tin[u])^get_root_xor(tin[v])^masks[w]
                ans.append((path_mask&(path_mask-1))==0)

        return ans
        