# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pit : if we compare values of left and right nodes with root only.. not sufficient
        if not root:
            return True # empty tree=>valid BST

        #check if each node satisfies the condn that left boundary<node's val<right boundary
        def isValid(node,left,right):
            if not node:
                return True
            
            if node.val<=left or node.val>=right:
                return False
            #we checked the current node, now check the left and right nodes
            return ((isValid(node.left,left,node.val) and isValid(node.right,node.val,right)))

        return isValid(root,float('-inf'),float('inf'))