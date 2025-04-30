class Solution:
    def countDigit(self, num):
        count = 0
        while num > 0:
            count += 1
            num = num // 10
        # print(count)
        return count
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            count = self.countDigit(ele)
            if count % 2 == 0:
                res += 1
        return res