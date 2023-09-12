# Given the roots of two binary trees p and q, 
# write a function to check if they are the same or not.
# Two binary trees are considered the same if they are 
# structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
 
#Solution:

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None or (p.val!=q.val):
            return False
        else:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)