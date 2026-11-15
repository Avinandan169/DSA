class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #Avinandan169

        vals=[
            (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
            (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
            (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")
        ]
        res=[]
        for val,sym in vals:
            if num==0:
                break
            count,num=divmod(num,val)
            res.append(sym*count)
        return "".join(res)