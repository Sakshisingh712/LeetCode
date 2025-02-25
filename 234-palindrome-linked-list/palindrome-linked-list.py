# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # stack = []
        if head is not None and head.next is None:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle_element = slow
        prev = None
        while middle_element:
            next_node = middle_element.next
            middle_element.next = prev
            prev = middle_element
            middle_element = next_node
        # print(head) 
        # print(prev)  
        first, second = head, prev
        while second:
            # print()
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

            

        