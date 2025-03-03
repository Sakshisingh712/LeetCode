class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        equal = []
        ind = nums.index(pivot)
        for num in nums:
            if num<pivot:
                list1.append(num)
            elif num>pivot:
                list2.append(num)
            else:
                equal.append(num)
        list1.extend(equal)
        list1.extend(list2)   
        return list1
      