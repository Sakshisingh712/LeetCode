class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = int(math.pow(len(grid),2))
        dup_dict = {}
        for row in grid:
            for element in row:
                count = 1
                if dup_dict and element in dup_dict.keys():
                    count += 1
                dup_dict[element] = count
        # print(dup_dict)
        repeated_num = 0
        grid_sum = 0
        for key, val in dup_dict.items():
            grid_sum += key
            if val == 2:
                repeated_num = key
        return [repeated_num,(n*(n+1)//2)-grid_sum]