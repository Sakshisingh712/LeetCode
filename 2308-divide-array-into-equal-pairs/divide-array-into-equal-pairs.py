class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numDict = {}
        x = len(nums)//2
        for n in nums:
            if n not in numDict:
                numDict[n] = nums.count(n)
        # print(numDict)
        for key, val in numDict.items():
            # print(key)
            if val % 2 != 0:
                return False
        return True
