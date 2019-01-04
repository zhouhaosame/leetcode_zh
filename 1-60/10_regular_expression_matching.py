import numpy as np
def isMatch(s,p):
    pl,sl,i,j,flag,j_index=len(p),len(s),0,0,False,0
   #if pl<sl:return False
    while(i < sl and j < pl and j_index<pl):
        if not flag:j=j_index
        if s[i]==p[j] or p[j]==".":
            i+=1
            j+=1
            flag=True
        elif j+1<pl and p[j+1]=="*":
            j+=2#这里是说明*表示前面char 0个的意思
            flag=True
        elif p[j]=="*":
            if flag==True:
                if s[i]==p[j-1] or p[j-1]==".":#因为一个*可能代表多个它前面的char，所以要消消乐
                    if i==sl-1:return True
                    if j==pl-1:return False#这里是用来判断这个比较是否是最后一个的
                    temp=s[i]
                    while (i + 1 < sl):
                        if s[i+1]==temp:i+=1
                        else:
                            i+=1
                            break

                    while (j + 1 < pl):
                        if p[j+1]==temp or p[j+1]=="*":j+=1
                        else:
                            j+=1
                            break
                elif (p[j-1]=="*" and s[i-1]==s[i]):
                    i+=1
                    j+=1
                else:
                    i=0
                    j_index+=1
                    flag=False
            else:
                j_index+=1
        else:
            i=0
            j_index+=1
            flag=False
    return True if flag and i==sl else False


def dynamic_program(s,p):
    dp=[[0]*(len(s)+1) for _ in range(len(p)+1)]
    if not s or not p or p.startswith("*") or (len(p)-p.count("*")>len(s)):
        return False
    dp[0][0]=1
    for i in range(1,len(p)+1):
        for j in range(1,len(s)+1):
            if p[i-1]=="." or p[i-1]==s[j-1]:
                dp[i][j]=dp[i-1][j-1]
            elif p[i-1]=="*":
                dp[i][j]=dp[i-1][j] or (dp[i][j-1] and s[j-1]==s[j-2])
                #因为开始时最前面的不为*，所以可以j-2
    return dp[i][j]==1
s="aab"
p="c*a*b"
#print(isMatch(s,p))
print(dynamic_program(s,p))
