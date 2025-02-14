class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = []
        unique =  set(arr)
        for i in unique:
            x = arr.count(i)
            if x in count:
                return False
            count.append(x)
        return True   
        