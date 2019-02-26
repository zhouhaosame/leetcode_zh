def topKFrequent(nums, k):
    import collections
    import heapq
    count = collections.Counter(nums)
    print(count)#Counter({1: 4, 3: 4, 4: 2, 2: 1, 5: 1})
    print(type(count))
    print(count.keys())#dict_keys([1, 2, 3, 4, 5])，可以说和list的作用类似的
    print(type(count.keys()))
    print(count.get)#<built-in method get of Counter object at 0x000002297E8F8AF0>，是一个函数
    """return heapq.nlargest(k, count.keys(), key=count.get)
    """
    #key和sort函数中的key类似，用列表元素的某个属性和函数作为关键字
    #这里记住就行了，因为count.get表示的就是一个函数。得到的是对应的函数出现次数。
    return heapq.nlargest(k,count.keys(),lambda item:count[item])#这个正确的，方然上面也是正确的。
nums=[1,1,1,1,2,3,3,3,3,4,4,5]
print(topKFrequent(nums,2))#[1, 3]

from collections import Counter
a=Counter("success")
print(a)#Counter({'s': 3, 'c': 2, 'u': 1, 'e': 1})
b=(1,2,3,4,1,2,3)
b=Counter(b)
print(b)#Counter({1: 2, 2: 2, 3: 2, 4: 1})
c={"s":3,"c":2,"e":1,"u":1}
c=Counter(c)
print(c)#Counter({'s': 3, 'c': 2, 'e': 1, 'u': 1})
"""很明显，Counter中对应的都是字典形式的"""
print(a.elements())#<itertools.chain object at 0x000001B6DEF85A20>
print(list(a.elements()))#['s', 's', 's', 'u', 'c', 'c', 'e']
"""注意，这里不是字典中所有的键，而是COunter中特有的键，旅行它作为计数器的职责"""
####
###
print(a.most_common(2))#[('s', 3), ('c', 2)]
print(a.get("s"))#3
print(a["s"])#3
print(a.get)#<built-in method get of Counter object at 0x000001C639E28AF0>,是一种得到对象计数的内置方法。

a=[4,6,3,5,9]
b=[0,1,2,3,4]
b=sorted(b,key=lambda item:a[item])
print(b)#[2, 0, 3, 1, 4]
"""一定要注意，这个是有返回值的啊！！！！"""
print(a)#[4, 6, 3, 5, 9]