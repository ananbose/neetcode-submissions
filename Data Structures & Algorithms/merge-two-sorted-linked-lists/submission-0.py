# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        res = ListNode()
        head = res
        while temp1 and temp2:
            if temp1.val<temp2.val:
                res.next = temp1
                temp1= temp1.next
                res = res.next
            else:
                res.next = temp2 
                temp2=temp2.next
                res = res.next
        if temp1:
            res.next = temp1
        if temp2:
            res.next = temp2

        return head.next