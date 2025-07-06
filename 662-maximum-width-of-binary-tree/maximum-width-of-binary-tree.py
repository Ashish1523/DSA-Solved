# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans=0
        q=deque()
        q.append([root,0])
        while q:
            l=len(q)
            min1=q[0][1]
            first=0
            last=0
            for i in range(l):
                node,idx=q.popleft()
                # print(node.val,idx)
                if i==0:
                    first=idx
                if i==l-1:
                    last=idx
                if node.left:
                    q.append([node.left,2*idx+1])
                if node.right:
                    q.append([node.right,2*idx+2])
            ans=max(ans,last-first+1)
        return ans

