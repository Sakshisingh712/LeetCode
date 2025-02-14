class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        # print(answer[0].append([33]))
        # n1, n2 = [], []
        # for i in range(len(nums1)):
        #     if nums1[i] not in nums2 and nums1[i] not in n1:
        #         n1.append(nums1[i])
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1 and nums2[i] not in n2:
        #         n2.append(nums2[i])
        # answer.append(n1)
        # answer.append(n2)
        answer.append(list(set(nums1)-set(nums2)))
        answer.append(list(set(nums2)-set(nums1)))

        return answer