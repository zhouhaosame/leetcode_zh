def search(nums,target):
    """时间复杂度是O（logn），这就是意味着二分法的方法
    相比于普通的二分法，这种情况下的二分法肯定是有所不同
    之前写的时候，考虑的太精致了，当考虑的很精致时，往往是错误的

    """
    if not nums:return -1
    left,right,nums_l=0,len(nums)-1,len(nums)
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]==target:return mid
        if nums[left]<nums[right]:
            #这种情况下明显就是普通的二分法了
            if nums[mid]<target:
                left=mid+1
            else:right=mid-1
        else:
            #这种情况下，left在左边，right在右边,要按照mid在左还是在右考虑
            if nums[left]<=nums[mid]:
                #说明mid在左部分
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:left=mid+1
            else:#这时说明mid在右边
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:right=mid-1
    return -1
nums=[1,3]
target=1
print(search(nums,target))


