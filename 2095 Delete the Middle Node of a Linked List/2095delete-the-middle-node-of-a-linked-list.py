# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
            
        fast=head.next
        slow=head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        temp=slow.next
        slow.next=slow.next.next
        temp=None

        return head
        