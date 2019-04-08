"""快速排序"""
def partition(low,high):
    pivot=nums[low]
    while(low<high):
        while(low<high and nums[high]>=pivot):
            high-=1
        nums[low]=nums[high]
        """temp=nums[low]
        nums[low]=nums[high]
        nums[high]=temp
        不需要交换，只要赋值就好啦。因为nums中的数是和pivot比较的
        所以只要在最后不要忘记吧nums[low]赋值为pivot就好啦"""
        while(low<high and nums[low]<=pivot):
            low+=1
        """temp=nums[low]
        nums[low]=nums[high]
        nums[high]=temp"""
        nums[high]=nums[low]
    nums[low]=pivot
    return low
def quickly_sort(low,high):
    if low>high:
        return
    i=partition(low,high)
    quickly_sort(low,i-1)
    quickly_sort(i+1,high)


"""然后使用归并排序"""
def merge(nums1,nums2):
    #nums1和nums2都是有序的
    i,j,nums=0,0,[]
    while(i<len(nums1) and j<len(nums2)):
        if nums1[i]<=nums2[j]:
            nums.append(nums1[i])
            i+=1
        else:
            nums.append(nums2[j])
            j+=1
    if i==len(nums1):
        """在这里要注意一下，i与j是否能同时是len(nums1)与len(nums2)
        因为每次只在nums中增加一个，所以不可能出现同时超过nums范围的情况
        而且nums与nums2都是存在的"""
        nums.extend(nums2[j:])############
        """注意了，这里一定要用extend，因为append是将[]作为元素添加的"""
    else:
        nums.extend(nums1[i:])
    return nums



def merge_sort(nums):
    """merge_sort的作用是将nums排序，使用了某种方法--合并排序"""
    l_nums=len(nums)
    if l_nums==1 or l_nums==0:
        return nums
    else:
        mid=l_nums//2
        """最简单的就是分成左右两部分"""
        nums_left=merge_sort(nums[:mid])
        nums_right=merge_sort(nums[mid:])
        """得到的nums_left和nums_right是有序的了"""
        return merge(nums_left,nums_right)
"""归并排序每次递归需要用到一个辅助表，长度与待排序的表相等，
虽然递归次数是O(log2n)，但每次递归都会释放掉所占的辅助空间，
所以下次递归的栈空间和辅助空间与这部分释放的空间就不相关了，
因而空间复杂度还是O（n）。

时间复杂度是NlogN。Tn=Tn/2+O(N),后面的N是合并所花费的时间。用二叉树
方法，"""
"""二分查找"""
def binary_search(nums,target):
    low,high=0,len(nums)-1
    while(low<=high):
        """是在low和high之间找--包括low和high
        所以要<=，因为如果只是小于的话，比如2,3.那么mid=2，索引
        为3的high将不能够被判断到"""
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False
    """bisect.bisect可以使用二分查找"""

"""如果面试的时候，要求你排序用N的时间复杂度，那么一般来说，
要排序的数组里面的数是在一个明确的范围之内的（比如员工的年龄）。
使用空间换时间的方法"""

nums=[1,3,4,5,5,6,7,4,5,8,9,10,2,3]
quickly_sort(0,len(nums)-1)#快排
print(nums)
nums=[1,3,4,5,5,6,7,4,5,8,9,10,2,3]
nums=merge_sort(nums)
print(nums)
print(binary_search(nums,4))

