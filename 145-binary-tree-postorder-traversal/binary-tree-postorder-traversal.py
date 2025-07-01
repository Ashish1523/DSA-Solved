# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans=[]
        # def post(root):
        #     if root==None:
        #         return
        #     post(root.left)
        #     post(root.right)
        #     ans.append(root.val)
        # post(root)
        # return ans

        # if not root:
        #     return []
        
        # stack1=[root]
        # stack2=[]
        # result=[]

        # while stack1:
        #     node=stack1.pop()
        #     stack2.append(node)

        #     if node.left:
        #         stack1.append(node.left)
        #     if node.right:
        #         stack1.append(node.right)
            
        # while stack2:
        #     result.append(stack2.pop().val)
            
        # return result

        res=[]
        st=[]
        curr=root
        last=None

        while curr or st:
            if curr:
                st.append(curr)
                curr=curr.left
            else:
                peek=st[-1]
                if peek.right and last!=peek.right:
                    curr=peek.right
                else:
                    res.append(peek.val)
                    last=st.pop()
        return res