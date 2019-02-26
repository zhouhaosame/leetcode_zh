def find_maximum_subarray_sum(nums):
    if not nums:
        return nums
    max_sum_list=[0]*len(nums)
    max_sum_list[0]=nums[0]
    for i in range(1,len(nums)):
        if max_sum_list[i-1]>0:
            max_sum_list[i]=max_sum_list[i-1]+nums[i]
        else:
            max_sum_list[i]=nums[i]
    return max(max_sum_list)
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(find_maximum_subarray_sum(nums))
