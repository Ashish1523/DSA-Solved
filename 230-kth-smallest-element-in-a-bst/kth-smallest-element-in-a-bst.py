# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q=[]
        def inorder(root):
            if root ==None:
                return
            inorder(root.left)
            # heapq.heappush(q,-root.val)
            # if len(q)>k:
            #     heapq.heappop(q)
            q.append(root.val)
            inorder(root.right)
        inorder(root)
        # return -q[0]
        return q[k-1]