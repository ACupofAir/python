#%%
def jump(nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


line_len = input()
line = input()
lst_test = list(map(int, line.split()))
print(jump(lst_test)) 
# %%
