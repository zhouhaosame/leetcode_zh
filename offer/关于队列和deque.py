"""关于双向队列"""
from collections import deque
#可以指定生成队列的大小，这个一单指定，大小是不能改变的
mydeque=deque(maxlen=5)
print(len(mydeque))#0
print(mydeque.maxlen)#5
#默认从右边插入
mydeque.append(1)
print(mydeque)#deque([1], maxlen=5)
mydeque.extend([2,3,4,5,6,7])
print(mydeque)#deque([3, 4, 5, 6, 7], maxlen=5)，从右边插入的，就把元素从左边挤出去了
mydeque.appendleft(0)
print(mydeque)#deque([0, 3, 4, 5, 6], maxlen=5),从左边插入，就把元素从右边挤出去了
#主要是出队，他们本质上就是list
print(mydeque.pop())#6,只要是队列，pop都是摘除的队列的最后一个元素
print(mydeque)#deque([0, 3, 4, 5], maxlen=5)
print(mydeque.popleft())#0
#统计元素的个数
print(mydeque.count(3))#1
#反转操作
print(mydeque.reverse())#None
print(mydeque)#deque([5, 4, 3], maxlen=5),由此可见，reverse和sort的方法是在本地操作的
#重要方法说明rotate
mydeque=deque([1,2,3,4,5,6,7])
print(mydeque)#deque([1, 2, 3, 4, 5, 6, 7])
#rotate（value) 对队列实行旋转操作
mydeque.rotate(2)#指定次数，默认一次
print(mydeque)#deque([6, 7, 1, 2, 3, 4, 5])
mydeque.rotate()
print(mydeque)#deque([5, 6, 7, 1, 2, 3, 4])


