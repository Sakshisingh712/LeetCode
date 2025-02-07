class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num=len(flowerbed)
        i=0
        if num<=1:
            if n==0:
                return True
            elif flowerbed[0]==0 and n==1:
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
        