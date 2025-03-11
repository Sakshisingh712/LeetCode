class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        hash_table = {'a': -1,'b': -1, 'c': -1}
        for right in range(len(s)):
            hash_table[s[right]] = right
            count += max(0, min(hash_table.values())+1)
        del hash_table
        return count
        # left = 0
        # for right in range(len(s)):
        #     hash_table[s[right]] += 1
        #     while min(hash_table.values())>0:
        #         count += len(s) - right
        #         hash_table[s[left]] -= 1
        #         left += 1
        # del hash_table
        # return count