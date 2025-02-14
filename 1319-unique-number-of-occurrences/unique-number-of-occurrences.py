class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = []
        unique =  set(arr)
        for i in unique:
            count.append(arr.count(i))
        if len(set(count)) == len(count):
            return True
        else:
            return False
        