class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashT = {}
        for i in range(len(nums1)):
            hashT[nums1[i][0]] = nums1[i][1]
        for i in range(len(nums2)):
            if nums2[i][0] in hashT.keys():
                val = [hashT[nums2[i][0]]]
                hashT[nums2[i][0]] = val
                hashT[nums2[i][0]].append(nums2[i][1])
            else:
                hashT[nums2[i][0]] = nums2[i][1]
        hashT = dict(sorted(hashT.items()))
        ans = []
        for key, val in hashT.items():
            if type(val)==list:
                ans.append([key, sum(val)])
            else:
                ans.append([key, val])
        return ans