# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        newNode=TreeNode(preorder[0])
        midIdx=inorder.index(preorder[0])
        newNode.left=self.buildTree(preorder[1:1+midIdx],inorder[:midIdx])
        newNode.right=self.buildTree(preorder[1+midIdx:],inorder[1+midIdx:]) #in the last argument=> include 1+ to exclude root

        return newNode



