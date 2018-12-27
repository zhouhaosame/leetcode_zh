def searchInsert(nums,target):
    if not nums:return 0
    left,right,nums_len=0,len(nums)-1,len(nums)
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        else:
            return mid
        #会发现mid最后的位置是刚刚比target大的，如果没有找到的话。
        #所以target会占据mid的位置
    return mid if nums[mid]>target else mid+1
nums=[1,3,5,6]
target=7
print(searchInsert(nums,target))
