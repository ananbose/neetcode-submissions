# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if not root:
            return 0
        q.append(root)
        cnt = 0
        while q:
            lq = len(q)
            while lq>0:
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lq-=1
            cnt+=1
        return cnt