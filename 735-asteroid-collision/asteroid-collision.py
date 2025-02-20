# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         j = 0
#         n = len(asteroids)
#         stack = []
#         # print(not stack)
#         for i in range(n):
#             if not stack:
#                 stack.append(asteroids[i])   
#                 continue 
#             if stack[-1]>0:
#                 if asteroids[i]<0:
#                     # if abs(stack[-1])>abs(asteroids[i]):
#                     #     break
#                     if abs(stack[-1])==abs(asteroids[i]):
#                         stack.pop()
#                     elif abs(stack[-1])<abs(asteroids[i]):
#                         last_pop = 0
#                         while stack and abs(stack[-1])<=abs(asteroids[i]) and stack[-1]>0 and asteroids[i]<0:
#                             last_pop = stack[-1]
#                             stack.pop()
#                             if last_pop==abs(asteroids[i]):
#                                 break
#                         if stack and stack[-1]<0 and abs(last_pop)<abs(asteroids[i]):
#                             stack.append(asteroids[i])
#                             # print(asteroids[i], '  ', last_pop)
#                         if not stack:
#                             stack.append(asteroids[i])
#                 else:
#                     stack.append(asteroids[i])
#             elif stack[-1]<0:
#                 stack.append(asteroids[i])
#                 print(stack)
#         return stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j = 0
        n = len(asteroids)

        for i in range(n):
            asteroid = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1

            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid
                j += 1
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1
        return asteroids[:j]