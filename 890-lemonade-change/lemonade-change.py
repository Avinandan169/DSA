class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change={5:0,10:0}

        for bill in bills:
            if bill==5:
                change[5]+=1
            elif bill==10:
                change[10]+=1
                if change[5]>0:
                    change[5]-=1
                else:
                    return False
            else:
                if change[10]>0 and change[5]>0:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
            
        return True


        