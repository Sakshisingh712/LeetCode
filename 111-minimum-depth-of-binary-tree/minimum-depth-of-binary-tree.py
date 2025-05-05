# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        
        # if root and root.left is None and root.right is None:
        #     return 1
        
        # if root.left is None:
        #     return self.minDepth(root.right) + 1

        # if root.right is None:
        #     return self.minDepth(root.left) + 1
        
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 

        if root is None:
            return 0
        
        queue = []

        queue.append({'node': root, 'depth': 1})

        while len(queue) > 0:
            item = queue.pop(0)
            # print(item)
            node = item['node']
            depth = item['depth']

            if node.left is None and node.right is None:
                return depth 
            
            if node.left:
                queue.append({'node': node.left, 'depth': depth + 1})

            if node.right:
                queue.append({'node': node.right, 'depth': depth + 1})
            
        