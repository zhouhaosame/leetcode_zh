from collections import Counter
a=[1,2,2,2,3,4,4,4,4,6,7,7]
c=Counter(a)#和字典类似
b=[]
for x in c:#这样的话遍历的是key
    b.append(c[x])
print(b)#[1, 3, 1, 4, 1, 2]
c[1]=0
b=[]
for x in c:#这样的话遍历的是key
    b.append(c[x])
print(b)#[0, 3, 1, 4, 1, 2]
"""虽然不存在的话，默认是0，但是当初如Counter之后，即使是0，
也不会被删除掉"""
del c[1]#这才是真正的删除掉
b=[]
for x in c:#这样的话遍历的是key
    b.append(c[x])
print(b)#[3, 1, 4, 1, 2]
c.clear()
b=[]
for x in c:#这样的话遍历的是key
    b.append(c[x])
print(b)#[]