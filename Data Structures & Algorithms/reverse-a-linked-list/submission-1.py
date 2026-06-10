# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def LL(self,cur,prev):
        if not cur:
            return prev

        tmp=cur.next
        cur.next=prev
        return self.LL(tmp,cur)

        # return cur

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.LL(head,None)