class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = int(math.pow(len(grid),2))
        dup_dict = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                count = 1
                # print(j)
                if dup_dict and grid[i][j] in dup_dict.keys():
                    count += 1
                dup_dict[grid[i][j]] = count
        repeated_num = 0
        grid_sum = 0
        # print(dup_dict)
        for key, val in dup_dict.items():
            grid_sum += key
            if val == 2:
                repeated_num = key
        # print((n*(n+1)//2))
        return [repeated_num,(n*(n+1)//2)-grid_sum]