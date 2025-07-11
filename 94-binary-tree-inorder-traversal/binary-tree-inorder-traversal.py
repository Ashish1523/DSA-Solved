# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # t1=[]
        # def inord(root):
        #     if root==None:
        #         return
        #     inord(root.left)
        #     t1.append(root.val)
        #     inord(root.right)
        
        # inord(root)
        # return t1

        # stack=[]
        # res=[]
        # curr=root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr=curr.left
        #     curr=stack.pop()
        #     res.append(curr.val)
        #     curr=curr.right
        # return res

        #Morris Traversal
        inorder=[]
        if not root:
            return []
        curr=root
        while curr!=None:
            if curr.left==None:
                inorder.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while(prev.right and prev.right !=curr):
                    prev=prev.right
                if prev.right==None:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    inorder.append(curr.val)
                    curr=curr.right
        
        return inorder