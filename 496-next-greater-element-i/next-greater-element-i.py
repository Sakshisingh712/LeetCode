class Solution:
    def process_nums2(x, stk):
        # print('X', x, stk)
        for ele in stk:
            # print('P', ele)
            if ele > x:
                return ele
        return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)==1:
            return [-1]
        ans = []
        sorted_dict = {}
        for i in range(len(nums2)-1):
            sorted_dict.update({ nums2[i]: Solution.process_nums2(nums2[i], nums2[i+1:])})
        sorted_dict.update({nums2[-1]: -1})
        # print(sorted_dict)
        for element in nums1:
            # print(element)
            # print(sorted_dict[element])
            ans.append(sorted_dict[element])
        return ans