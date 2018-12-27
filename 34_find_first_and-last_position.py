#能不能先用二分法找到index，然后两边扩展？？
"""又是二分法的变种，再找到target的时候，不要直接返回最先找到的index，而是继续往下寻找，
直到left==right。下面的代码展示的分别是两种二分方法，先找最左边的，再找最右边的"""
def searchRange(nums,target):
    if not nums:return [-1,-1]
    left,right,nums_len,left_index,right_index=0,len(nums)-1,len(nums),-1,-1
    while(left<right):#这边是找最左边的，是<号
        ##这里虽然没有<=,但是没有比较的拿一个元素，拿到外面单独比较了
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:#当等于target的时候，继续往前面找，直到left==right 且 nums[left]==target
            right=mid-1
        else:right=mid
        #当找到相等的值之后，right=mid，因为mid=(left+right)//2，最终会mid=left,进入到其中，
        #right总会和left相遇
    if left==right and nums[left]==target:
        left_index=left
    if left_index!=-1:
        left,right=left_index,nums_len-1
    else:return [-1,-1]
    while (left < right):
        mid = (left + right+1)//2
        #这里的+1处理非常的重要，是为了mid最终会和right重合（即right偏向右移动），和上面的
        #偏向左的相反的
        if nums[mid]>target:#不必考虑<的了，因为现在遍历的列表里面不可能有大于target的
            right = mid - 1
        else:left=mid
    right_index=left
    return [left_index,right_index]
nums=[5,7,7,8,8,10]
target=6
print(searchRange(nums,target))