# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque()
        q.append(root)

        while q:
            stack=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    stack.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if stack:
                res.append(stack)
        return res


