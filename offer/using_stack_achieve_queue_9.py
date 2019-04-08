class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,x):
        self.stack1.append(x)
    def pop(self):
        while(self.stack1):
            temp=self.stack1.pop()
            self.stack2.append(temp)
        itme=self.stack2.pop()
        while(self.stack2):
            temp=self.stack2.pop()
            self.stack1.append(temp)
        return itme
    """使用stack1来存储数据，stack2是过渡空间，最后操作完成后
    要返回原来的形式"""
    def peek(self):
        while(self.stack1):
            temp=self.stack1.pop()
            self.stack2.append(temp)
        itme=self.stack2[-1]
        while(self.stack2):
            temp=self.stack2.pop()
            self.stack1.append(temp)
        return itme
    def empty(self):
        return True if not self.stack1 else False
