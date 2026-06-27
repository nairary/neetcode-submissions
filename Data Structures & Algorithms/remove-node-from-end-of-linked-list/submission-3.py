# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head: Optional[ListNode]) -> (ListNode, int):
        slow, fast = head, head
        list_len = 0
        while fast and fast.next:
            list_len += 1
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            list_len = 2*list_len + 1
        else:
            list_len = 2*list_len

        return (slow, list_len)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mid, list_len = self.findMiddle(head)
        if list_len == 1:
            return None

        prev, cur = None, head
        counter = list_len - n
        if counter == 0:
            head = head.next
            return head
            
        while counter > 0:
            counter -= 1
            tmp = cur.next
            prev = cur
            cur = tmp

        prev.next = cur.next
        cur.next = None

        return head
