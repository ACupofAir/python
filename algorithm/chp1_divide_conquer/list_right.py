import bisect


def countSmaller(nums:list[int]) -> list[int]:
    sortns = []
    res = []
    for n in reversed(nums):
        index = bisect.bisect_left(sortns, n)
        res.append(index)
        sortns.insert(index, n)
    return res[::-1]


line = input()
lst_val_test = list(map(int, line.split()))
lst_right_result = countSmaller(lst_val_test)
for i in range(len(lst_right_result)):
    print(lst_right_result[i], end=" ")
