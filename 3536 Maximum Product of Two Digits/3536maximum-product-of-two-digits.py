class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        number=n
        nums_list=[]
        while(number):
            nums_list.append(number%10)
            number=number//10
        nums_list.sort()
        product=nums_list[-1]*nums_list[-2]
        return product
        