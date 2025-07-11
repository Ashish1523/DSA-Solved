# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s=""
        if not root:
            return ""
        q=deque()
        q.append(root)
        while q:
            curr=q.popleft()
            if curr==None:
                s+="#,"
            else:
                s=s+str(curr.val)+','
            if curr is not None:
                q.append(curr.left)
                q.append(curr.right)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        s=data.split(",")
        s=s[:len(s)-1]
        q=deque()
        root=TreeNode(int(s[0]))
        q=deque()
        q.append(root)
        i=1
        while q:
            node=q.popleft()
            k=s[i]
            if k=="#":
                node.left=None
            else:
                leftN=TreeNode(int(k))
                node.left=leftN
                q.append(leftN)
            i+=1
            k=s[i]
            if k=="#":
                node.right=None
            else:
                rightN=TreeNode(int(k))
                node.right=rightN
                q.append(rightN)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))