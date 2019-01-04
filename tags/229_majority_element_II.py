"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space."""
"""这里面涉及到一个算法，就是摩尔投票法，一排观众排排坐。假设我们
已经知道，有一个人的票是超过半数的，现在我们线性时间内知道是谁。
比如从头到尾扫描，用c来表示当前扫描的观众所投的票，fc表示扫描到现在超过半数的c的个数。
在这个过程中遇到与当前c不一样的fc就减去一张，相同的fc就加上一张，当fc变成0的时候，表示扫描至今，没有谁是超过一半的
所以前面的可以不看了，就是相当于从头开始了。c存当前位置观众所投的票"""
def mol_vote(nums):
    #假设nums中存在超过半数的int
    c=nums[0]
    fc=0
    i=0
    while(i<len(nums)):
        if nums[i]==c:
            fc+=1
        elif fc==0:
            c=nums[i]
        else:
            fc-=1
        i+=1
    return c#得到的c里面存的就是超过半数的int，因为最后，只有它没有被其他的int消除掉。超过半数就是超过：向下取整[n/2]
#如果想得到具体的数量，可以使用len的公式，也可以再次扫描一遍
"""如果是找出所有的大于:向下取整[n/3]的呢"""
def mol_vote(nums):
    #因为是寻找大于n/3的，所以我们 可以 确定nums'中最多存在两种这样的int
    """当数组中元素和c1或者c2相同，对应的fc1或者fc2加1；
如果fc1或fc2为0，将遍历到的该元素赋给c1或者c2；
否则c1和c2都减1。
最重要的一点是，在上述这个过程中，务必保证c1和c2是不相同的，当c1,c2，x都不同的时候
才能够消除"""
    if not nums: return []
    c1,c2,fc1,fc2=None,None,0,0
    for x in nums:
        if x==c1:
            fc1+=1
        elif x==c2:
            fc2+=1
        elif fc1==0:
            c1=x
            fc1+=1
        elif fc2==0:
            c2=x
            fc2+=1
        else:
            fc2-=1
            fc1-=1
    #return [x for x in [c1,c2] if x !=None]#得到的c里面存的就是超过半数的int，因为最后，只有它没有被其他的int消除掉。超过半数就是超过：向下取整[n/2]
    #到了这一步并不意味着，因为当遇到三个互不相同的组是，我们 才选择消掉
    #但是这种情况下呢？[1,1,1,1,1,1,2,2],很明显上述的结果是[1,2]，但是最终的correct应该是[1]。
    #因为再次扫描的验证过程是必不可少的
    count1,count2,ans=0,0,[]
    for x in nums:
        if c1==x:count1+=1
        if c2==x:count2+=1
    if count1>len(nums)//3:ans.append(c1)
    if count2>len(nums)//3:ans.append(c2)
    return ans


nums=[3,3,5,3,3,6,3,4,5,6,3,6]
print(mol_vote(nums))
