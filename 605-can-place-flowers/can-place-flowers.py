class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # numofZero = flowerbed.count(0)
        # pos=0
        # index  = []
        num=len(flowerbed)
        i=0
        if num<=1:
            if n==0:
                return True
            else:
                if n==1 and flowerbed[0]==0:
                    return True
                return False
        while i <=num-1:
            if n==0:
                break
            if i==0 and flowerbed[i+1]!=1 and flowerbed[i]==0:
                n-=1
                print('I1', i, n)
                i+=2
            elif i!= num-1 and flowerbed[i+1]!=1 and flowerbed[i-1]!=1 and flowerbed[i]==0:
                n-=1
                print('I2', i, n)
                i+=2
            elif i==num-1 and flowerbed[i-1]!=1 and flowerbed[i]==0:
                n-=1
                print('I3', i, n)
                i+=2
            else:
                i+=1
        if n==0:
            return True
        return False
        # if num<=1:
        #     if n==0:
        #         return True
        #     elif n==1 and flowerbed[0]==0:
        #         return True
        #     return False
        # elif all(s==0 for s in flowerbed):
        #     if num%2==0:
        #         if n<= num//2:
        #             return True
        #         return False
        #     else:
        #         if n<= num//2+1:
        #             return True
        #         return False
        # else:
        #     if flowerbed[0] == 0:
        #         i=2
        #         if flowerbed[1]!=1:
        #             index.append(0)
        #             pos += 1
        #         while i<=num-1:
        #                 # print(i)
        #                 if i==num-1:
        #                     # print('I', i)
        #                     if flowerbed[i-1]!=1 and flowerbed[i]!=1:
        #                         if num%2!=0 and i-2 not in index:
        #                         # print('i',i)
        #                             index.append(i)
        #                             pos+=1
        #                             i+=2
        #                         elif num%2==0:
        #                             index.append(i)
        #                             pos+=1
        #                             i+=2
        #                     else:
        #                         i+=1
        #                 elif flowerbed[i-1]!=1 and flowerbed[i+1]!=1 and flowerbed[i]!=1:
        #                     # print('i',i)
        #                     index.append(i)
        #                     pos += 1
        #                     i += 2
        #                     # print('i',i)
        #                 else:
        #                     i+=1
        #             # print(i, pos)
        #     elif flowerbed[0] == 1:
        #         i=2
        #         while i<=num-1:
        #                 # print(i)
        #                 if i==num-1:
        #                     # print(index)
        #                     if flowerbed[i-1]!=1 and flowerbed[i]!=1:
        #                         index.append(i)
        #                         pos+=1
        #                 elif flowerbed[i-1]!=1 and flowerbed[i+1]!=1 and flowerbed[i]!=1:
        #                     index.append(i)
        #                     pos += 1
        #                 i+=2  
        #         # print(pos)  
        #     if pos>=n:
        #         return True
        #     return False


