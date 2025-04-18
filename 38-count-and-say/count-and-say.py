class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n - 1):
            result = []
            currCount = 1
            for i in range(1, len(prev)):
                if prev[i - 1] != prev[i]:
                    result.append(str(currCount) + prev[i - 1])
                    currCount = 1
                else:
                    currCount += 1
                i += 1
            result.append(str(currCount) + prev[-1])
            prev = "".join(result)

        return prev

        

    

        # def relHelper(string):
        #     result = ''
        #     uniqueEle = list(set(string))
        #     # print(string)
        #     for ele in uniqueEle:
        #         # print(ele, string, string.count(ele))
        #         result += str(string.count(ele)) + ele
        #         # print(result)
        #     return result
        # if n == 1:
        #     return str(n)      
        # res = '1'
        # for i in range(1, n):
        #     # print(i)
        #     res = relHelper(res)
        # return res
        
            