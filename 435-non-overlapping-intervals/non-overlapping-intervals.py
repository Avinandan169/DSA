class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Avinandan169
 
        intervals.sort(key=lambda x: x[1])
        removal=0
        prev_end=intervals[0][1]

        for i in range(1,len(intervals)):

            start,end=intervals[i]

            if start<prev_end:
                removal+=1
                prev_end=min(prev_end,end)
                
            else:
                prev_end=end
        
        return removal

        