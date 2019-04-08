"""找到一个pivot，这个pivot的左边是满足某种类型的，右边也是满足某种类型的。可以定义一个类型函数，那么这个不就是封装
了吗，这个和快排还是不一样的。没必要去找pivot。因为快排中，函数和pivot所指的是有关的，所以可以"""
def isOld(x):
    if x&1:
        return 1
    else:
        return 0
def reset_nums(nums):
    if not nums:
        return nums
    nums_len=len(nums)
    left,right=0,nums_len-1
    while(left<right):
        while(left<right and not isOld(nums[right])):
            right-=1
        while(left<right and isOld(nums[left])):
            left+=1
        if left<right:
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp

nums=[1,2,3,4,5,6,7,8,9,10,11]

reset_nums(nums)
print(nums)