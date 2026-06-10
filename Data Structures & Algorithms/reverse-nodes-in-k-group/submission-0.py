# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prevGrpLast=dummy

        while True:
            kth=self.getkthNode(prevGrpLast,k) # not (dummy,k)

            # if kth node is empty, just return dummy.next
            if not kth:
                return dummy.next

            nextGrpBeg=kth.next
            prev=nextGrpBeg
            cur=prevGrpLast.next

            if not cur:
                return dummy.next

            while cur!=nextGrpBeg:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt

            #we have to update the prevGrpLast=>we have to store the next of prevGrpLast before updating it
            newPrevGrpLast=prevGrpLast.next
            # now prev contains the kth node, now we have to connect the prevGrpLast to the prev(kth node)
            prevGrpLast.next=kth
            prevGrpLast=newPrevGrpLast

        return dummy.next

    def getkthNode(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1

        return cur

        