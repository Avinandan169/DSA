class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        Phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def backtrack(index,current_string):
            if index==len(digits):
                res.append(current_string)
                return

            possible_string=Phone[digits[index]]

            for letter in possible_string:
                backtrack(index+1,current_string+letter)
        backtrack(0,"") 
        return res   
        
        