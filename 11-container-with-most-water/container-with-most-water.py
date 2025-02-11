class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        max_val = float('-inf')
        maxHeight = max(height)
        while i<j:
            max_val = max(min(height[i], height[j])*(j-i),max_val)
            # print(i, j, amount)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            if maxHeight*(j-i)<=max_val:
                break
        return max_val