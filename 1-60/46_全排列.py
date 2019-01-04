def permute(nums):
    import copy
    permutation,i=[],len(nums)-1
    #使用递归的方式吧
    def insert_permutation(str_list,n):
        temp=[]
        for item in str_list:
             for i in range(len(item)+1):
                 s=copy.deepcopy(item)
                 s.insert(i, n)
                 temp.append(s)
        str_list=temp
        return str_list
    def reve(i):
        if i==0:
            return [[nums[i]]]
        permutation=insert_permutation(reve(i-1),nums[i])
        return permutation
    #整体赋值的话，会将引用直接覆盖掉，和单个的赋值不一样，所以需要返回一个permutation
    return reve(i)
    #%8,已经算是比较慢的了， 这是 basic idea

def iterate(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms

def reduce_permute(nums):
    #还是对reduce的了解不深啊
    from functools  import reduce
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p) + 1)], nums, [[]])

#reduce产生的结果是在左边的input，这里面就是相当于P，iterable list里面的每一个都是作为右边的输入的
nums=[1,2,3]
print(permute(nums))
print(iterate(nums))
print(reduce_permute(nums))



