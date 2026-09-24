# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root,result):
            if not root:
                return 
            if root.left:
                dfs(root.left,result)
            result.append(root.val)
            if root.right:
                dfs(root.right,result)

        
        result = []
        dfs(root, result)
        if k>len(result):
            return -1
        return result[k-1]
