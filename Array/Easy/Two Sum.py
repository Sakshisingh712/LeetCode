# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Time Complexity: O(n^2)

#Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(nums):
            x=target-j
            if x in d:
                return [d[x],i]
            d[j]=i