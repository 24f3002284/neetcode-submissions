# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # to take care of the deletion of head case, it  is lways better to use a dummy node, next of which points to head
        dummy=ListNode(0,head)

        slow,fast=dummy,dummy
        while n>0 and fast:
            fast=fast.next
            n-=1

        while fast and fast.next:
            slow=slow.next
            fast=fast.next

        #now slow.next is the node to be deleted
        slow.next=slow.next.next

        return dummy.next

