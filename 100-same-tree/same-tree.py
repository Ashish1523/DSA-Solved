# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node1,node2):
            if node1==None or node2==None:
                return node1==node2
            return node1.val==node2.val and preorder(node1.left,node2.left) and preorder(node1.right,node2.right)
        return preorder(p,q)
