# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        
        # print(queue)
        
        ans = []
        
        while queue:
            levelSize = len(queue)
            # size = len(queue)
            tempRes = []
            while levelSize: 
                node = queue.popleft()
                tempRes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                levelSize -= 1
            ans.append(tempRes)

        return ans


            
            