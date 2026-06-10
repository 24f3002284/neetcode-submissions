# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res=float('-inf')
        
        def dfs(node):
            if not node:
                return 0 # sum is 0 for a path which contains only None node

            left=dfs(node.left)
            right=dfs(node.right)
            leftMax=max(0,left)
            rightMax=max(0,right)
            # res+=node.val+leftMax+rightMax not this, but the line of code below
            self.res=max(self.res,node.val+leftMax+rightMax)

            return node.val+max(leftMax,rightMax)

        # return dfs(root) wrong
        dfs(root)
        return self.res

            