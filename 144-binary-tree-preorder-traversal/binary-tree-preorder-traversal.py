# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans=[]
        # def pre(root):
        #     if root==None:
        #         return
        #     ans.append(root.val)
        #     pre(root.left)
        #     pre(root.right)
        # pre(root)
        # return ans

        preorder=[]
        if root is None:
            return preorder
        stack=[]
        stack.append(root)
        while stack:
            root=stack.pop()
            preorder.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return preorder