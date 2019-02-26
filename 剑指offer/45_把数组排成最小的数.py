"""因为leetcode是最大的数，所以这里我们去得到最大的数"""
from functools import cmp_to_key
def largestNumber1(nums):
    def new_compare(n,m):
        """这里是比较n与m谁应该在前面的。从而得到最大的数。
        按理说，应该是让nums中降序排序的。
        如果nm>mn则，n在前面，m在后面,与正常的compare
        函数类似，我们如果认为n在m前面，也就是n大于m,则返回True"""
        if n+m>m+n:
            return 1
        elif n+m==m+n:
            return 0
        else:
            return -1
    nums=sorted(list(map(str,nums)),key=cmp_to_key(new_compare),reverse=True)
    """这里为什么reverse是true呢，比如[2,0,3,4,1]四个中，顺序是4,3,2,1,0--降序    
    2:[0,1,-1,-1,1]
    0:[-1,0,-1,-1,-1]
    3:[1,1,0,-1,1]
    4:[1,1,1,0,1]
    1:[-1,1,-1,-1,0]。
    很明显，只有根据降序，才能够得到正确的顺序"""
    return "".join(nums) or "0"
nums=[10,2]
print(largestNumber1(nums))
nums=[]
def cmp_new(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
nums=[2,0,3,4,1]
print(sorted(nums,key=cmp_to_key(cmp_new),reverse=True))

from functools import cmp_to_key
a=[-2,2,3]
print(sorted(a,key=cmp_to_key(lambda x,y:x*y)))#[2, 3, -2]
a=[2,-2,3]
print(sorted(a,key=cmp_to_key(lambda x,y:x*y)))#[3, -2, 2]