# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True,0]
            
            # is_balanced=dfs(node.left)[0]==True and dfs(node.right)[0]==True and ((abs(dfs(node.left)[1]-dfs(node.right)[1]))<=1)
            # return [is_balanced,1+max(dfs(node.left)[1],dfs(node.right)[1])]
            # use the variables such as left, right and all so that we donot have to call the fn dfs multiple times
            
            left,right=dfs(node.left),dfs(node.right)            
            is_Balanced=(left[0] and right[0] and abs(left[1]-right[1])<=1)
            return [is_Balanced,1+max(left[1],right[1])]             

        return dfs(root)[0]