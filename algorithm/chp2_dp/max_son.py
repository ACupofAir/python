def maxSubArray(nums):
    left, right = 1, 1
    onesum = 0
    maxsum = nums[0]
    for i in range(len(nums)):
        onesum += nums[i]
        if maxsum < onesum:
            right = i + 91
        maxsum = max(maxsum, onesum)
        if onesum < 0:
            onesum = 0
            left = i + 1
    return maxsum, left, right


case_num = int(input())
while case_num > 0:
    line = input()
    lst_test = list(map(int, line.split()))
print(maxSubArray(lst_test))
