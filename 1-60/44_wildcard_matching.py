def isMatching(s,p):
    l = len(s)
    if len(p) - p.count('*') > l:#这个不是1是len(s)=l
        return False
    dp = [True] + [False] * l
    for letter in p:
        new_dp = [dp[0] and letter == '*']
        if letter == '*':
            for j in range(l):
                new_dp.append(new_dp[-1] or dp[j + 1])
        elif letter == '?':
            new_dp += dp[:l]
        else:
            new_dp += [dp[j] and s[j] == letter for j in range(l)]
        dp = new_dp
    return dp[-1]

def dp_1(s,p):
    #设计一个表格dp[i,j]用来存储s[:i+1]和p[:j+1]是否能够匹配
    dp=[[0]*(len(s)+1) for i in range(len(p)+1)]#初始化一个dp二维列表
    dp[0][0]=1#初始状态,i=0,j=0行是存储的最初状态，是直接赋值的，所以可以一行一行的从左往右计算
    #因为dp是从1,1才对应到p，s中的，所以在p中的i位置，对应dp中的i+1行
    #判断为空
    if not p and not s: return True
    if not p and s:return False
    if not s and p and len(p)==p.count("*"): return True
    if len(p)-p.count("*")>len(s):return False
    for i in range(0,len(p)):
        if p[i]=="*":
            dp[i+1][0]=1
        else:
            break
    for i in range(1,len(p)+1):
        for j in range(1,len(s)+1):
            if p[i - 1] == "*":
                if dp[i - 1][j] or dp[i][j - 1]:
                    dp[i][j] = 1
            elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
  # 用while千万不要忘记归0了，用for更好，自动加+1，！！！！是归1啊，不是归0..
        # 这里还是出现了问题，最后出循环的时候，j=1了，还是用for吧，多省事
    return True if dp[i][j]==1 else False
"""自己写的花费了1212ms，33%"""
def dp_2():
    return

def double_pointer(s,p):
    i,j,pi,sj=0,0,-1,-1
    if len(p) - p.count("*") > len(s): return False
    while(j<len(s)):
        if i<len(p) and (s[j]==p[i] or p[i]=='?'):
            i+=1
            j+=1
        elif i<len(p) and p[i]=="*":#开始、中间是一串*的可能也已经被包括了
            pi=i
            i+=1
            sj=j#匹配的是i，j，当p[i]==*时，i++，j不变，就相当于看了*表示空的选择，那么sj表示的就是substring的最后一个位置的下一个
        elif pi>-1:#s[j]!=p[i]
            sj=sj+1
            j=sj#!!!!!!!!!这里要十分注意，sj表示最后一个的下一个，sj加入subtring后，肯定sj=sj+1，这时候
            #sj就是我们要和新的i标胶的位置，所以j=sj
            i=pi+1#状态指针不会超过i,j的
        else:
            return False
    while(i<len(p) and p[i]=="*"):#防止最后一连串是*
        i+=1
    return i==len(p)#这里是用p匹配s，当退出第一个while循环，j要么return，要么=len（s），如果i到头了，那不就是
    #意味着匹配成功了啊

def divide_str(s,p):
    """这种是错误的方式，因为最后即使都是在s中，只能说明p存在于s中，并不能说明p和s完全匹配，比如aa和a"""
    strs=list(filter(None,p.split("*")))
    #filter第一个参数是None的时候，返回第二个参数中非空的值。
    i=0
    for str in strs:
        if i <len(s):
            index="".join(s[i:len(s)]).find(str)
            if index==-1:
                return False
            i=index+len(str)
        else:
            return False
    return True


s="aa"
p="a"
#print(isMatching(s,p))
#print(dp_1(s,p))
#print(double_pointer(s,p))
print(divide_str(s,p))
#print(com(s,p))