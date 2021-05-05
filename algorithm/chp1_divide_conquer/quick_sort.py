import random
def qsort(xs, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = xs[random.randint(fst, lst)]

    while i <= j:
        while xs[i] < pivot:
            i += 1
        while xs[j] > pivot:
            j -= 1

        if i <= j:
            xs[i], xs[j] = xs[j], xs[i]
            i, j = i + 1, j - 1
    qsort(xs, fst, j)
    qsort(xs, i, lst)
    return xs
line = input()
lst = list(map(int, line.split()))
lst_result = qsort(lst, 0, len(lst)-1)
for i in range(len(lst_result)):
    print(lst_result[i], end=" ")
