# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, mp, minD, hd, root, lvl):
        if root is None:
            return 
        if hd not in mp:
            mp[hd] = []
        mp[hd].append((lvl, root.val))
        
        minD[0] = min(minD[0], hd)

        # self.dfs(mp, minD, hd + 1, root.right)
        self.dfs(mp, minD, hd - 1, root.left, lvl + 1)
        self.dfs(mp, minD, hd + 1, root.right, lvl + 1)


    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        minD = [0]
        mapping = {}
        
        self.dfs(mapping, minD, 0, root, 0)
        # print(mapping)
        hd = minD[0]
        res = []
        while hd in mapping:
    
            nodes = sorted(mapping[hd])
            # print(nodes)
            res.append([val for lvl, val in nodes])
            hd += 1
        return res
            
        