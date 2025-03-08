class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = float('inf')
        i = 0
        j = k
        while j <= len(blocks):
            if blocks[i:j].count('B') < k:
                # print(blocks[i:j])
                w_count = min(w_count, blocks[i:j].count('W'))
                # print(w_count)
                i += 1
                j +=1
            elif blocks[i:j].count('B') == k:
                return 0
        return w_count
