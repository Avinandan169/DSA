class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start_idx=0
        end_idx=-1
        n=len(intervals)
        merged=[intervals[0]]
        i=1

        while(i<n):
            if(merged[-1][end_idx]>=intervals[i][start_idx]):
                merged[-1][end_idx]=max(merged[-1][end_idx],intervals[i][end_idx])
            else:
                merged.append(intervals[i])
            i+=1
            
        
        return merged
                
            
            
            
            



            
        


        