def print_matrix(matrix):
    nums = []
    bound = [len(matrix[0]) - 1, len(matrix) - 1, 0, 0]
    point = [0, -1]
    while (bound[0] >= bound[2] and bound[1] >= bound[3]):
        for i in range(1, -1, -1):
            while (point[i] + 1) <= bound[i ^ 1] and (bound[0] >= bound[2] and bound[1] >= bound[3]):#
                #后面的那个and是专门用来处理单行或者单列的
                point[i] = point[i] + 1
                nums.append(matrix[point[0]][point[1]])
        bound[3]+= 1
        bound[0]-=1
        for i in range(1, -1, -1):
            while (point[i] - 1) >= bound[(i ^ 1) + 2] and (bound[0] >= bound[2] and bound[1] >= bound[3]):
                point[i] = point[i] - 1
                nums.append(matrix[point[0]][point[1]])
        bound[1]-=1
        bound[2]+=1
    return nums
def spiralOrder(matrix):#这是人家的,简单明了，很容易理解
    if not matrix or not matrix[0]:
        return []
    ans = []
    row, col = len(matrix), len(matrix[0])
    row_up, row_bottom, col_left, col_right = 0, row - 1, 0, col - 1
    while row_up <row_bottom and col_left < col_right:
        """为什么不是等于号呢？因为在最里面的时候，只有四种可能，一种是正方形，一种是一行，一种是一列，一种是只有一个数字
        如果是正方形的，正好所有的都打印出来了，
        假设是大于等于的且只有一行的情况。
        比如[[1,2,3]],ans增加的是1,2，然后[],然后[3,2]，然后[]。很明显这是错误的。所以那三种情况要单独考虑"""
        ans.extend([matrix[row_up][j] for j in range(col_left, col_right)])
        ans.extend([matrix[j][col_right] for j in range(row_up, row_bottom)])
        ans.extend([matrix[row_bottom][j] for j in range(col_right, col_left, -1)])
        ans.extend([matrix[j][col_left] for j in range(row_bottom, row_up, -1)])
        row_up, row_bottom, col_left, col_right=row_up+1, row_bottom-1, col_left+1, col_right-1
    if  row_up ==row_bottom:#表示一行
        ans.extend([matrix[row_up][j] for j in range(col_left,col_right+1)])
    elif col_left==col_right:#表示一列
        ans.extend([matrix[j][col_left] for j in range(row_up,row_bottom+1)])
    return ans

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(print_matrix(nums))
print(spiralOrder(nums))