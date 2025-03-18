# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            mid = len(nums)//2
            newNode = TreeNode(nums[mid])
            head = newNode
            # print(newNode)
            head.left = self.sortedArrayToBST(nums[:mid])
            head.right = self.sortedArrayToBST(nums[mid+1:])
            return newNode
        return None