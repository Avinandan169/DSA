class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        answer=[]
        n=len(nums)
        for i in range(0,n-3):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target):
                break
            if(nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target):
                continue
            for j in range(i+1,n-2):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                if(nums[i]+nums[j]+nums[j+1]+nums[j+2]>target):
                    break
                if(nums[i]+nums[j]+nums[n-1]+nums[n-2]<target):
                    continue
                k=j+1
                l=n-1
                while(k<l):
                    curr_sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if(curr_sum==target):
                        answer.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while(k<l and nums[k]==nums[k-1]):
                            k+=1
                        while(k<l and nums[l]==nums[l+1]):
                            l-=1
                    elif(curr_sum<target):
                        k+=1
                    else:
                        l-=1
            
        return answer