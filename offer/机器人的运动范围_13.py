def range_of_motion_of_robert(board):
    if not board:
        return None
    row_len, col_len, num, k = len(board), len(board), set(), 13
    """可以用ans存储所有的路径，然后将里面的格子并集，就得到了所有的范围"""
    def check_point(row, col):
        sum_row, sum_col = 0, 0
        while (row):
            sum_row += row % 10
            row = row // 10
        while (col):
            sum_col += col % 10
            col = col // 10
        return sum_row + sum_col

    def backtracking(i, j, visited):
        if not check_point(i, j) < k:
            return
        else:
            #num=num | set([(i, j)])
            """这里很重要的啊，因为，虽然感觉num好像会一直增加，但是其实回溯的时候，num也会回到上一阶段，为什么呢？？？？？
            因为
            num重新赋值了啊，num有了一个新的地址，老的num地址被存储在栈中，然后返回上一级会回到那个老的地址的，这样就造成了
            num的"回溯"。
            正确的方法是直接在地址里改变内容
            
            原来我定义了一个count计数器，没进入一次就count++，这样是错误的，因为这个思路是当前i,j是(2,2),然后延伸出来(2,3)
            ,(2,4)这一条路，visited中是(2,2),(2,3),(2,4)。然后，count=count+2.然后我回溯，这时候，visited中只有(2,2)了，然后
            新的路径可能会和上一条路径有重复的格子。所以count会多很多
            """
            num.add((i, j))
            for (a, b) in [(a, b) for (a, b) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if
                           0 <= a < row_len and 0 <= b < col_len and (a, b) not in visited]:
                visited.add((i, j))#！！！！！！！！！！！和平常不一样
                backtracking(a, b, visited)##！！！！！！！！！！！！
                """这里又有一个小技巧，原来的是backtracking(a, b, visited| set([(i,j)]),相当于将所有的路径都求出来了，
                不是相当于2的m*n次方条路径，因为比如九宫格，周围都不是路径的一份子，则中间的不可能是是路径的一份子。
                这样很浪费时间，非常浪费。
                但是将每次迭代遍历过的都保留，这就相当于给格子染上黑色。最终只要是有路径能够到达的地方，都会被染成黑色"""
    backtracking(0, 0, set())
    return len(num)


# if flag==0:#如果flag是0的话，表示已经到头了，退出就可以了
#    return
n=100
board = [[0] * n for _ in range(0, n)]
print(board)
print(range_of_motion_of_robert(board))
