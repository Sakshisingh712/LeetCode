class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        # IceCreAm
        # leetcode
        s=s.strip('')
        string = list(s)
        print(string)
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        i=0
        j=length-1
        while(i<j):
            if string[i] in vowels:
                if string[j] in vowels:
                    string[i], string[j] = string[j], string[i]
                    i+=1
                j-=1
            elif string[j] in vowels:
                if string[i] in vowels:
                    string[i], string[j] = string[j], string[i]
                    j-=1
                i+=1
            else:
                i+=1
                j-=1
        string= ''.join(string)
        return string