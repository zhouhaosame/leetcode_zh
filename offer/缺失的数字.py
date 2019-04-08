"""找到第一个i!=nums[i]的数,剑指offer上是排序的"""
def f(nums):
    if not nums:
        return 0
    left,right=0,len(nums)-1
    index=-1
    while(left<=right):
        mid=left+right
        if nums[mid]==mid:
            left=mid+1
        else:
            right=mid-1
            index=mid
    return index
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]
Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
leetcode上面是不排序的的。
每个索引都对应一个数，然后根据索引和数的关系去找
"""
def f_leetcode(nums):
    if not nums:
        return 0
    #从头到尾遍历一遍，将当前位置上的数放在它应该在的地方
    i,j=0,len(nums)
    while(i<j):
        if not(nums[i]==-1 or nums[i]==len(nums)):
            #因为最多只有一个number是超出len的，所以这个number可以忽略
            k=nums[i]#我们是将i位置处的数回归原处。所以要先知道他在那，里面才能循环，对于i位置本身，不需要在这里考虑置为-1
            while(k<len(nums) and k!=-1):
                temp=nums[k]
                nums[k]=-1
                k=temp
        i+=1
    for index,item in enumerate(nums):
        if item!=-1:
            return index
    return len(nums)
nums=[0,1,2]
print(f_leetcode(nums))

