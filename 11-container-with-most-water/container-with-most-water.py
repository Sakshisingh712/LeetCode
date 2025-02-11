class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        max_val = float('-inf')
        while i<j:
            print(i, j)
            length = min(height[i], height[j])
            width = abs(j-i)
            amount = length*width
            # print(i, j, amount)
            if amount > max_val:
                max_val = amount
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_val