class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count = 0
        if len(word2)>len(word1):
            return False
        else:
            list1, list2 = [], []
            # word1, word2 = sorted(word1),
            set1 = list(set(word1))
            set2 = list(set(word2))
            if set(word1)==set(word2):
                for i in range(len(set1)):
                    list1.append(word1.count(set1[i]))
                    # print(word1[i], list1)
                    list2.append(word2.count(set2[i]))
                    # print(word2[i], list2)
                if sorted(list1) == sorted(list2):
                    return True
            return False

            