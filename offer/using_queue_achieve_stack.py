class MyStack:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def push(self,x):
        self.queue1.append(x)
    def pop(self):
        while(self.queue1):
            temp=self.queue1.pop(0)
            self.queue2.append(temp)
        self.queue2.pop()
        item=temp
        while(self.queue2):
            temp=self.queue2.pop(0)
            self.queue1.append(temp)
        return item
    def top(self):
        while(self.queue1):
            temp=self.queue1.pop(0)
            self.queue2.append(temp)
        item=temp
        while(self.queue2):
            temp=self.queue2.pop(0)
            self.queue1.append(temp)
        return item
    def empty(self):
        return True if not self.queue1 else False
"""其实你很简单那，虽然python的栈和队列都是list表示的
但是，只要随时看着栈或者队列的性质就可以实现了"""
a=[1,3,4,5,6]
while(a):
    print(a.pop(0))