# 最长回文串，一共有两种，一种是动态规划，一种是马拉车算法
def dp_f(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    max_n = 0
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
    for j in range(2, len(s)):
        for distance in range(len(s) - j):
            dp[distance][j + distance] = dp[distance + 1][j + distance - 1] and s[distance] == s[j + distance]
            max_n = max(max_n, j+1) if dp[distance][j+distance] else max_n
    print(max_n)
while True:
    try:
        str1 = input()
        dp_f(str1)
    except:
        break




