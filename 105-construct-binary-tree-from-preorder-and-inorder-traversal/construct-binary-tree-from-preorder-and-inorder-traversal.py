# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def Construct(preorder,preStart,preEnd,indorder,inStart,inEnd,inMap):
            if preStart>preEnd or inStart>inEnd:
                return None
            root=TreeNode(preorder[preStart])
            inRoot=inMap[root.val]
            numsLeft=inRoot -inStart
            root.left=Construct(preorder,preStart+1,preStart+numsLeft,inorder,inStart,inRoot-1,inMap)
            root.right=Construct(preorder,preStart+numsLeft+1,preEnd,inorder,inRoot+1,inEnd,inMap)
            return root
        
        inMap={}
        for i in range(len(inorder)):
            inMap[inorder[i]]=i
        root=Construct(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inMap)
        return root
