def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    max_part1, min_part2 = 0, 0

    while left <= right:
        i = (left + right) // 2
        j = (m + n) // 2 - i

        nums_im1 = nums1[i - 1]
        nums_i = nums1[i]
        nums_jm1 = nums2[j - 1]
        nums_j = nums2[j]

        if nums_im1 <= nums_j:
            max_part1, min_part2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
            left = i + 1
        else:
            right = i - 1

    return (max_part1 + min_part2) / 2


n = input()
line = input()
lst_1 = list(map(int, line.split()))
line = input()
lst_2 = list(map(int, line.split()))
print(findMedianSortedArrays(lst_1, lst_2))
