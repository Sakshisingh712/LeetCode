# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return True
        elif not leftNode or not rightNode:
            return False
        else:
            if leftNode.val == rightNode.val and self.check(leftNode.left, rightNode.right) and self.check(leftNode.right, rightNode.left):
                return True
            else:
                return False
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.check(root.left, root.right)
         