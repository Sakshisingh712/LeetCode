# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # print('return',prev)


        first = head
        second = prev
        max_sum = float('-inf')
        while second:
            max_sum = max(max_sum, (first.val + second.val))
            first = first.next
            second = second.next
        return max_sum