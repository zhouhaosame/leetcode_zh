def f(nums):
    dp=[[0]*len(nums) for _ in range(0,2)]
    if not nums:
        return 0
    dp[0][0]=nums[0]
    dp[1][0]=0
    dp[0][1]=min(dp[0][0],dp[1][0])+nums[1]
    dp[1][1]=min(dp[0][0],0)
    for i in range(2,len(dp[0])):
        dp[0][i]=min(dp[0][i-1],dp[1][i-1])+nums[i]
        dp[1][i]=min(dp[0][i-1],dp[0][i-2])
    print(dp)
    return min(dp[0][-1],dp[1][-1])

print(f([3,5,1000,8,2]))