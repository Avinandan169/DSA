class Solution(object):
    def isPalindrome(self, s):
        new_s=""
        for i in s:
            if i.isalpha() or i.isdigit():
                new_s+=i.lower()
        if new_s==new_s[::-1]:
            return True
        else:
            return False
        