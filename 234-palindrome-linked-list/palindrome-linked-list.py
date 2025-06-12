# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # arr=[]
        # while head:
        #     v1=head.val
        #     arr.append(v1)
        #     head=head.next
        

        # lt=0
        # rt=len(arr)-1
        # while lt<rt:
        #     if arr[lt]!=arr[rt]:
        #         return False
        #     lt+=1
        #     rt-=1
        # return True
        def rev(node1):
            curr=node1
            prev=None
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        slow=head
        fast=head
        while(fast.next is not None and fast.next.next is not None):
            slow=slow.next
            fast=fast.next.next
        newH=slow.next
        rev1=rev(newH)
        temp1=rev1
        temp=head
        while temp1:
            if temp1.val!=temp.val:
                slow.next=newH
                return False
            temp1=temp1.next
            temp=temp.next
        slow.next=newH
        return True

        
        
