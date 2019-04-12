#计算排列组合
#首先，是存在这种排列组合函数可以
from scipy.special import comb,perm
print(perm(6,3))#120.0
print(comb(6,3))#20.0
#这种引用包再笔试的时候其实是无法引用的，所以还是要直接用公式
from math import factorial

def combination_test(n,m):
    return factorial(n)//(factorial(n-m)*factorial(m))
def permutation_test(n,m):
    return factorial(n)//factorial(n-m)
print(permutation_test(6,3))#120
print(combination_test(6,3))#20
