# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        from collections import deque
        level = 1
        maxSum = float('-inf')
        
        maxLevel = 0

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            sums = 0
            for _ in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                sums += curr.val
                # print(level, sums)

            if sums > maxSum:
                maxSum = sums
                maxLevel = level
            
            level += 1

        return maxLevel

        