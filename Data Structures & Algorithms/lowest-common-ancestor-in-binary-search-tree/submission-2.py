# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root # None

        cur=root
        while cur:
            if p.val>cur.val and q.val>cur.val: #move cur to the left if both values are less than cur. bcz, lowest common ancestor will be in the left subtree, since both p and q are either equal to or less than the left node of cur
                cur=cur.right
            elif p.val<cur.val and q.val<cur.val: # if both the values are greater than cur, move cur to the right
                cur=cur.left
            else: # if one of the values is equal to cur, cur is the ancestor
                return cur