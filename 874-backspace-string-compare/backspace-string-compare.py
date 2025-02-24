class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []

        for ele in s:
            if ele != '#':
                stack.append(ele)
            else:
                if stack:
                    stack.pop()
        s = ''.join(stack)
        stack.clear()
        for ele in t:
            if ele != '#':
                stack.append(ele)
            else:
                if stack:
                    stack.pop()
        t = ''.join(stack)
        stack.clear()
        if s == t:
            return True
        return False
        # len_s, len_t = len(s), len(t)
        # i,j = 0, 0
        # for _ in range(max(len_s,len_t)):
        #     ele1, ele2 = '',''
        #     if i < len_s:
        #         if s[i] != '#':
        #             ele1 = s[i]
        #         i += 1

        #     if j < len_t:
        #         if t[j] != '#':
        #             ele2 = t[j]
        #         j += 1
                
        #     if ele1!='' and ele2 != '' and ele1 == ele2:
        #         stack.append(ele1)
        # print(stack)
            