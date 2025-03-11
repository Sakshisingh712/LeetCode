class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        hash_table = {'a': -1,'b': -1, 'c': -1}
        for right in range(len(s)):
            hash_table[s[right]] = right
            count += max(0, min(hash_table.values())+1)
        return count
        