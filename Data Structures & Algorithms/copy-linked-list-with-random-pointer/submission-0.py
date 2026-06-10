"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}
        cur=head

        while cur:
            copyNode=Node(cur.val)
            oldToCopy[cur]=copyNode
            cur=cur.next

        cur=head
        while cur:
            copyNode=oldToCopy[cur]
            copyNode.next=oldToCopy[cur.next]
            copyNode.random=oldToCopy[cur.random]
            cur=cur.next

        return oldToCopy[head]