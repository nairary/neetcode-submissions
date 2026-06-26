# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None):
            return None
        elif (list1 == None):
            return list2
        elif (list2 == None):
            return list1

        dummy = ListNode()
        cur = dummy

        lcur, rcur = list1, list2
        while lcur != None:
            if rcur == None:
                cur.next = lcur
                return dummy.next

            if lcur.val <= rcur.val:
                cur.next = lcur
                lcur = lcur.next
            else:
                cur.next = rcur
                rcur = rcur.next

            cur = cur.next

        cur.next = rcur
        return dummy.next