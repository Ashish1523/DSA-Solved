from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def markParents(node, parent_track):
            q = deque([node])
            while q:
                current = q.popleft()
                if current.left:
                    parent_track[current.left] = current
                    q.append(current.left)
                if current.right:
                    parent_track[current.right] = current
                    q.append(current.right)

        parent_track = {}
        markParents(root, parent_track)

        visited = set()
        q = deque([target])
        visited.add(target)
        curr_level = 0

        while q:
            if curr_level == k:
                break
            level_size = len(q)
            for _ in range(level_size):
                current = q.popleft()
                for neighbor in (current.left, current.right, parent_track.get(current)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            curr_level += 1

        return [node.val for node in q]
