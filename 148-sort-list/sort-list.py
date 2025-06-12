# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #sorted using array
        # li=[]
        # curr=head
        # while curr:
        #     li.append(curr.val)
        #     curr=curr.next
        # li.sort()
        # new_h=head
        # for i in range(len(li)):
        #     new_h.val=li[i]
        #     new_h=new_h.next
        # return head

        #sorted using merge sort
        def mergeLL(list1,list2):
            dummyNode=ListNode(-1)
            temp=dummyNode

            while list1 is not None and list2 is not None:
                if list1.val<=list2.val:
                    temp.next=list1
                    list1=list1.next
                else:
                    temp.next=list2
                    list2=list2.next

                temp=temp.next
            
            if list1 is not None:
                temp.next=list1
            else:
                temp.next=list2
            
            return dummyNode.next
        
        def findMiddle(head):
            if head is None or head.next is None:
                return head
            
            slow=head
            fast=head.next

            while fast is not None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next

            return slow

        if head is None or head.next is None:
            return head

        middle=findMiddle(head)

        right=middle.next
        middle.next=None
        left=head

        left=self.sortList(left)
        right=self.sortList(right)

        return mergeLL(left,right)