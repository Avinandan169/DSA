class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        #Avinandan169
        
        months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_no(date):
            month,day=map(int,date.split('-'))
            return sum(months[:month-1])+day
        
        start=max(day_no(arriveAlice),day_no(arriveBob))
        end=min(day_no(leaveAlice),day_no(leaveBob))

        return max(0,end-start+1)