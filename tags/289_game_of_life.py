"""According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.
这个题目按理说应该是很简单的，难的是，in_place解决他，普通方法就是用m*n空间的矩阵去更新他
这个题目和对年龄进行排序有点相同点。可以枚举所有的可能
live+<2 live=die
live+2/3 live=live
live+>3 live=die
die+3 live=live
考虑 in place，对于原来的矩阵，用3表示第一种情况，4表示第二种情况，5表示第三种情况，而且3,4,5意味着上一轮是live，
用6表示第四种情况
这样的话就简单了"""


def gameoflife(board):
    if not board:
        return False
    l_row, l_col = len(board), len(board[0])
    for index_row, row in enumerate(board):
        for index_col, col in enumerate(row):
            live, die = 0, 0
            for (a, b) in [(a, b) for (a, b) in
                           [(index_row - 1, index_col - 1), (index_row - 1, index_col), (index_row - 1, index_col + 1)
                               , (index_row, index_col - 1), (index_row, index_col + 1), (index_row + 1, index_col - 1)
                               , (index_row + 1, index_col), (index_row + 1, index_col + 1)]
                           if 0 <= a < l_row and 0 <= b < l_col]:
                if board[a][b] in [1, 3, 4, 5]:
                    live += 1
                else:
                    die += 1
            if board[index_row][index_col]==1:
                if live<2:
                    board[index_row][index_col]=3
                elif live==2 or live==3:
                    board[index_row][index_col]=4
                else:
                    board[index_row][index_col]=5
            elif live==3:
                board[index_row][index_col]=6

    for index_row, row in enumerate(board):
        for index_col, col in enumerate(row):
            if board[index_row][index_col] in [4,6]:
                board[index_row][index_col]=1
            else:
                board[index_row][index_col]=0


