class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        ind=0
        if ch not in word:
            return word
        for i, w in enumerate(word):
            # print(w)
            stack.append(w)
            
            if word and w==ch:
                ind = i
                break 
        x = ''
        for i in range(ind+1, len(word)):
            x+=word[i]
        for i in stack:
            x = i + x
        return (x)
