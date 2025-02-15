class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        win = []
        max_len = 0
        if nums.count(1)==len(nums):
            print(set(nums))
            return len(nums)-1
        elif nums.count(0)==len(nums):
            return 0
        else:
            while i<len(nums):
                if i==0 and nums[i]==0:
                    i+=1
                if nums[i]==1:
                    win.append(nums[i])
                elif nums[i]==0:
                    if win.count(0)==1:
                            max_len = max(max_len, len(win)-win.count(0))
                            # print('max1', max_len)
                            win = win[win.index(0)+1:]
                            win.append(nums[i])
                    else:
                        win.append(nums[i])
                if i == len(nums)-1:
                    max_len = max(max_len, len(win)-win.count(0))
                    # print(win)
                    # print('in',max_len)
                i+=1
                # print(win, i)
            return max_len  