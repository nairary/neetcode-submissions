# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow        

    def revertList(self, head: Optional[ListNode], middle: Optional[ListNode]) -> ListNode:
        left = head
        right = middle.next
        middle.next = None

        prev, cur = None, right
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMiddle(head)
        right = self.revertList(head, mid)

        left = head
        while right:
            left_tmp, right_tmp = left.next, right.next

            left.next = right
            right.next = left_tmp

            left, right = left_tmp, right_tmp