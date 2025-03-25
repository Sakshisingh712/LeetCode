class Solution:
    def check(self, interval):
        interval.sort()
        max_end = interval[0][1]
        sections = 0
        for start, end in interval:
            if max_end <= start:
                sections += 1
            max_end = max(max_end, end)
        return sections>=2

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_interval, y_interval = [], []
        for x in rectangles:
            x_interval.append([x[0], x[2]])
            y_interval.append([x[1], x[3]])
        return self.check(x_interval) or self.check(y_interval)

