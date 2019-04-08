def search_min_in_rotate_array(nums):
    """85页的在旋转数组中寻找最小的值"""
    if not nums:
        return nums
    min_value=nums[0]
    left,right=0,len(nums)-1
    while(left<=right):
        mid=(left+right)//2
        """这里min_value的初值是前段数组的最小值，所以这个mid肯定在第二段"""
        if nums[mid]<min_value:
            min_value=nums[mid]
            right=mid-1
            #mid在第二段
        elif nums[mid]>min_value:
            """与上面同理，这时候，mid在第一段。因为即使min_value被第二段中的某个给赋值了，第二段前面的是不会
            大于它的"""
            left=mid+1
        else:#这时候mid与min_value相等
            if nums[mid]<nums[0]:#说明已经有过赋值了，这时候只可能是第二段中的mid的值等于最小值。如[5,6,1,1,1,1,1,2]
                right=mid-1
            else:#这个时候，nums[mid]==nums[0]就是刚开始的时候，这时候，mid可能在第一段也可能在第二段。
                #如[1,1,0,1,1,1,1,1,1,1]在第二段，[1,1,1,1,1,1,0,0]在第一段。所以这时候只能够顺序索引
                return min(nums[left:right+1])
    return min_value
#44%

def find(nums,low,high):
    if low==high:
        return nums[low]
    mid=(low+high)//2
    return min(find(nums,low,mid),find(nums,mid+1,high))
"""旋转数组的递归二分查找，时间是NlogN"""


nums=[5,6,7,8,1,2,3,4,5]
nums=[2,3,4,5,6,7]
nums=[1,1,1,0,1,1,1,1,1]
print(search_min_in_rotate_array(nums))
print(find(nums,0,len(nums)-1))