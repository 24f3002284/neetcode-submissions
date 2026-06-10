# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 # no good node for an empty BT

        # we have to keep track of the max val. obtained so far in the path from the root to the current node
        #and add 1 to the ans which is to be returned only if the value of the current node is >= the max value obtained so far.
        def dfs(node,maxVal):
            if not node:
                return 0

            res=1 if node.val>=maxVal else 0
            maxVal=max(maxVal,node.val)

            return res+dfs(node.left,maxVal)+dfs(node.right,maxVal)

        return dfs(root,root.val)
            