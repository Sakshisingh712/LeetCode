# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            #it will set first element at last and last to first so reversing the string
            next_node = current.next ## next = 2, next = 3, next = 4, next = 5
            # print('next',next_node)
            current.next = prev #1-> None, 2->1->None, 3->2->1->None .....
            # print('current.next', prev)
            prev = current #prev = 1, prev = 2 prev = 3, prev= 4
            # print('prev', current)
            current = next_node #current = 2, current = 3
            # print('current', next_node)
        return prev