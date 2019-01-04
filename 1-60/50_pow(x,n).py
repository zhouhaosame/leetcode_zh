def pow(x,n):
    def revse(x,n):
        if n<0:
            return 1/revse(x,-n)
        elif n==0:
            return 1
        elif n%2==0:
            return revse(x**2,n//2)
        #是revse(x**2,n/2),而不是x**x*revse(x,n/2)，也不是revse(x**x,n/2)
        return x*revse(x,n-1)
    return revse(x,n)


class Solution:
    def __init__(self,x,n):
        self.x=x
        self.n=n
        def myPow(x,n):
            if not n:
                return 1
            if n < 0:
                return 1 / myPow(x, -n)
            if n % 2:
                return x * myPow(x, n - 1)
            return myPow(x * x, n / 2)
        self.res=myPow(self.x,self.n)
"""上述的两种方法受困于--- (34, 'Result too large'),会提示你，出错了，返回运行失败
但是Solution那里的类中函数的使用可以借鉴一下！！！！
接下来这种方法竟然，竟然超过了100%"""


def myPow_newb(x, n):
    if n == 0: return 1
    if n < 0: return 1 / myPow_newb(x, -n)
    half = myPow_newb(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
def myPow_zuinb(x,n):
    b = n
    a = x
    if b == 0: return 1
    if b < 0: return 1.0 / myPow_zuinb(a, -b)
    half = myPow_zuinb(a, b // 2)
    if b % 2 == 0:
        return half * half
    else:
        return half * half * a
x=2.00000
n=3488
#print(pow(x,n))
#print(s.myPow(x,n))
#print(Solution(x,n).res)
print(myPow_newb(x,n))
print(myPow_zuinb(x,n))
"""开始的两种方法--会提示你，出错了，返回运行失败，而下面的nb的方法会返回  inf和0.0这个和OJ的结果是一样的。。。
怎么我也能返回这个呢？？"""