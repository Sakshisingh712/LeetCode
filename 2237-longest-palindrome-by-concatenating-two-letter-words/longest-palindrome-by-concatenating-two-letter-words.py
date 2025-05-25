class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        mapping = Counter(words)
        # print(maps)
        res = 0
        alreadyPalindrome = 0
        for word, freq in mapping.items():
            string = word[::-1]
            if word == string:
                res += (freq // 2) * 4
                if freq % 2:
                    alreadyPalindrome = 1
            elif word < string and string in mapping:
                res += min(freq, mapping[string]) * 4
        return res + alreadyPalindrome * 2

        # mapping = {'symmetric': [], 'unsymmetric': []}
        # for w in words:
        #     if w[0] == w[1]:
        #         mapping['symmetric'].append(w)
        #     else:
        #         mapping['unsymmetric'].append(w)

        # res = 0
        # while len(mapping['unsymmetric']):
        #     ele = mapping['unsymmetric'].pop()
        #     mirrorEle = mirror(ele)
        #     if mirrorEle in mapping['unsymmetric']:
        #         res += 4
        #         # mapping['unsymmetric'].remove(ele)
        #         mapping['unsymmetric'].remove(mirrorEle)
        # extras = []
        # while len(mapping['symmetric']):
        #     ele = mapping['symmetric'].pop()
        #     if mapping['symmetric'].count(ele) >= 1:
        #         res += 4
        #         mapping['symmetric'].remove(ele)
        #         # mapping['symmetric'].remove(ele)
        #     else:
        #         extras.append(ele)
        # if extras:
        #     res += 2

        # return res       
        
