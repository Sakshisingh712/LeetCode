class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ele in s:
            if ele != '#':
                stack1.append(ele)
            else:
                if stack1:
                    stack1.pop()
        for ele in t:
            if ele != '#':
                stack2.append(ele)
            else:
                if stack2:
                    stack2.pop()
        if stack1 == stack2:
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
            