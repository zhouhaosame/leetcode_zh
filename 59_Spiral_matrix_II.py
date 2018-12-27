def generatrMatrix(n):
    """超过99%"""
    if n==0:
        return []
    sj=[1,0,-1,0]
    si=[0,1,0,-1]#这里就是通过si/sj[b]来控制指针的方向
    visited,matrix=[[0]*n for _ in range(n)],[[0]*n for _ in range(n)]
    count,count_limit,i,j,b=1,n*n,0,0,0
    while(count<=count_limit):
        while(i<n and j<n and visited[i][j]!=1):
            matrix[i][j]=count
            count+=1
            visited[i][j] = 1
            i=i+si[b]
            j=j+sj[b]
        i=i-si[b]#这时的i或者j已经是超过范围的了。所以要退回来
        j=j-sj[b]
        b=(b+1)%4
        i=i+si[b]
        j=j+sj[b]#退回来之后还需要继续移动，要不然就是死循环了
    return matrix
n=3
print(generatrMatrix(n))
