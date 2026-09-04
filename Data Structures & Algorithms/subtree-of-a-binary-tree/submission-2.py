# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 

        if not root:
            return False
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def dfs(self, t, s):

        if not t and not s:
            return True
        
        if t and s and s.val == t.val:
            return (self.dfs(s.left, t.left) and self.dfs(s.right, t.right) )

        return False 