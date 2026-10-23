class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Avinandan169

        n=len(intervals)

        starting=[start for start,end in intervals]
        ending=[end for start,end in intervals]

        max_divide=0
        divide=0

        starting.sort()
        ending.sort()

        start=0
        end=0

        while start<n:

            if starting[start]<=ending[end]:
                divide+=1
                start+=1
            else:
                divide-=1
                end+=1

            max_divide=max(max_divide,divide)
        
        return max_divide
