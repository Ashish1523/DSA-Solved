# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def PostIn(inorder,inStart,inEnd,postorder,poStart,poEnd):
            if poStart>poEnd or inStart>inEnd:
                return None
            root=TreeNode(postorder[poEnd])
            inRoot=mapy[postorder[poEnd]]
            numsLeft =inRoot-inStart
            root.left=PostIn(inorder,inStart,inRoot-1,postorder,poStart,poStart+numsLeft-1)
            root.right=PostIn(inorder,inRoot+1,inEnd,postorder,poStart+numsLeft,poEnd-1)
            return root

        
        if len(inorder)!=len(postorder):
            return None
        
        mapy={}
        for i in range(len(inorder)):
            mapy[inorder[i]]=i
        
        return PostIn(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)

