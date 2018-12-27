def rotate(matrix):
    #总的想法是现将矩阵进行转置，然后将转置后的每一行都进行反转，得到的就是旋转90度的
    #没必要用数学的方式去计算ij旋转后的位置，直接找个例子旋转之后就能够发现了这个规律
    #！！！！in place swap不一定就是用那种交换方式，使用^
    #直接x,y=y,x这样就直接交换啦！！！
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    #这个就是反转之后的，接下来进行row的翻转
    for i in range(len(matrix)):
        matrix[i]=matrix[i][::-1]
    print(matrix)
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
