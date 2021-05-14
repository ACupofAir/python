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
lst_test = list(map(int, line.split()))
print(c)
