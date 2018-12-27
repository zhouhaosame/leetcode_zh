import numpy
import string
def according_values_get_key():
    dct={"a":1,"b":2,"c":1,"d":4,"g":1,"yy":2}
    #python3中 keys() 方法返回一个迭代器，可以使用 list() 来转换为列表
    #print(list(dct.keys())[list(dct.values()).index()])
    print(dct)
    print(sorted(dct.items(),key=lambda x:x[1]))
def str_to_int():
    str="34"
    print(str[0:6])
def puanduan():
    dct,l,str1,l_str,dct_str={},[],"",[""],{"":""}
    if not dct:print("dct为空")
    if not l:print("列表为空")
    if not str1:print("字符串为空")
    if not l_str:print("只包含空字符串的列表")
    if not dct_str:print("字典-只有空字符串为空")
def ss():
    s=[1,2,3,4,5,6]
    s1=[[1,2],[2,3],[1,2]]
    dic={}
    list=dic.fromkeys(s1).keys()
    s=list(set(s))
    print(list)
def 列表加列表():
    s=[[1,2],[3,4],[5,6]]
    k=[[1,3],[9,8]]
    print(s+k)
    s=[1,2,3]
    k=[4,5]
    k=4
    print(s+k)
def 函数里面的函数():
    result=[]
    def add(s,result):
        result.append(s)
    add("ab",result)
    print(result)#["ab"]，很明显虽然result没有返回，但是因为result是（函数里面的函数中的）全局变量，所以可以直接修改
    #或者这么理解，先声明result，有一个地址了，然后将这个地址传入。在那里已经进行了修改。和C++中的传入指针变量的操作差不

class ListNode:
    def __init__(self,data):
        self.val=data
        self.next=None
def creat_node():
    node=ListNode(2)
    node=node.next
    if node:print("not None")
    else:print("None")
def test_heap():
    import heapq
    heap=[]
    heapq.heappush(heap,10)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    heapq.heappush(heap, -9)
    #每次只能插入一个
    x=[1,2,3,4,5]
    heapq.heapify(x)
    #将列表放入heap中
    [heapq.heappush(heap, i) for i in range(1,100)]
    print(heapq.nsmallest(len(heap),heap))
def for循环中的间隔问题():
    for i in range(0,1,2):
        print(i)#0
    for i in range(0,2,2):
        print(i)#0
    for i in range(0,3,2):
        print(i)#0,2
def 关于is的用法():
    print(True is True)
    print(False is False)
    print(False is True)
    #True，True，False
    s="123"
    print(s[0:2])
def 关于函数的嵌套问题():
    x = y = z = 2
    a=[1,2,3]
    def test1():
        def test(i,j):
            a[i]=a[i]+a[j]
            a[j]=a[i]-a[j]
            a[i]=a[i]-a[j]
            """很明显，普通的变量没有全局变量的意思，但是列表明显是有的，那么列表中的元素会改变吗
            证明过了，列表中的元素也是会改变的
            """
        test(0,1)
    test1()
    print(x)
    print(a)
def 关于复制原始常量():
    x=8
    y=x
    y+=2
    print(x)#8
    print(y)#10
    x={2:0,3:0}
    y=x
    y[2]+=1
    y[3]=y[3]+1
    print(y)
    print(x)
    d1 = {'k1': [1, 2, 3, 4, 5]}
    t1 = d1['k1']
    t1[0] = 9
    print(d1['k1'])  # [9, 2, 3, 4, 5]
    #
    d2 = {'k1': 'v1'}
    t2 = d2['k1']
    print(t2)  # v1
    t2 = 'v2'
    print(d2)  # {'k1': 'v1'}
    #
    d3 = {'k1': {'kk1': 'v1'}}
    t3 = d3['k1']
    print(t3)  # {'kk1': 'v1'}
    t3['kk1'] = 'v2'
    print(d3)  # {'k1': {'kk1': 'v2'}}
def 关于set_add():
    s=set([1,1,2,3])
    print(s)
    s1=s.add(1)
    print(s)
    print(s1)
    s2=s.add(6)
    print(s2)
    print(s)
def 汉字的长度用len():
    c="周豪，周豪 周"
    d="周hao\n"
    v="\t"
    print(len(c))#7
    print(len(d))#5
def 标点():
    symbol = ["！", "？", '｡', '＂', '＃', '＄', '％', '＆', '＇', '（', '）', '＊', '＋', '，', '－', '／', '：', '；',
              '＜', '＝', '＞', '＠', '［', '＼', '］', '＾', '＿', '｀', '｛', '｜', '｝', '～', '｟', '｠', '｢', '｣', '､', '、',
              '〃', '》', '「', '」', '『', '』', '【', '】', '〔', '〕', '〖', '〗', '〘', '〙', '〚', '〛', '〜', '〝', '〞', '〟',
              '〰', '〾', '〿', '–', '—', '‘', '‛', '“', '”', '„', '‟', '…', '\'']
    print(dict.fromkeys(symbol,0))
def strcount():
    s='*rr*trew*0998'
    print(s.count('*'))
def 给二维数组第一个元素赋值():
    d=[[1,2,3],[0,0,0]]
    d[0][0]=9
    print(d)
    c=[0]*3
    c[0]=1
    v=[[0]*3]*3
    v[0][0]=7
    print(v)
    a=[1,2,3]
    a.insert(3,9)
    print(a)
    import numpy as np
    array=np.ones((5,6))*1
    print(array)
    print(array[1][1])
def 深浅赋值():
    n=[1,2,3]
    b=n
    n[1]=9
    print(id(b))
    print(id(n))
    #2292460678600
    #2292460678600
    #2292460676552
    n=[]
    print(id(n))

    print(b)
def 判断两个字典是否相等():
    d={1:2,"a":1,'b':2}
    c={'b':2,'a':1,1:2}
    print(d==c)
    c = list(c.items())
    print(c)
    for i in c:
        print(i)
    a=[1,1,2,3,4,5]
    a.remove(1)
    print(a)
    a=3 if 3>4 else 2
    print(a)
    nums=[1,2,3,4,56,7]
    left,right=1,2
    sum_temp = nums[left] if left == right else sum(nums[left:right + 1])
    print(sum_temp)
    l=[[1,2,3],[3,4,5],[5,6,7]]
    print(l[1:3][0])

    l_2=[[1,3,5],[6,4,3],[3,7,9],[22,3,6]]
    print(sorted(l_2,key=lambda x: x[2]))
    #[[6, 4, 3], [1, 3, 5], [22, 3, 6], [3, 7, 9]]
    b=[]
    v=[2]
    print(b+v)
    b="1,2 3  4      6"
    print(list(filter(None,b.split(" "))))
    b=[1,2,4]
    c=b
    b[1]=0
    print(c)#[1,0,4]
    b=[5,6,7,8]
    print(c)#[1,0,4]
def tf():
    c=[1,2,3,4]
    print(c[-1])
    print(c[:-1])
tf()