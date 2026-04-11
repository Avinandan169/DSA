# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        s=""
        temp=head
        while(temp!=None):
            s+=str(temp.val)
            temp=temp.next
        if s==s[::-1]:
            return True
        else:
            return False
        