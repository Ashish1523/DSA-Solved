# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque()
        q.append(root)
        count=1
        while q:
            stack=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    stack.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if count%2:
                if stack:
                    res.append(stack)
            else:
                if stack:
                    res.append(stack[::-1])
            count+=1
        return res
