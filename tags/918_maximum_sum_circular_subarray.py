def first_kadanes_method(arr):
    """kadanes是专门用来求一个array中的最大maximum sum of subarray的
    方法
    这里当然是改进的啦，kadanes的算法时间复杂度是o(N)，如果将circul array
    划分成N分的话，那么时间复杂度就是O（N^2）了。
    题目的意思是：在array中找到一个指针，然后将arrat分成两段
    这两段可以将第len（arr）-1和0连接，构成一个新的array
    其实这种情况下，一共有两种可能，一个是指针在最后，那么就是
    一个interval，另一个是指针在中间，将原来的array分成了两个interval
    这个可以分开考虑"""
    #当一个interval的时候，就是普通的kadanes方法
    if not arr:return 0
    ans=left_sum=float("-inf")#left表示已i位置结尾的，0：i段的和的最大值,这里一定不能够使用0去赋值，因为可能数组中都是负的
    for x in arr:
        left_sum=x+max(left_sum,0)
        ans=max(ans,left_sum)
    #当两个interva的时候
    """两个interval一定是这种情况，第一个inter是以0 所以开始的
    第二个interval是以len(array)-1结束的。那么就可以这样去找最大值
    ：指针i后面的一段的sum，与其前面一段的最大的sum的和中的最大值
    （遍历所有的i）得到的就是两个interval中的最大值"""
    l=len(arr)
    left_sum=[0]*l
    left_sum[0]=arr[0]
    for i in range(1,l):
        left_sum[i]=left_sum[i-1]+arr[i]
    max_left_sum=[0]*l
    max_left_sum[0]=arr[0]
    #max_left_sum中存的是以0位置开始的到当前i之间的最大的连续
    #subarray的和
    for i in range(1,l):
        max_left_sum[i]=max(max_left_sum[i-1],left_sum[i])
    #for i in range(l-1):
     #   ans=max(ans,sum(arr[i+1:])+max_left_sum[i])
    #如果使用这种，结果是对的，但是有了很多的重复计算。TEL
    right_sum=0
    for i in range(l-1,0,-1):
        right_sum=right_sum+arr[i]
        ans=max(ans,right_sum+max_left_sum[i-1])
    return ans

def 改良_kadanes(A):
    """先推理，kadanes(A)的作用是找循环array的最大sum，sum(A)=kadanes(A)+剩下的连续subarray的sum。如果ladanes
    是最大的，那么剩下的连续subarray的sum是最小的连续subarray了。证明：如果不是，说明有一个连续的subarray更小
    因为总的sum是不变的，所以会找到一个更大的subarray，这与假设不符合。
    如果B=-A,且kadanes(A)=a1,a2...ai,aj,aj+1,...alen-1（等价于sum(A)-(ai+1,...aj-1)）。那么kadanes(B)=-(ai+1,...aj-1)
    所以kadanes(A)=sum(A)+kadanes(B)
    """
    def kadane(gen):
        # Maximum non-empty subarray sum
        ans = cur = None
        for x in gen:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        return ans

    S = sum(A)
    ans1 = kadane(iter(A))
    ans2 = S + kadane(-A[i] for i in range(1, len(A)))
    ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
    """
    ans1表示subarray没有使用循环特性找到的值
    
    """
    return max(ans1, ans2, ans3)

arr=[-3,-2,-1]
print(first_kadanes_method(arr))


