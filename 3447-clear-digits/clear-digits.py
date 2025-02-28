class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        # print(s == '')
        for i in s:
            # print(i)
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)