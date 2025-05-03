class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        freqTop = Counter(tops + bottoms)
        maxFreq = 0
        count = 0
        num = 0
        for i, val in freqTop.items():
            if val > maxFreq:
                maxFreq = val 
                num = i
    
        CountTop = tops.count(num)
        CountBottom = bottoms.count(num)
        # print(list(set(tops))) 
        if (list(set(tops))[0] == num and len(list(set(tops)))== 1)or (list(set(bottoms))[0] == num and len(list(set(tops)))== 1):
            return 0
        

        if CountTop >= CountBottom:
            for i in range(len(tops)):
                # if tops[i] == bottom[i]:
                #     continue
                if bottoms[i] == num and tops[i] != num:
                    tops[i], bottoms[i] = bottoms[i], tops[i]
                    count += 1
            # print(list(set(tops)))
            if (list(set(tops))[0] == num and len(list(set(tops)))== 1):
                return count
        else:
            print(CountBottom)
            for i in range(len(tops)):
                if tops[i] == num and bottoms[i] != num:
                    count += 1
                    tops[i], bottoms[i] = bottoms[i], tops[i]
            print(bottoms, tops, count)
            if (list(set(bottoms))[0] == num and len(list(set(bottoms)))== 1):
                return count
        return -1

        