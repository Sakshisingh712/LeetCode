class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # list1 = []
        # list2 = []
        # equal = []
        # ind = nums.index(pivot)
        # for num in nums:
        #     if num<pivot:
        #         list1.append(num)
        #     elif num>pivot:
        #         list2.append(num)
        #     else:
        #         equal.append(num)
        # list1.extend(equal)
        # list1.extend(list2)   
        # return list1
        equal = 0
        numLess = 0
        ans = [0]*len(nums)
        for num in nums:
            if num < pivot:
                numLess += 1
            elif num == pivot:
                equal += 1
        ptrLess = 0
        ptrEqual = numLess
        ptrGreater = numLess + equal
        # print(ptrLess,ptrEqual,ptrGreater)
        for num in nums:
            if num < pivot:
                ans[ptrLess] = num
                ptrLess += 1
            elif num == pivot:
                ans[ptrEqual] = num
                ptrEqual += 1
            elif num > pivot:
                ans[ptrGreater] = num
                ptrGreater += 1
        return ans