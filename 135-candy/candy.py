class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        # print(candy)
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                if candy[j] <= candy[j + 1]:
                    candy[j] = candy[j + 1] + 1
                # print(candy)
        print(candy)
        return sum(candy)
            
