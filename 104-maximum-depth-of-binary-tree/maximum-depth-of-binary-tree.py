# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def maxD(root):
        #     if root==None:
        #         return 0
        #     r1=maxD(root.right)
        #     r2=maxD(root.left)
        #     return max(r1,r2) +1
        # return maxD(root)
        if not root:
            return 0
        q=deque()
        q.append(root)
        depth=0
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth+=1
        return depth
