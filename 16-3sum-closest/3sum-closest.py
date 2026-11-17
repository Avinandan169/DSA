class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Avinandan169

        nums.sort()
        n=len(nums)
        closest=nums[0]+nums[1]+nums[2]

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                cur=nums[i]+nums[l]+nums[r]
                if cur==target:
                    return target
                if abs(cur-target)<abs(closest-target):
                    closest=cur
                if cur<target:
                    l+=1
                else:
                    r-=1

        return closest
        