# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            # temp = head
            # head = head.next
            # temp = None
            return head.next

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        temp = head
        
        while temp != slow:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return head
