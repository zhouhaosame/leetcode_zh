"""递归用来验证"""
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def fibo_not_recurse(n):
    first=0
    second=1
    if n<=0:
        return 0
    elif n==1:
        return 1
    for i in range(1,n):
        temp=second
        second=first+second
        first=temp
    return second
"""就是用两个数不断地存储f(n-1)和f(n-2).
和青蛙跳台阶类似"""

n=13
print(fibo(n))
print(fibo_not_recurse(n))