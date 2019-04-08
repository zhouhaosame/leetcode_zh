def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    无重复
    """
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while (left <= right):
        if nums[left] < nums[right] or right-left==0:
            return nums[left]
        """这里非常的重要，因为二分查找类似于分治（递归），就是在当前的left，right之间确定最小值可能在哪个新的left和
        right之间，然后再使用相同的方法去处理
        一定要先看这个新的left，right是不是递增的，或者是长度为1的"""
        mid = (left + right) // 2
        if mid==left:
            left=mid+1
            #这个很重要，因为mid是偏向left的，所以可能出现是0的情况，那么这时候只能够特殊处理
            #因为首先nums[0]不能是最小的，这样的话那么就是递增的了(无重复)
        elif nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def minNumberInRotateArray(rotateArray):#有重复的
    if not rotateArray:
        return 0
    left,right=0,len(rotateArray)-1
    while(left<=right):
        if rotateArray[left]<rotateArray[right] or right==left:
            return rotateArray[left]
        """这个也是非常的重要，因为当left+=1的时候，很有可能剩下的"""
        mid=(left+right)//2
        if mid==left:
            left=mid+1
        elif rotateArray[mid]<rotateArray[mid-1]:
            return rotateArray[mid]
        elif rotateArray[mid]<rotateArray[left]:
            right=mid-1
        elif rotateArray[mid]>rotateArray[left]:
            left=mid+1
        else:
            left+=1
            """最关键的一步，就是当相等的时候，可能在前半段也可能是在后半段，
            比如2,2,2,2,2,2,1,2,2（后半段）,2,2,1,2,2,2,2,2,（前半段）
            所以这正情况下
            我们已经知道nums[mid]不是最小值了，那么nums[left]也肯定不是最小值。所以left可以向后移动一位"""
    return rotateArray[0]
nums=[2,3,4,5,1]
print(findMin(nums))
print(minNumberInRotateArray(nums))