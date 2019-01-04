def permute(nums):
    permutations=[[]]
    for n in nums:
        ans=[]
        for item in permutations:
            for i in range(len(item)+1):
                s=item[:i] + [n] + item[i:]
                if s not in ans:
                    ans.append(s)
        permutations=ans#这里按理说保险的话就是深拷贝，但是经过测试，ans直接为空的话，不会影响permutations的
        #z值，如果要是丹丹的改变其中的一个值，那么permutations里面的值就会发生变化.
        #这里面的原因并不是说赋值为空就是将索引断开了，恰恰相反，只不过是用了一个空的列表重新进行赋值，这样的
        #话，ans就有了新的地址
    return permutations

def permuteUnique(nums):
    """这种方法更快"""
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break
                """想想这一种可能 x1,x2,x3,1,x4,x5,x6,x7,添加1进去，上述的方法是在1的前面添加，添加之后是
                x1,x2,1(new),x3,1(old),x4,x5,x6,x7,为什么就不在后面添加了呢？
                x1,x2,x3,1(old),x4,x5，1(new),x6,x7,因为这种方法是x1,x2,x3,1(new),x4,x5，1(old),x6,x7中
                1的交换，会在别的item中得到，所以可以只在前面添加"""
                #handles duplication
                """When k=0, it holds.
Then we prove it will also holds in each iteration using proof by contradiction.
Suppose duplicate happens when inserting n into the ith location, the result is [l2[:i], n, l2[i:]], and it duplicates with the item [l1[:j], n, l1[j:]]
Suppose i < j, then we have l1[i] ==n, however, we will break when l1[i]==n, and thus n will not be inserted after l1[:j] -> contradiction,
Suppose i > j, then we have l2[j] == n, however we will break when l2[j] == n, and thus n will not be inserted after l2[:i] -> contradiction.
Suppose i==j, then we have l1==l2, which contradicts the assumption that ans is a list of unique permutations.
Thus the argument hold."""
        ans = new_ans
    return ans
nums=[1,2,3,1]
print(permute(nums))
print(permuteUnique(nums))
