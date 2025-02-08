class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        n=len(chars)
        CompStr = []
        # print(len(set(chars))==1)
        if len(chars)==1:
            return 1
        elif len(set(chars))==1:
            CompStr.append(chars[0])
            count = len(chars)
            print(count)
            if count>1 and count<10:
                CompStr.append(str(count))
            elif count>=10:
                new_count = list(str(count))
                for i in new_count:
                    CompStr.append(i)
            for i in range(len(CompStr)):
                chars[i] = CompStr[i]
            return len(chars[:len(CompStr)])    
            
        for i in range(len(chars)-1):
            if chars[i]!=chars[i+1]:
                CompStr.append(chars[i])
                if count>1 and count<10:
                    CompStr.append(str(count))
                    count = 1
                elif count>=10:
                    new_count = list(str(count))
                    print(new_count)
                    for i in new_count:
                        CompStr.append(i)
                    count=1
            else:
                count+=1

        CompStr.append(chars[n-1])
        if count>=10:
            new_count = list(str(count))
            for i in new_count:
                CompStr.append(i)
        elif count>1 and count<10:
            CompStr.append(str(count))
        
        for i in range(len(CompStr)):
            chars[i] = CompStr[i]
        return len(chars[:len(CompStr)])
