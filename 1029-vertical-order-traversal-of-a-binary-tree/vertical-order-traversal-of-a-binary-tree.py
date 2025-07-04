# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # q=deque([(root,0)])
        # min_col,max_col=0,0
        # cols=defaultdict(list)

        # while q:
        #     node,col=q.popleft()
        #     min_col,max_col=min(min_col,col),max(max_col,col)
        #     cols[col].append(node.val)

        #     if node.left:
        #         q.append((node.left,col-1))
        #     if node.right:
        #         q.append((node.right,col+1))
        # return [cols[c] for c in range(min_col,max_col+1)]

        nodes = []

        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val)) 
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        #print(nodes)
        answer = []
        prev_col = float('-inf')

        for col, row, val in nodes:
            if col != prev_col:
                answer.append([])
                prev_col = col
            answer[-1].append(val)

        return answer