def lengthOfLIS(nums):
    if not nums: return 0
    dp=[1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[j]+1,dp[i])
    return max(dp)
#%6
def dp_and_binary_search(nums):
    import bisect
    """
    关于bisect：
    这是一个python的针对有序 数组的插入和排序操作的一个模块
    bisect_left(a, x, lo=0, hi=None)
    其目的在于查找该数值将会插入的位置并返回，而不会插入。如果x存在在a中则返回x左边的位置
    a=[1,3,3,3,6,8,10,16,19,44]
    print(bisect.bisect_left(a,2)),1
    print(bisect.bisect_right(a,2)),1#看来right和left的区别，就当在a中已经存在的时候才有的变化了
    恰好，题目中里面就是有重复的
    print(bisect.bisect_left(a,3)),1
    print(bisect.bisect_right(a,3)),4
    相当于，假设我插入了，那么会插在什么位置
    bisect.insort_left(li, 3)
    这个是真正的插入    
    """
    lis = []
    for n in nums:
        pos = bisect.bisect_left(lis, n)#他的时间复杂度是O(longN)
        """
        因为要求是increasing，所以当nums里面有重复值时，只能够取一个。所以相当于把当前的与n重复的"替换"掉
        """
        if pos == len(lis):#意思就是说应该插在最后，那肯定就是说，当前n都比有序的lis中的元素大
            lis.append(n)
        else:
            lis[pos] = n
            """
            当前所存在的假如就是一个正常的升序lis。[5,9,16,22,56],如果遇到了n=55，意思是用[5,9,16,22,55]来
            替代lis并不会影响len。应为55是出现在lis后面的，可以用来替代56。因为我们要尽可能的找到tail最小的
            lis。因为这样才更有机会append。如果n=10.[5,9,10,22,56]，这个可以替换原来的lis。因为后面如果出现了
            可以append的，并不会因为你用10替换16而改变。还是那个原理，当len=3的时候，[5,9,10]比[5，9，16]有机会
            更长。
            lis中存的是当len(sub_lis)=1，2，3，4，5...n时，sub_lis[tail]最小的那一组，即使可能sub_lis中间有的地方
            被后面的代替了，不能满足lis中的jndex增加与其在nums中对应的index的增加所表现的一致。
            这种方法是找不到具体的序列的 ，只能够找到number
            """
    return len(lis)
nums=[4,7,7,10,7,8]
print(lengthOfLIS(nums))
print(dp_and_binary_search(nums))

