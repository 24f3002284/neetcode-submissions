# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque()
        ans=collections.defaultdict(list)
        q.append([root,1])

        while q:
            node,level=q.popleft()
            ans[level].append(node.val)

            if node.left:
                q.append([node.left,level+1])
            if node.right:
                q.append([node.right,level+1])

        return list(ans.values())


