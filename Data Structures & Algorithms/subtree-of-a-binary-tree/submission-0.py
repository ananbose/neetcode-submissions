# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node,subnode):
            if node is None and subnode is None:
                return True
            if node is None or subnode is None:
                return False
            if node.val != subnode.val:
                return False
            return sameTree(node.right,subnode.right) and sameTree(node.left,subnode.left)
        if not root:
            return False
        if sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)