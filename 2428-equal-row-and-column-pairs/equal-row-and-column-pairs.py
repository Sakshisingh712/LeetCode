class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dictR = {}
        dictC = []
        for i in range(len(grid[0])):
            val = ''
            val2 = ''
            for j in range(len(grid[0])):
               val += str(grid[i][j])+'_'
               val2 += str(grid[j][i])+'_'
            dictR[i] = val
            dictC.append(val2)
        count = 0
        print(dictR, dictC)
        for i in range(len(dictR)):
            if dictR[i] in dictC:
                count += dictC.count(dictR[i])
        return count