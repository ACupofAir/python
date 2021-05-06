def countSmaller(nums):
    nums = list(enumerate(nums)) 
    cnt = [0 for _ in range(len(nums))] 
    def mergesort(nums):
        n=len(nums)
        if n<2: return
        mid = n//2
        nums_l, nums_r = nums[0:mid], nums[mid:n]
        mergesort(nums_l) 
        mergesort(nums_r)
        i, j = 0, 0 
        while i+j<n:
            if (i<mid and j<n-mid and nums_l[i][1]<=nums_r[j][1]) or (j==n-mid):
                nums[i+j]=nums_l[i]
                cnt[nums[i+j][0]] += j 
                i+=1
            else:
                nums[i+j]=nums_r[j]
                j+=1
    mergesort(nums)
    return cnt


line = input()
lst_val_test = list(map(int, line.split()))
lst_right_result = countSmaller(lst_val_test)
for i in range(len(lst_right_result)):
    print(lst_right_result[i], end=" ")
