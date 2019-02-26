class MinStack(object):
    """超过了100%的方法"""
    def __init__(self):
        self.nums=[]
        self.min_nums=[]
        #因为len的时间复杂度是O(1)所以，min_nums可以是只保存历代的min的index
        """为什么保存index就可以了呢，比如index=i,是当前的最大值。在i出栈之前，i之前的历史
        min的索引是不可能出栈的，而且还和data stack中一一对应，因为根本没变"""
    def push(self,x):
        if not self.nums:
            self.nums.append(x)
            self.min_nums.append(0)
        elif self.nums[self.min_nums[-1]]>x:
            self.nums.append(x)
            self.min_nums.append(len(self.nums)-1)
            #因为python中的len的时间复杂度是O(1)
        else:
            self.nums.append(x)
    def pop(self):
        if self.nums:
            if self.min_nums[-1]==len(self.nums)-1:
                self.min_nums.pop()
                return self.nums.pop()
            else:
                self.nums.pop()
    def top(self):
        return self.nums[-1]
    def getMin(self):
        return self.nums[self.min_nums[-1]]
"""
def greeting(name: str) -> str:
    return 'Hello ' + name
    In the function greeting, the argument name is expected to be of type 
    str and the return type str. Subtypes are accepted as arguments.
    也就是说，参数后面:加变量类型是类似注释的东西，就是为了提醒你这个变量应该是输入什么类型的。
    而后面跟着的->  :是这个函数的返回值类型
"""


class Queue_init(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)
    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outStack.pop()
    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]
    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)
    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        #将要出的元素都放在outstack中，如果里面不是空的，
        # 就一直出，知道里面为空为止，然后将in里面的放入out中，再出