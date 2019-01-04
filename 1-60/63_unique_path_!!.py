def uniquePathWithObstacles(obstacleGrid):
    if not obstacleGrid:return 0
    dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    for i in range(0,len(obstacleGrid)):#这里要注意，当出现1的时候，由于只能够往下或者往右，所以障碍物后面的或者下面的
        #都是0了
        if obstacleGrid[i][0]==1:
            break
        else:
            dp[i][0]=1
    for j in range(0,len(obstacleGrid[0])):
        if obstacleGrid[0][j]==1:
            break
        else:
            dp[0][j]=1
    for i in range(1,len(dp)):
        for j in range(1,len(dp[i])):
            if obstacleGrid[i][j]==1:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]
obstacles=[
  [1]
]
print(uniquePathWithObstacles(obstacles))