#1、brute_force
def isValidSudoku(board):
    if not board:return False
    import copy
    #determine row
    num_dict_origin={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    for row in board:
        num_dict=copy.deepcopy(num_dict_origin)
        for item in row:
            if item in num_dict:
                num_dict[item]+=1
                if num_dict[item]<2:
                    continue
                else:return False
            else:
                continue
    #determine columns
    for index,value in enumerate(board[0]):
        num_dict = copy.deepcopy(num_dict_origin)
        i=0
        while(i<9):
            if board[i][index] in num_dict:
                num_dict[board[i][index]]+=1
                if num_dict[board[i][index]]<2:
                    i += 1
                    continue
                else:
                    return False
            else:
                i += 1
                continue
    i,j=0,0
    while(i<=6 and j<=6):
        num_dict = copy.deepcopy(num_dict_origin)
        for x in range(i,i+3):
            for y in range(j,j+3):
                if board[x][y] in num_dict:
                    num_dict[board[x][y]] +=1
                    if num_dict[board[x][y]]<2:
                        continue
                    else:
                        return False
        if j<6:
            j=y+1
            i=x-2
        else:
            j=0
            i=x+1
    return True

def using_any(board):
    seen = set()#set() 函数创建一个无序不重复元素集
    #any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
    #any=是否存在true
    #all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
    #all=是否都为true
    return not any(x in seen or seen.add(x)
                   #add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
                   #不管执行不执行，set返回的都是None，所以这里只要根据x in seen来判断就好了，
                   #seen.add()只是一个操作
                   for i, row in enumerate(board)
                   for j, c in enumerate(row)
                   if c != '.'
                   for x in ((c, i), (j, c), (i //3, j // 3, c)))
    #类似这样的，第一行都是操作，接下来都是一些循环或者判断
"""对于每个c来说，它都会被判断三次，分别是行，列，快，只要将这个c加上。。index..就能够表示这个
c在哪出现过了，和加入字典的考虑是一样的。(c，row_index)表示在哪行出现过这个c，（col_index）表示在哪列出现
了这个，最后的则是块，其中，前面的两个是  用块的左上角坐标来代表块，厉害了"""

def using_len(board):
    seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))
"""sum(iterable[, start])，其中iterable为可迭代对象，可以是list、tuple或者dictionary等。
不要弄混了，这里的可迭代对象是元祖，元祖元素是列表。start是[]
sum函数最后的值 = 可迭代对象里面的数相加的值 + start的值，其中start可以不写，默认为0。
"""
def test(board):
    print([[(c, i), (j, c), (i // 3, j // 3, c)]
    for i, row in enumerate(board)
        for j, c in enumerate(row)
            if c != '.'])
    print(sum(([1,2],[3,4]),[0]))#[0, 1, 2, 3, 4]，合并成一个列表
    #print(sum(({1:2},{2:3} ), {}))  # 错误的，不支持字典
    #如果迭代的是int，直接就是相加了，如果是列表，则是合并成一个列表
    #print(sum(('c','b'), 'n'))  # 错误的，目前来说，只能用于列表和int
def using_counter(board):
    import collections
    return 1 == max(collections.Counter(
        x
        for i, row in enumerate(board)
        for j, c in enumerate(row)
        if c != '.'
        for x in ((c, i), (j, c), (i / 3, j / 3, c))).values())
# 实例化Counter对象，可接收任何hashable序列（元祖，列表，没有重复元素的集合），Counter对象可以像字典一样访问元素并返回出现的次数
def test_value():
    import collections
    print(collections.Counter((1,2,3,3)))
    print(collections.Counter((1, 2, 3, 3)).values())
    #Counter({3: 2, 1: 1, 2: 1})
    #dict_values([1, 1, 2])
    print(collections.Counter([1, 3, 3]))#Counter({3: 2, 1: 1})
    print({1,3,3})#{1,3}
    print(collections.Counter({1, 3, 3}))#Counter({1: 1, 3: 1}),注意，这里明显显示3出现一次，因为set，也就是{},里面不能有重复元素

board=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board))
print(using_any(board))
print(using_len(board))
print(using_counter(board))
test_value()

def test_set():
    seen={1,2}
    seen.add(2)
    print(seen)
    seen.add(3)
    print(seen)
    #{1, 2}
    #{1, 2, 3}
    #这说明，如果是集合的类型，往里面添加重复元素，是不能够添加进去的，但是不管能不能添加进去，返回的都是false

test_set()