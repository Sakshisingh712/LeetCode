class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0 
        max_count = 0
        if len(s)==1 and s in vowels:
            return 1
        else:
            i, j = 0, 0
            while j < len(s):
                if j-i +1 <= k:
                    if s[j] in vowels:
                        count += 1
                    j += 1
                    max_count = max(max_count, count)
                else:
                    if s[i] in vowels:
                        count -= 1
                    if s[j] in vowels: 
                        count += 1
                    max_count = max(count, max_count)
                    i += 1
                    j += 1
            return max_count
        return 0