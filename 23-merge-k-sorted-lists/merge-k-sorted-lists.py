# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        dummy=ListNode()
        for idx,head in enumerate(lists):
            if head:
                heapq.heappush(pq,(head.val,idx,head))
        fHead=dummy
        while pq:
            value,idx,node=heapq.heappop(pq)
            dummy.next=node
            dummy=dummy.next
            if node.next:
                heapq.heappush(pq,(node.next.val,idx,node.next))
        return fHead.next