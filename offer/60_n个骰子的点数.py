"""
小易参加了一个骰子游戏,这个游戏需要同时投掷n个骰子,每个骰子都是一个印有数字1~6的均匀正方体。
小易同时投掷出这n个骰子,如果这n个骰子向上面的数字之和大于等于x,小易就会获得游戏奖励。
小易想让你帮他算算他获得奖励的概率有多大。
"""
def f(n, x):
    if n <= 0 or x > 6 * n:
        return 0
    max_values = 6
    flag = 0
    SumFre_values = [[0] * (max_values * n + 2), [0] * (max_values * n + 2)]
    # 0位置保存当前掷骰子m-1次的最小和在哪里，n+1位置保存当前投掷次数m-1次的最大可能和在哪里
    # 初始化，第一次时候
    for i in range(1, max_values+1):
        SumFre_values[1 - flag][i] = 1
    SumFre_values[1-flag][0],SumFre_values[1-flag][-1]=1,max_values
    for i in range(2, n + 1):
        for j in range(i, i * max_values + 1):
            SumFre_values[flag][j] = sum([SumFre_values[1 - flag][j - m] for m in range(1, max_values+1) if j - m >= SumFre_values[1-flag][0] \
                                       and j - m <= SumFre_values[1 - flag][-1]])
        SumFre_values[flag][0], SumFre_values[flag][-1] = i, i * max_values
        flag = 1 - flag
    return sum(SumFre_values[1 - flag][x:-1]) / sum(SumFre_values[1-flag][n:-1])

print(f(3,9))

