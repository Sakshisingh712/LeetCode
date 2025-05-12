class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n =  len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j==k or k==i:
                        continue
                    num = ((digits[i] * 10) + digits[j]) * 10 + digits[k]
                    # print(digits[i], digits[j], digits[k])
                    if num >= 100 and num % 2 == 0:
                        res.add(num)
        res = sorted(list(res))
        return res
