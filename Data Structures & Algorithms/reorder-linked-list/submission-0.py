# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes=[]
        tmp=head

        while tmp:
            nodes.append(tmp)
            tmp=tmp.next

        midIdx=len(nodes)//2
        nodes[midIdx:]=nodes[midIdx:][::-1] #imp
 
        p1,p2=0,midIdx
        dummy=ListNode()
        tail=dummy
        while p2<len(nodes):
            if p1<midIdx:
                tail.next=nodes[p1]
                tail=tail.next
                p1+=1
            tail.next=nodes[p2]
            p2+=1
            tail=tail.next

        if p1<midIdx:
            tail.next=nodes[p1]
            tail=tail.next
        
        tail.next=None

        head.val=dummy.next.val
        head.next=dummy.next.next
