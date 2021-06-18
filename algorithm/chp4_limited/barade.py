def massage(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp0, dp1 = 0, nums[0]
    for i in range(1, n):
        tdp0 = max(dp0, dp1) 
        tdp1 = dp0 + nums[i] 
        dp0, dp1 = tdp0, tdp1
    
    return max(dp0, dp1)


line_cusomers = input()
line_cusomers_int = list(map(int, line_cusomers.split()))
print(massage(line_cusomers_int))
