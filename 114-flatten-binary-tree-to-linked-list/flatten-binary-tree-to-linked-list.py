# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            q=[]
            q.append(root)
            while q:
                node=q.pop()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                if q:
                    node.right=q[-1]
                node.left=None
                