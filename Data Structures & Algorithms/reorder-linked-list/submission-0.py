# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def rotate(self, middle: Optional[ListNode]) -> ListNode:
        right = middle.next
        middle.next = None
        
        prev, cur = None, right
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev

    def findMiddle(self, head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = self.findMiddle(head)
        right = self.rotate(middle)
        
        left = head
        while right:
            right_tmp = right.next
            left_tmp = left.next

            left.next = right
            right.next = left_tmp

            right = right_tmp
            left = left_tmp