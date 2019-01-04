"""可以使用简单的math solution也就是使用。对于m，n,一共是向下移动m-1 steps，向右移动n-1 steps
（毕竟是从1,1位置开始的）。C（m-1+n-1）,(n-1)"""
def DP(m,n):
    aux = [[1 for x in range(n)] for x in range(m)]
    #上边和右边靠墙的都初始化为1，不要动了
    for i in range(1, m):
        for j in range(1, n):
            aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
    return aux[-1][-1]


def uniquepaths(m,n):
    """动态规划是正确的，但是出现TLE错误"""
    if m == 1 and n == 1: return 1
    result=[0]
    path=[]
    import copy
    def findpath(i,j,res):
        if i==m and j==n:
            path.append(copy.deepcopy(res))
            return True
        else:
            if i+1<=m and findpath(i+1,j,res+[(i+1,j)]):
                result[0]+=1
                #return True
                """这里是非常要注意的地方，一定不能加上return True，因为加上这个，相当于，我从i,j位置
                移动，i=i+1,然后有路，result+1，这时就没有再看j+1的情况，直接就返回True了，结果当然是错误的"""
            if j+1<=n and findpath(i,j+1,res+[(i,j+1)]):
                result[0]+=1
                #return True
            #最后也咩有必要加上return，因为相当于返回None了
    findpath(1,1,[])
    return result[0],path
"""这样，连路径都知道啦！！"""
m=7
n=3
print(uniquepaths(m,n))
print(DP(m,n))
