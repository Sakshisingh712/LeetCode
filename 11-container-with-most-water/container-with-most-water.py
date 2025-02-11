class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_val = 0
        maxHeight = max(height)
        while i<j:
            max_val = max(min(height[i], height[j])*(j-i),max_val)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            if maxHeight*(j-i)<=max_val:
                break
        return max_val