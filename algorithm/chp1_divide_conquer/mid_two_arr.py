def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
    nums1.extend(nums2)
    nums1.sort()

    length = len(nums1)
    if length % 2 == 0:
        return (nums1[int(length/2 - 1)] + nums1[int(length/2)]) / 2.0
    else:
        return nums1[int((length+1)/2 - 1)]

