class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169
        n=len(nums)
        pref=[0]*n
        last_drop=[-1]*n
        
        curr_last=-1
        for i in range(n-1):

            if nums[i]>nums[i+1]:
                curr_last=i
                pref[i+1]=pref[i]+1

            else:
                pref[i+1]=pref[i]
            last_drop[i]=curr_last
            
        def is_sortable(k):
            prev_max=-1

            for L in range(0,n,k):
                
                R= L+k-1
                drops=pref[R]-pref[L]

                if drops==0:
                    cur_min,cur_max=nums[L],nums[R]

                elif drops==1 and nums[R]<=nums[L]:
                    j=last_drop[R-1]
                    cur_min,cur_max=nums[j+1],nums[j]

                else:
                    return False

                if prev_max>cur_min:
                    return False

                prev_max=cur_max
            return True

        ans=0
        d=1

        while d*d<=n:
            if n%d==0:

                if is_sortable(d):
                    ans+=d

                if d*d!=n and is_sortable(n//d):
                    ans+=n//d

            d+=1

        return ans
        