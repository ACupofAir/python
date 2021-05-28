def jumpStep(nums):
  n, rightmost, step = len(nums), 0, 0
  for i in range(n):
    if i <= rightmost:
      if rightmost < (i + nums[i]):
        rightmost = i + nums[i]
        step += 1
      if rightmost >= n - 1:
          return step



line_len = input()
line = input()
lst_test = list(map(int, line.split()))
print(jumpStep(lst_test)) 