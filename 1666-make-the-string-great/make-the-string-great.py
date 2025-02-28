class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        # print(ord('s'))
        for i in s:
            if stack and abs(ord(i)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(i)
        print(stack)
            # if stack and i.islower() and stack[-1].isupper() and stack[-1].lower() == i:
            #     stack.pop()
            # elif stack and i.isupper() and stack[-1].islower() and stack[-1].upper() == i:
            #     stack.pop()
            # else:
            #     stack.append(i)
        
        return ''.join(stack)