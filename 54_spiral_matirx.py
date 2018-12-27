def spiralMatrix(matrix):
    #很明显，这个可以用递归
    ans=[]
    def myPrint(row1,row2,col1,col2):
        if row1>row2 or col1>col2:
            return
        if row1==row2:
            ans.append(matrix[row1][col1:col2+1])
            return
        elif col1==col2:
            ans.append([x[col1] for x in matrix[row1:row2+1]])
            return
        if row1==row2-1:
            ans.append(matrix[row1][col1:col2+1])
            ans.append(matrix[row2][col1:col2+1][::-1])
            return
        elif col1==col2-1:
            ans.append(matrix[row1][col1])
            ans.append([x[col2] for x in matrix[row1:row2+1]])
            ans.append([x[col1] for x in matrix[row1+1:row2+1]][::-1])
            return
            """未完待续"""
            """使用递归地方式，因为出口有点多，而且还比较难写，因为稍微不注意就会 beyond bounds"""
        else:
            ans.append(matrix[row1][col1:col2+1])
            ans.append([x[col2] for x in matrix[row1+1:row2+1]])
            ans.append(matrix[row2][col1:col2][::-1])
            ans.append([x[col1] for x in matrix[row1+1:row2]][::-1])
            myPrint(row1+1,row2-1,col1+1,col2-1)
    myPrint(0,len(matrix)-1,0,len(matrix[0])-1)
    a=[]
    print(ans)
    for item in ans:
        if type(item)==type(0):
            a.append(item)
        else:
            for i in range(len(item)):
                a.append(item[i])
    return a
Input=[
[2,5],[8,4],[0,1]
]
print(spiralMatrix(Input))
#结果正确，超过16%.。。注意了，别看是个递归，可是，时间复杂度是O(N),其实就是对每个元素操作了一次
