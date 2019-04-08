def f(nums, values):
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    left_index, right_index = -1, -1
    while (left <= right):
        mid = (left + right) // 2
        if nums[mid] == values:
            left_index = mid
            right = mid - 1
        elif nums[mid] < values:
            left = mid + 1
        else:
            right = mid - 1
    if left_index != -1:
        left = left_index
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == values:
                right_index = mid
                left = mid + 1
            elif nums[mid] < values:
                left = mid + 1
            else:
                right = mid - 1
    return right_index-left_index+1 if left_index!=-1 else 0
nums=[1,2,3,3,3,3,3,3,4,4,6]
print(f(nums,9))
