def reverse_int(x):#只是我自己写的，但是有问题。有的结果是错误的。
    # 加上return x if -(2 ** 31) - 1 < x < 2 ** 31 else 0
    #就好了。
    x = str(x)
    sign=""
    if x.startswith("-"):
        sign = x[0]
        x = x[1:]
    x=list(x)
    x.reverse()
    x=int(sign+"".join(x))
    return x if -(2 ** 31) - 1 < x < 2 ** 31 else 0
def correct_reverse_int(x):
    sign = [1, -1][x < 0]#[1,-1]是一个列表。[x<0]表示index
    rst = sign * int(str(abs(x))[::-1])#1、str[:-1]去掉最后一个字符2、str[::-1]，表示反转
    return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0
"""所以整数就有“有符号整数”和“无符号整数”之分啊，比如你说的8位的整数，
如果按无符号整数来用，那么最小值0（二进制0000-0000），最大值是255（1111-1111），
总数是256个，而如果作为有符号整数来用，则最小值为-128（二进制1000-0000），
最大值为127（0111-1111），总数也还是256个"""
print(correct_reverse_int(-12300))
print(reverse_int(-7537832))