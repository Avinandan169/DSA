class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n:int)->int:
            product_n=1
            digit=0
            number=n
            while(number):
                digit=number%10
                product_n*=digit
                number=number//10
            return product_n
        while(True):
            product_n=product(n)
            if(product_n%t==0):
                break
            n+=1
        return n


        


        