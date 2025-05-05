# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightView(self, root, currLevel, maxLevel, result):
        if root is None:
            return 

        if currLevel >  maxLevel[0]:
            result.append(root.val)
            maxLevel[0] = currLevel
        
        # self.rightView(root.left, currLevel + 1, maxLevel, result)
        self.rightView(root.right, currLevel + 1, maxLevel, result)
        self.rightView(root.left, currLevel + 1, maxLevel, result)



    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        maxLevel = [-1]

        self.rightView(root, 0, maxLevel, result)

        return result