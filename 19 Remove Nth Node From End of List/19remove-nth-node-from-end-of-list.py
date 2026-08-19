# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fast=head
        for i in range(n):
            fast=fast.next
        
        if not fast:
            return head.next
            
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        temp=slow.next
        slow.next=slow.next.next
        temp=None
        return head


