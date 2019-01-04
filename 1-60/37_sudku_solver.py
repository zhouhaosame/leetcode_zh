def brute_force_solveSudoku(board):
    ans = []
    def isValidSudoku(board):
        import collections
        temp = collections.Counter(sum(
            [[(i, item), (item, j), (i // 3, j // 3, item)] for i, row in enumerate(board) for j, item in enumerate(row)
             if
             item != '.'], [])).values()
        if not temp: return True  # 防止为空
        return 1 == max(temp)

    def collect_row_col_block(board, i, j):
        res = set()
        for x in range(9):
            res.add(board[i][x])
        for x in range(9):
            res.add(board[x][j])
        i, j = i - i % 3, j - j % 3
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                res.add(board[x][y])
        return res

    def generate_sudoku(board, j):
        import copy
        # 为了让递归能够pop，i,j可以采取一直往上加的方式
        if j == 81:
            print(j)
            if isValidSudoku(board):
                ans.append(copy.deepcopy(board))
        else:
            if board[j // 9][j % 9] == '.':
                # temp = collect_row_col_block(board, j // 9, j % 9)
                # s = set(list(str(123456789)))
                # if temp & s == s:return False
                for item in '123456789':
                    # if item not in temp:
                    board[j // 9][j % 9] = item
                    if isValidSudoku(board):
                        generate_sudoku(board, j + 1)
                    board[j // 9][j % 9] = '.'
            else:
                if isValidSudoku(board):
                    generate_sudoku(board, j + 1)
                else:
                    return
    generate_sudoku(board, 0)
    return ans
#这是暴力法（+回溯）,非常浪费时间

def solveSudoku(board):
    """这种方法更加的精简，超过25%"""
    ans = []
    def collect_row_col_block(board, i, j):
        #这个函数的含义是，找到i，j处可以是的那些值
        res = set()
        for x in range(9):
            res.add(board[i][x])
        for x in range(9):
            res.add(board[x][j])
        i, j = i - i % 3, j - j % 3
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                res.add(board[x][y])
        return res

    def generate_sudoku(board, j):
        import copy
        # 为了让递归能够pop，i,j可以采取一直往上加的方式
        if j == 81:
            ans.append(copy.deepcopy(board))#！！！！！！！！！以后这里，不管什么都是深层拷贝！！
        else:
            if board[j // 9][j % 9] == '.':
                temp = collect_row_col_block(board, j // 9, j % 9)
                s = set(list(str(123456789)))
                if temp & s == s:
                    return
                for item in s-temp:#不需要判断是否有效（九宫格）,因为temp中的都是有效的
                    board[j // 9][j % 9] = item
                    generate_sudoku(board, j + 1)
                    board[j // 9][j % 9] = '.'#！！！！一定要回复到原来的状态！！！！！删掉就是错的
            else:
                generate_sudoku(board, j + 1)#不需要判断，因为替换“.”的都是根据已有的的数字替换的
    generate_sudoku(board, 0)
    #return ans
    #在leetcode中，不让返回东西，所以只能对board进行修改
    #board=ans[0],这样赋值是不行的，这样相当远重新生成一个board
    #要在board原来的地址中进行修改，必须要一个一个修改
    for i in range(9):
        for j in range(9):
            board[i][j]=ans[0][i][j]
    return board

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(solveSudoku(board))
