class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = 1
        # for i in range(1, len(dp)):
        #     if p[i - 1] == "*":
        #         dp[i][0] = 1
        #     else:
        #         break
        for j in range(len(dp)):
            for i in range(len(dp[0])):
                if p[j - 1] in [s[i - 1], "."]:
                    dp[j][i] = dp[j - 1][i - 1]
                elif p[j - 1] == "*":
                    dp[j][i] = j - 2 >= 0 and dp[j - 2][i] or dp[j - 1][i] or (dp[j - 1][i - 1] or dp[j][i - 1]) and (
                                i - 2 >= 0 and s[i - 2] == s[i - 1] or j - 2 >= 0 and p[j - 2] == ".")
        return bool(dp[-1][-1])
test1=Solution()
print(test1.isMatch("a","c*a"))



