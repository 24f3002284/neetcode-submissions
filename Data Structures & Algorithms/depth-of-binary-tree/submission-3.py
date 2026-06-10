# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive dfs
        st=[]
        ans=0
        st.append([root,1])
        depth=1

        while st:
            node,depth=st.pop()   
            if not node:
                return ans         

            if node.left:
                st.append((node.left,depth+1))
            if node.right:
                st.append((node.right,depth+1))
                
            ans=max(ans,depth)

        return ans

            