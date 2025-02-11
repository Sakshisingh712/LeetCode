class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j =0, 0
        temp = ''
        if not s:
            return True
        while j<len(t):
            if s[i]==t[j]:
                temp+=s[i]
                i+=1
                j+=1
                print(i, j, temp)
            else:
                j+=1
                print(j)
            if i==len(s):
                break
        if temp==s:
            return True
        else:
            return False