class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        #Avinandan169
        n=len(nums)
        vals=sorted(list(set(nums)))
        V=len(vals)
        rank={v:i+1 for i,v in enumerate(vals)}

        bit_cnt=[0]*(V+1)
        bit_sum=[0]*(V+1)

        def update(idx,dc,ds):
            while idx<=V:
                bit_cnt[idx]+=dc
                bit_sum[idx]+=ds
                idx+=idx&-idx

        def query(idx):
            c,s=0,0
            while idx>0:
                c+=bit_cnt[idx]
                s+=bit_sum[idx]
                idx-=idx&-idx
            return c,s

        def find_median_idx(target):
            idx=0
            cur=0
            pw=1<<(V.bit_length())
            while pw>0:
                nxt=idx+pw
                if nxt<=V and cur+bit_cnt[nxt]<target:
                    cur+=bit_cnt[nxt]
                    idx=nxt
                pw>>=1
            return idx+1

        m=(x+1)//2
        cost=[0]*(n-x+1)

        for i in range(n):
            update(rank[nums[i]],1,nums[i])
            if i>=x:
                update(rank[nums[i-x]],-1,-nums[i-x])
            if i>=x-1:
                mid_r=find_median_idx(m)
                med=vals[mid_r-1]
                c_l,s_l=query(mid_r)
                c_tot,s_tot=query(V)
                cost[i-x+1]=(c_l*med-s_l)+((s_tot-s_l)-(c_tot-c_l)*med)

        INF=float('inf')
        dp=[[0]*(n+1)]+[[INF]*(n+1) for _ in range(k)]

        for i in range(x,n+1):
            c=cost[i-x]
            for j in range(k,0,-1):
                p=dp[j][i-1]
                t=dp[j-1][i-x]+c if dp[j-1][i-x]!=INF else INF
                dp[j][i]=t if t<p else p

        return dp[k][n]