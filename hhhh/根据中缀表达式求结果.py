# 这个是很经典的，先用后缀表达式表示，然后再求结果
#注意了，这里说   字符串中的有效字符包括[‘0’-‘9’]，是指单个字母，实际上是有两位数的，还要读取两位数
#有正负号的，简直是rg
while True:
    try:
        str1 = input()
        flag=0#加上flag是为了输入多位数
        # 定义优先级级别,加上#可以少去判断是否越界
        dct = {"#": 0, "+": 1, '-': 1, '*': 2, "/": 2}#这里不需要将括号也赋值，因为要是赋值的话，
        #括号的优先级应该是最大的，那么就要出战了
        left_bracket = ['{', '(', '[']
        right_bracket = ['}', ')', ']']
        sign_list = ['+', '-', '*', '/']
        pre_char="#"
        def convert_post(str1,flag):#这里要不然将flag变成全局变量 也就是flag=[0],要不然就要讲flag=0作为参数输入
            res = []
            sign = ["#"]#这样就不需要判断是否越界了
            for index in range(len(str1)):
                if "0" <= str1[index] <= "9":
                    if flag==1:#如果刚刚也输入了number，那么应该是连在一起的
                        res[-1]=res[-1]+str1[index]
                    else:
                        res.append(str1[index])
                    flag=1
                elif str1[index] in sign_list:
                    if str1[index]=="-" and (index>0 and (str1[index-1] in left_bracket or str1[index-1] in sign_list)\
                                             or index==0 ):
                        res.append(str1[index])
                        flag=1#这里就是判断那个-是不是表示负号，注意当前面是加减乘除或者左括号的时候，才是，右括号的时候不是
                        continue
                    while (sign[-1] in dct and dct[str1[index]] <= dct[sign[-1]]):
                        res.append(sign.pop())
                    sign.append(str1[index])
                    flag=0
                elif str1[index] in left_bracket:
                    sign.append(str1[index])
                    flag=0
                elif str1[index] in right_bracket:
                    index = [k for k in range(len(sign)) if sign[k] == left_bracket[right_bracket.index(str1[index])]][-1]
                    #找到最左边的
                    res.extend(sign[index:][1:][::-1])
                    sign=sign[:index]#一定要从sign中删除已经出栈的，这里还是完全用栈吧，因为这样不会忘记写这样
                    flag=0
            res.extend(sign[1:][::-1])
            return res
        post_dix = convert_post(str1,flag)
        def using_post_dix(post_dix):
            res = []
            c = 0
            for item in post_dix:
                if item not in sign_list:
                    res.append(int(item))
                else:
                    b = res.pop()
                    a = res.pop()
                    """
                    c = [a + b, a-b, a * b, a / b][sign_list.index(item)]
                    原来这里是这样来计算c的，以为这样只用了一行代码，其实是非常shab 的事情
                    1、增加了运算量
                    2、当b为0的时候，就出错了
                    哎
                    """
                    if item == '+':
                        c = a + b
                    elif item == '-':
                        c = a - b
                    elif item == '*':
                        c = a * b
                    elif item == '/':
                        c = a / b
                    res.append(c)
            return c
        print(using_post_dix(post_dix))
    except:
        break