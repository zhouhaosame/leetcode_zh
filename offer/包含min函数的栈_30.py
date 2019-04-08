class min_stack:
    def __init__(self):
        self.nums=[]
        self.min_nums=[]
        #因为len的时间复杂度是O(1)所以，min_nums可以是只保存历代的min的index
    def push(self,x):
        if not self.nums:
            self.nums.append(x)
            self.min_nums.append(0)
        elif self.nums[self.min_nums[-1]]>x:
            self.nums.append(x)
            self.min_nums.append(len(self.nums)-1)
        else:
            self.nums.append(x)
    def pop(self):
        if self.nums:
            if self.min_nums[-1]==len(self.nums)-1:
                self.nums.pop()
                self.min_nums.pop()
            else:
                self.nums.pop()
    def top(self):
        return self.nums[-1]
    def getMin(self):
        return self.nums[self.min_nums[-1]]

