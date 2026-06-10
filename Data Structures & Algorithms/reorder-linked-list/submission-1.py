# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next

        while fast and fast.next: # must write fast also here
            slow=slow.next
            fast=fast.next.next

        secondHalf=slow.next
        prev=None
        slow.next=None
        # secondHalf.next=None

        while secondHalf:
            tmp=secondHalf.next
            secondHalf.next=prev
            prev=secondHalf
            secondHalf=tmp

        #now secondHalf=None, we have to make it point to the last node in the secondHalf.
        secondHalf=prev 

        p1,p2=head,secondHalf
        while p2:
            tmp1=p1.next
            p1.next=p2
            p1=tmp1 # typo not tmp
            tmp2=p2.next
            p2.next=tmp1
            p2=tmp2

        if p1:
            p1.next=None


        