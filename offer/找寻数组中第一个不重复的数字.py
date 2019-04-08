def search(nums):
    import collections
    dct = collections.defaultdict(int)
    for x in nums:
        dct[x]+=1
    select_nums=dict(filter(lambda x1:x1[1]<2,dct.items())).keys()
    if not select_nums:return 0
    for x in nums:
        if x in select_nums:
            return x
    #超过50%，但是接下来的方法超过100%
def fastest(nums):
    letters='abcdefghijklmnopqrstuvwxyz'
    select_nums=[nums.index(x) for x in letters if nums.count(x)==1]
    if not select_nums:
        return min(select_nums)
    else:
        return -1
"""第一个函数的时间复杂度是2-3N，第二个方法是26N（count）+26N（index）+1N,
但是第二种再leetcode上的速度更快，这是为什么呢？
因为字符串的built-in函数是用c code写的，速度很快"""
nums=[1,1,2,2,4,5,6,6]
search(nums)