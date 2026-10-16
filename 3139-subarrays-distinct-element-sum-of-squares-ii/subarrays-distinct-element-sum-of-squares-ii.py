class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        MOD=10**9 + 7
        n=len(nums)
        sum1=[0] * (4*n)
        sum2=[0] * (4*n)
        lazy=[0] * (4*n)
        
        def apply(node,l,r,val):

            length=r-l+1
            sum2[node]=(sum2[node] + 2*val*sum1[node] + val*val*length)%MOD
            sum1[node]=(sum1[node]+val*length)%MOD
            lazy[node]+=val
            
        def push(node,l,r):

            if lazy[node]!=0:
                mid=(l + r)//2
                apply(node*2,l,mid,lazy[node])
                apply(node*2+1,mid+1,r,lazy[node])
                lazy[node]=0
                
        def update(node,l,r,ql,qr,val):

            if ql<=l and r<=qr:
                apply(node,l,r,val)
                return

            push(node,l,r)
            mid=(l + r)//2

            if ql<=mid:
                update(node*2,l,mid,ql,qr,val)

            if qr>mid:
                update(node*2+1,mid+1,r,ql,qr,val)

            sum1[node]=(sum1[node*2] + sum1[node*2 + 1])%MOD
            sum2[node]=(sum2[node*2] + sum2[node*2 + 1])%MOD

        last_seen={}
        total_ans=0

        for i, x in enumerate(nums):

            prev_idx=last_seen.get(x, -1)
            update(1,0,n - 1,prev_idx + 1,i,1)
            total_ans=(total_ans + sum2[1])%MOD
            last_seen[x]=i
            
        return total_ans