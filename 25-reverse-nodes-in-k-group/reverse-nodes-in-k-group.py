# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head):
            curr=head
            prev=None
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            # print(prev)
            return prev
        
        def getKthNode(temp,k):
            k-=1
            while temp is not None and k>0:
                k-=1
                temp=temp.next
            return temp

        temp=head
        prevLast=None

        while temp is not None:
            kThNode=getKthNode(temp,k)

            if kThNode is None:
                prevLast.next=temp
            
                break
        
            nextNode=kThNode.next

            kThNode.next=None
            reverseLinkedList(temp)

            if temp==head:
                head=kThNode
            else:
                prevLast.next=kThNode
            
            prevLast=temp

            temp=nextNode
        
        return head
    
