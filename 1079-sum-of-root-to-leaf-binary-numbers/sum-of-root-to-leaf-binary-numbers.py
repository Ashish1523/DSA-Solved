# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum1=0
        s=[]
        def preorder(node,s):
            nonlocal sum1
            if node==None:
                return
            s.append(str(node.val))
            if node.left==None and node.right==None:
                k="".join(s[:])
                sum1+=int(k,2)
            else:
                preorder(node.left,s)
                preorder(node.right,s)
            s.pop()
        preorder(root,s)
        return sum1