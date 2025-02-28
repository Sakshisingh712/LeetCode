class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        #chr and ord is the function used to get ascii value.
        for i in s:
            if stack and i.islower() and stack[-1].isupper() and stack[-1].lower() == i:
                stack.pop()
            elif stack and i.isupper() and stack[-1].islower() and stack[-1].upper() == i:
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)