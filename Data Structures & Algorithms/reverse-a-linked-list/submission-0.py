# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #  0->1->2->3->None
    #     so the next pointer should point from 2 to 0 but the next-> next pointer should be also saved so you can go there
        curr = head
        prev = None
        while(curr):
            tmp = curr.next # tmp = 1
            curr.next = prev 
            prev = curr
            curr = tmp
        return prev
