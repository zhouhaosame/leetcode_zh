class test1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum_new(self):
        return self.a+self.b
t=test1(1111111111111111111111111111111111,33333333333333333333333333333)
print(t.sum_new())
print(2**999)
print(len("zhou"))
print(len("周"))
import sys
a=""
print(a.__sizeof__())#49
print(sys.getsizeof(a))#49
#说明这两个函数是一样的
a=a+"z"
print(a.__sizeof__())#50
a=a+"j"
print(a.__sizeof__())#51
#一个空的字符串的声明就已经占据了49了。然后每放入一个字母，就+1
c=""
print(c.__sizeof__())#49
b=''
print(b.__sizeof__())#49
#说明""和''是等价的，在内存方面
i=9
print(i.__sizeof__())#28
print(sys.getsizeof(int()))#24
print(sys.getsizeof(int(0)))#24
i=0
print(i.__sizeof__())#24
print(sys.getsizeof(int(1)))#28
print(sys.getsizeof(int(-1)))#28
print(sys.getsizeof(int(10)))#28
print(sys.getsizeof(int(10e12)))#32
print(sys.getsizeof(None))#16
#很明显，一个None是16.说明只要生命了，就会占用16字节的内存。存储着一些其他信息。
# 然后生命存储int信息，有耗费了8字节，所以生成一个空的int就耗费了24字节
# 然后每添加一个数字就增加四字节

print(sys.getsizeof(float()))#24
a=4.0
print(a.__sizeof__())#24
print(sys.getsizeof(float(9.0)))#24
#为什么float和int不一样呢？？
print(sys.getsizeof([]))#64
print(sys.getsizeof([[]]))#72
print(sys.getsizeof([int()]))#72
print(sys.getsizeof([2]))#72
print(sys.getsizeof([0]))#72
print(sys.getsizeof([99]))#72
print(sys.getsizeof([12,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))#72
print(sys.getsizeof(["222"]))#72
print(sys.getsizeof(["2228888888888888888888888888888888888888888"]))#72
print(sys.getsizeof(["222","3"]))#80
print(sys.getsizeof([["2","3"]]))#72
print(sys.getsizeof({}))#288
print(sys.getsizeof({2:3}))#288
print(sys.getsizeof({"3":2,"4":5}))#288
#字典类型直接这么大，难道是创建的时候就已经确定好字典能够存储的最大的内容了？？？
#这个是肯定的啊，因为{}是hashable的，如果不提前确定好范围，那么怎么一下子找到存储位置呢
#这么说set也是固定的啦？不是，下面有例子，真是奇怪
print(sys.getsizeof(()))#48
print(sys.getsizeof((2)))#28,很奇怪啊，这里为什么是28呢？？？
print(type((2)))#class int,因为这里(2)的类型是int啊
print(type((2,3)))#tuple
print(sys.getsizeof((2,3)))#64
print(sys.getsizeof((2,3,4)))#72
print(sys.getsizeof((2,3,4,5)))#80
#print(sys.getsizeof(tuple(2)))这里是错误的,'int' object is not iterable
"""当元祖里面只有一个元素时候，要在元素后面添加,来消除歧义"""
print(type((2,)))#tuple
print(sys.getsizeof(set()))#224
print(sys.getsizeof(set([1,1,1])))#224
print(sys.getsizeof(set([(1,2),1,1])))#224
#print(sys.getsizeof(set([[1,2],1,1])))这个命令是错误的，因为[]里面的元素必须都要是hashable的
print(sys.getsizeof(set([1,2])))#224
print(sys.getsizeof(set([1,2,3,4,5])))#224
print(sys.getsizeof(set([1,2,3,4,5,6])))#736
print(sys.getsizeof(set([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,22,23])))#736
print(sys.getsizeof(set([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,22,23,24])))#2272
#多了一个数，竟然多了这么多内存？？到底是什么机制？？
a={"a":2,"b":4}
print(a.get("c",9))
#a不变
print(a.setdefault("c",9))
print(a)#{'a': 2, 'b': 4, 'c': 9}
print(a.setdefault("c",2))#9
import collections
a=collections.defaultdict(list)
print(a["c"])#[]
print(a)#defaultdict(<class 'list'>, {'c': []}),很明显也修改了a。list默认值[]
a=collections.defaultdict(int)
print(a["c"])#0
a=collections.defaultdict(set)
print(a["c"])#set()
a=collections.defaultdict(str)
print(a["c"])#空字符串
#a=collections.defaultdict(1)这样是错误的，不能够直接赋值


def zero():
    return 3
d = collections.defaultdict(zero)
print(d["c"])#3
print(d)#defaultdict(<function zero at 0x0000022956E7F378>, {'c': 3})
#或者
a = collections.defaultdict(lambda:9)#注意了，没有x
print(a["c"])#9
#暂时没有发现使用了x传递进去，values随着key改变的方法
a = collections.defaultdict(lambda:[1,2])#注意了，没有x
print(a["c"])#[1,2]

print(sys.getsizeof([]))#64
print(sys.getsizeof([2]))#72
print(sys.getsizeof([2,3]))#80
print(sys.getsizeof([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))#208
print(sys.getsizeof([i for _ in range(1,3) for i in range(1,10)]))#264
print(sys.getsizeof([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))#280
print([i for _ in range(1,3) for i in range(1,10)])
print(sys.getsizeof([i for _ in range(1,4) for i in range(1,10)]))#344
print(sys.getsizeof([i for _ in range(1,5) for i in range(1,10)]))#434
#print(sys.getsizeof([i for _ in range(1,100000) for i in range(1,10)]))#
a="12qwYu"
print(a.upper())