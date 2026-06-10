# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we need the kth smallest number in the BST. so, we have to perform the inorder traversal so that we get the numbers in ascending order.
        # not the level order traversal. only the inorder traversal of BST will provide us with ascending order and hence kth smallest element
        st=[]
        node=root
        cur=0

        while st or node:
            
            while node: # trying to reach the leftmost element
                st.append(node)
                node=node.left

            node=st.pop()
            cur+=1

            if cur==k:
                return node.val

            node=node.right