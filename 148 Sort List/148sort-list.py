# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def FindMid(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def merge(left,right):
            dummy=ListNode(-1)
            curr=dummy
            while left and right:
                if left.val<=right.val:
                    curr.next=left
                    left=left.next
                else:
                    curr.next=right
                    right=right.next
                curr=curr.next
            curr.next=left if left else right
            return dummy.next

        def mergeSort(head):
            if not head or not head.next:
                return head
            middle=FindMid(head)
            lefthead=head
            righthead=middle.next
            middle.next=None
            lefthead=mergeSort(lefthead)
            righthead=mergeSort(righthead)
            return merge(lefthead,righthead)

        head=mergeSort(head)
        return head

        

        