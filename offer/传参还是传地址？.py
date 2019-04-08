#a,b地址不同
a=[1,2,3]
b=[1,2,3]
a=(1,2,3)
b=(1,2,3)
a=set([1,2])
b=set([1,2])
a={"1":2}
b={"1":2}
#a,b地址相同
a="cd"
b="cd"
a=1
b=1
print(id(a))
print(id(b))

