class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        nums = sorted(nums)

        curr = Counter(nums)
        # print(curr)
        n = len(curr)
        # print(enumerate(curr))
        # print(n)
        for key, val in curr.items():
            print(key)
            if curr[key] >= 2:
                return True
        return False
