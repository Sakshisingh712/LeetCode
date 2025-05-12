class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        #-----------Optimised Solution------------------------------
        count = [0] * 10
        for d in digits:
            count[d] += 1
        # print(count)
        result = []

        for i in range(100, 1000, 2):  # Only even numbers
            a = i // 100
            b = (i // 10) % 10
            c = i % 10

            count[a] -= 1
            count[b] -= 1
            count[c] -= 1
            # print(count)
            if count[a] >= 0 and count[b] >= 0 and count[c] >= 0:
                result.append(i)

            count[a] += 1
            count[b] += 1
            count[c] += 1
            # print(count)
        return result

        #---------Brute Force-------------------------------------
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i == j or j==k or k==i:
        #                 continue
        #             num = ((digits[i] * 10) + digits[j]) * 10 + digits[k]
        #             # print(digits[i], digits[j], digits[k])
        #             if num >= 100 and num % 2 == 0:
        #                 res.add(num)
        # res = sorted(list(res))
        # return res
