# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaves(self,root):
        if not root:
            return None
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node and not node.left and not node.right:
                ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans   
            # if not root.left and not root.right:
            #     ans.append(stack.pop())
        # leaves_list = []
        # if root:
        #     if not root.left and not root.right:
        #         return [root.val]
        #     leaves_list.extend(self.leaves(root.left))
        #     leaves_list.extend(self.leaves(root.right))
        # return leaves_list
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if self.leaves(root1) == self.leaves(root2):
            return True
        return False
        