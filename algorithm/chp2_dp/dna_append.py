#%%
def sort_arr(lst):
    res = []
    for y in range(0, int(len(lst)/2)):
        for x in range(0, 2):
            if x == 0:
                res.append([])
            res[y].append(lst[x + y * 2])
    res = sorted(res, key=(lambda x: x[0]))
    return res

#%%
def select_arr_head(left, right, intervals):
    res = []
    for interval in intervals:
        if (interval[0] <= right) and (interval[0] >= left):
            res.append(interval)
    if res :
        res = sorted(res, key=(lambda x: x[1]), reverse=True)
        intervals.remove(res[0])
        return res[0]
    else:
        return 0
#%%
def merge(intervals, target):
    merged = [[0, 0]]
    sum = 0
    while merged[-1][1] != target:
        temp = select_arr_head(merged[-1][0], merged[-1][1], intervals)
        if temp:
            merged[-1][1] = temp[1]
            sum += 1
        else:
            return -1
    if merged[-1][1] != target:
        return -1
    else: 
        return sum


#%%
target = int(input())
line = input()
lst_test = list(map(int, line.split()))
#%%
print(merge(sort_arr(lst_test), target))

#%%
line = input()
lst_test = list(map(int, line.split()))
sorted_arr = sort_arr(lst_test)
print(sorted_arr)