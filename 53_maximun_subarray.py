def maxSubArray(nums):
    #这题的解题点是---left和right之间的sum，表示的就是sum_temp，需要和sum_max
    #进行比较，当right+=1时，求得的sum_temp需要再次比较。如果right+=1后，sum_temp
    #可能减小，这个不碍事，因为和sum_max比较了，大的话保留，小的话继续扩大right，但是如果right+1
    #后，sum_temp<0了，这就意味着left和right之间已经是 毒瘤 了。这时候，left右移，直到
    #sum(left:right+1)>0 或者left>right
    #left和right之间的sum>0的
    sum_max,i=float('-inf'),0
    while(i<len(nums)):
        if nums[i]>0:
            break
        elif nums[i]>sum_max:
            sum_max=nums[i]
        i+=1
    if i==len(nums):return sum_max
    left,right,sum_max=i,i,nums[i]
    while(left<len(nums) and right<len(nums)-1):#left有时会超过right一个，当完全结束第三个选择的时候
        right+=1
        sum_temp = nums[left] if left == right else sum(nums[left:right + 1])
        if sum_temp>sum_max:#!!!!!!!!!!!!注意了，原来不是sun_max而是sum，用sum作为变量当然时错的
            sum_max=sum_temp
        elif sum_temp>0:
            continue
        else:
            while(left<=right):
                s = nums[left] if left == right else sum(nums[left:right + 1])
                if s<=0:#注意了<=,只是<0可能会出现死循环
                    left+=1
    return sum_max

def so_so_so_brilliant():
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)
#思想是：只可意会。ej,[2,-3,1,2,3,-6,5,3,-1,2]就变成了
#[2,-1,1,3,6,0,5,8,7,9]
#超过1%,真是无语



nums=[1,-1,1]
print(maxSubArray(nums))


