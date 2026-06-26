# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        elif head.next==None:
            return head

        prev = ListNode()

        curr = head
        flag = False

        while curr != None:
            tmp = curr.next
            if flag:
                curr.next = prev
            else:
                curr.next = None
            
            prev = curr
            curr = tmp
            flag = True

        return prev