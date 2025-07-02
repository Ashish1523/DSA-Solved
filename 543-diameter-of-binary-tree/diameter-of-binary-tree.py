# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxy=0
        def dia(node):
            nonlocal maxy
            if node==None:
                return 0
            l=dia(node.left)
            r=dia(node.right)
            maxy=max(maxy,l+r)
            return 1+max(l,r)
        dia(root)
        return maxy