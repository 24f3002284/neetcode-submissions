# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #using bfs
        # if not root:
        #     return 0

        # level=1
        # q=deque([root])

        # while q:
        #     node=q[0]
        #     q.popleft()

        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        #     level+=1

        # return level

        if not root:
            return 0

        q=deque([root])
        level=0
        
        while q:
            for i in range(len(q)):
                node=q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level+=1

        return level