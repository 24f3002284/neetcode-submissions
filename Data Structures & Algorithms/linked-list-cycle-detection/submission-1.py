# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp1,tmp2=head,head

        while tmp1 and tmp1.next and tmp2:
            tmp1=tmp1.next.next
            tmp2=tmp2.next

            if tmp1==tmp2:
                return True

        # if tmp1==tmp2:
        #     return True
        return False