# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            leftCount = self.maxDepth(root.left)
            rightCount = self.maxDepth(root.right)
            return max(leftCount, rightCount) + 1

        