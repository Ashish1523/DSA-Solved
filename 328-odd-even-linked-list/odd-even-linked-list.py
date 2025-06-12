# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        otrack=head
        eHead=head.next
        etrack=eHead
        temp=head.next.next
        k=0
        while temp:
            if k%2==0:
                otrack.next=temp
                temp=temp.next
                otrack=otrack.next
            else:
                etrack.next=temp
                temp=temp.next
                etrack=etrack.next
            k+=1
            # print(temp)
        etrack.next=None
        otrack.next=eHead
        return head
