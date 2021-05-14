def findMedianSortedArrays(nums1, nums2):
    infinty = 2**10
    n = len(nums1)
    left, right = 0, n
    median1, median2 = 0, 0

    while left <= right:
        i = (left + right) // 2
        j = n - i

        if i  == 0:
            nums_im1 = -infinty
        else:
            nums_im1 = nums1[i-1]
        if i  == n:
            nums_i = infinty
        else:
            nums_i = nums1[i]
        if j  == 0:
            nums_jm1 = -infinty
        else:
            nums_jm1 = nums1[j-1]
        if j  == n:
            nums_j = infinty
        else:
            nums_j = nums2[j]

        if nums_im1 <= nums_j:
            median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
            left = i + 1
        else:
            right = i - 1

    return (median1 + median2) / 2


n = input()
line = input()
lst_1 = list(map(int, line.split()))
line = input()
lst_2 = list(map(int, line.split()))
print(findMedianSortedArrays(lst_1, lst_2))
