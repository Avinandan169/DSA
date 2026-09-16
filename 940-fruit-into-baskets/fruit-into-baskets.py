class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        #Avinandan169
        max_len=0
        last_fruit=sec_last=-1
        curr_count=0
        last_fruit_streak=0

        for fruit in fruits:

            if fruit==last_fruit or fruit==sec_last:
                curr_count+=1
            else:
                curr_count=last_fruit_streak+1
            
            if fruit==last_fruit:
                last_fruit_streak+=1
            else:
                last_fruit_streak=1
                sec_last=last_fruit
                last_fruit=fruit
            max_len=max(max_len,curr_count)
        return max_len

        