class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Avinandan169

        n=len(nums)

        def get_digit_sum(num):
            s=0

            while num>0:
                s+=num%10
                num//=10
            return s
   
        arr=[(get_digit_sum(x),x,i) for i, x in enumerate(nums)]
        arr.sort()

        visited=[False]*n
        swaps=0
        
        for i in range(n):

            if visited[i] or arr[i][2]==i:
                continue

            cycle_size=0
            curr=i

            while not visited[curr]:
                visited[curr]=True
                curr=arr[curr][2]
                cycle_size+=1

            swaps+=(cycle_size-1)

        return swaps
        

        