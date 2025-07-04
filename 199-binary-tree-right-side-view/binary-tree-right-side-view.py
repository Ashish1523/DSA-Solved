# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q=deque()
        res=[]
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
        result=[]
        for i in res:
            result.append(i[-1])
        return result