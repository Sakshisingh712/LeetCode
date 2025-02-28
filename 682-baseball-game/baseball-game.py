class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i=='C' and stack:
                # print(stack)
                stack.pop()
            elif i=='D' and stack:
                # print(stack[-1])
                stack.append(stack[-1]*2)
            elif i=='+' and len(stack)>1:
                print(stack[-1], stack[-2])
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)