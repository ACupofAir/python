def majorityelement(nums):
    votes = 0
    for num in nums:
        if votes == 0:
            x = num
        if num == x:
            votes += 1
        else:
            votes -= 1
    return x

n = input()
line = input()
lst = list(map(int, line.split()))
print(majorityelement(lst))
