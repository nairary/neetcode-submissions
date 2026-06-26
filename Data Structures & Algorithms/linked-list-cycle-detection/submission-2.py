# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow, fast = head, head
        while True:
            if slow.next == None or fast.next == None or fast.next.next == None:
                return False
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow.next != None