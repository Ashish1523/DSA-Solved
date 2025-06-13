# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newH=ListNode(0)
        newH.next=head
        prev=newH
        curr=head
        while curr:
            if curr.next is not None and curr.val==curr.next.val:
                while curr.next is not None and curr.val==curr.next.val:
                    curr=curr.next
                
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        return newH.next
                
        return newH.next
