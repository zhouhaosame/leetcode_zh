"""动态规划,一般的动态规划就是将一个大问题分成几个小问题，小问题和大问题的解法是相同的。然后根据小问题的
解可以得到大问题的解。一般是求最大最小值。而且一定是会填表的。
这里只是一个list。0index存储的是n的长度，list一共n+1这么长。然后从前往后填表。
时间复杂度是n的平方。对于长度为n，在i处分成两段，fi和fn-i的乘积就是最大--不对。表中存的是
剪之后的最大的。因为在i处剪了，所以可能i里面没有剪，所以要 考虑多种情况。剪*不剪，剪*剪等四种情况"""
def dynamic(n):
    list_maxinum=[0]*(n+1)
    list_maxinum[0]=n
    """这里4后面的存的是划分之后的最大乘积，1,2，3存的是划分和不划分的最大乘积。
    为什么是4之后呢？
    假设n，我们只要证明，存在两个数相加是n然后成乘积大于n就好啦。
    比如(n/2)*(n-n/2)-n是否大于等于0，可以证明当n大于等于4使成立。所以四之后是最大值(只有划分的)。之前
    是n本身"""

    if n<2:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    list_maxinum[1]=1
    list_maxinum[2]=2
    list_maxinum[3]=3
    for x in range(2,n+1):
        for i in range(1,x//2+1):
            #list_maxinum[x]=max([list_maxinum[x],list_maxinum[i]*list_maxinum[x-i],
            #                    i*list_maxinum[x-i],list_maxinum[i]*(x-i),i*(x-i)])
            list_maxinum[x]=max([list_maxinum[x],list_maxinum[i]*list_maxinum[x-i]])
    return list_maxinum[n]


"""贪心算法是需要证明的。就是说，当n>=5的时候，可以分成3*n-3，然后n-3再分成3和n-6，直到最后剩下四（可以分成
2*2，虽然不忿也是4，但是要求是分的。就是这样，每次划掉三个
其实这个是需要证明的。
你想为什么在动态规划的时候，2,3都是单独的本身，而不是需要划分的呢？？
比如我们从n中划分除了>=5的一条线段，很明显，将这个5再次划分成2*3，结果是更大的。所以要一直的划掉3个的长度）"""
def greedy(n):
    count=0
    if n<=1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return 4
    while(n>4):
        n=n-3
        count+=1
    return 3**count*n
n=[2,3,4,5,6,7,8,9,10,12,13,14,15,16,100]
nums1=[]
nums2=[]
for x in n:
    nums1.append(dynamic(x))
    nums2.append(greedy(x))
print(nums1)
print(nums2)
