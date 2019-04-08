class MaxStack(object):
    """超过了100%的方法"""
    def __init__(self):
        self.nums,self.max_nums=[],[]
    def push(self,x):
        if not self.nums:
            self.nums.append(x)
            self.max_nums.append(0)
        elif self.nums[self.max_nums[-1]]<x:
            self.nums.append(x)
            self.max_nums.append(len(self.nums)-1)
        else:
            self.nums.append(x)
    def pop(self):
        if self.nums:
            if self.max_nums[-1]==len(self.nums)-1:
                self.max_nums.pop()
                return self.nums.pop()
            else:
                return self.nums.pop()
    def top(self):
        if not self.nums:
            return 0
        else:
            return self.nums[-1]
    def getmax(self):
        return self.nums[self.max_nums[-1]] if self.max_nums else float("-inf")
    def IsEmpty(self):
        """必须要加一个判断这个栈是否是空的函数，因为
        不能够使用MinStack()是否是空去判断啊，因为MInStack里面永远有两个列表
        所以永远不为空"""
        if not self.nums:
            return True
        else:
            return False

class Queue_init(object):
    """用包含get_min函数的栈去模拟队列"""
    def __init__(self):
        self.inStack, self.outStack = MaxStack(), MaxStack()
        #1、首先，这个是最大栈
    def push(self, x):
        self.inStack.push(x)
    def pop(self):
        self.move()
        return self.outStack.pop()
    def peek(self):
        self.move()
        return self.outStack.top()
    def IsEmpty(self):
        return self.inStack.IsEmpty() and self.outStack.IsEmpty()
    #2、然后使用函数去判断是否为空
    def move(self):
        if self.outStack.IsEmpty():
            while not self.inStack.IsEmpty():
                self.outStack.push(self.inStack.pop())
                #3、这里也去判断
    def get_max(self):
        return max(self.inStack.getmax(),self.outStack.getmax())
    #4、然后添加一个get函数
def maxNumberInNums(nums,k):
    if not nums or k<=0 or len(nums)<k:
        return []
    queue=Queue_init()
    for i in range(0,k):
        queue.push(nums[i])
    ans=[]
    for t in range(k,len(nums)):
        ans.append(queue.get_max())
        queue.pop()
        queue.push(nums[t])
    ans.append(queue.get_max())
    return ans

def using_deque(nums,k):
    if not nums or k<=0 or len(nums)<k:
        return []
    """使用一个双向序列去保存窗口中可能成为最大值的数的索引，deque里面存的是降序的。"""
    #如果先把第一个窗口填满(少填一个)，那么后面就不需要判断窗口是否是满的啦,但是这样的话，需要加上不少的代码。
    #还是直接都同一处理吧
    from collections import deque
    ans,mydeque=[],deque()
    for index,item in enumerate(nums):
        while mydeque and nums[mydeque[-1]]<=item:
            mydeque.pop()
        mydeque.append(index)
        if mydeque[0]<=index-k:
            mydeque.popleft()
        if index>=k-1:
            ans.append(nums[mydeque[0]])
    return ans



nums=[2,3,4,2,6,2,5,1]
print(maxNumberInNums(nums,3))
print(using_deque(nums,3))

