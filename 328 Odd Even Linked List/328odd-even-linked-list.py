# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        odd=head
        even_st=odd.next
        even=even_st

        while even and even.next:
            odd.next=even.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        
        odd.next=even_st

        return head
        