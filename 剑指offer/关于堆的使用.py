import heapq
nums=[2,1,3,9,3,6,7,5]
heapq.heapify(nums)#以线性的时间将一个列表转化成堆
print(nums)#[1, 2, 3, 5, 3, 6, 7, 9]，很明显，转化之后nums改变了，是一个堆树的层序遍历。
print(type(nums))#list
#将list类型转化为heap, 在线性时间内, 重新排列列表。
#print(a)#None
#print(heapq.heappop(a))#这条命令是错误的，heap argument must be a list
print(heapq)#<module 'heapq' from 'C:\\Users\\zhouhao\\Anaconda3\\lib\\heapq.py'>
"""这个时候，nums虽然不是有序的，但是他是一个堆的层序遍历，所以它的第一个元素肯定是最小的了"""
print(nums[0])#1,只查看，不弹出。
print(heapq.heappop(nums))#1,删除并返回堆中最小的元素
print(nums)#[2, 3, 3, 5, 9, 6, 7],很明显“堆”改变了。
item=heapq.heapreplace(nums, -100)#nums要是iterable,删除现有最小元素并将其替换为一个新值。
#弹出一个最小的值，然后将-100插入到堆当中。
print(item)#2
print(nums)#[-100, 3, 3, 5, 9, 6, 7],很明显，“堆”中的最小值被替换了。替换之后，这个
#堆还是保持最小堆的性质的
#heapq.nlargest(n, iterable) 和 heapq.nsmallest(n, iterable)
print(heapq.nlargest(2,nums,key=None))#[9, 7]
print(nums)#[-100, 3, 3, 5, 9, 6, 7],很明显只是返回不会修改nums的内容
print(heapq.nsmallest(2,nums,key=None))#[-100, 3]
"""上述的nums从头到尾只是list类型的，是iterable的，使用heapq的各种方法操作
其中，nums是作为输入的。
key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字
"""
print(nums)#[-100, 3, 3, 5, 9, 6, 7]
heapq.heappush(nums,22)
print(nums)#[-100, 3, 3, 5, 9, 6, 7, 22],最小堆的层序遍历。往堆中插入一条新的值


class TopkHeap(object):#在nums中取前k个最大的
    def __init__(self, k):
        self.k = k
        self.data = []

    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)

    def TopK(self):
        return [x for x in reversed([heapq.heappop(self.data) for _ in range(len(self.data))])]
class BtmkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def Push(self, elem):
        # Reverse elem to convert to max-heap
        elem = -elem
        # Using heap algorighem
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:#这里和小顶堆是一样的
                heapq.heapreplace(self.data, elem)

    def BtmK(self):
        return sorted([-x for x in self.data])
list_rand = [1,2,3,4,-1,-2,0,6,4,3,4,9,8]
th = TopkHeap(3)
for i in list_rand:
    th.Push(i)
print(th.TopK())#[9, 8, 6]
