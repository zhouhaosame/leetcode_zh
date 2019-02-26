def pow_my(base,exponent):
    if base==0:
        return 0
    if exponent==0:
        return 1
    if -1<exponent<1:
        return -1
    isminus=0 if exponent>=0 else 1
    exponent=exponent if exponent>0 else -exponent
    def pow_recurse(base,exponent):
        if exponent==1:
            return base
        if exponent&0x1==0:#满足条件的话就是偶数
            #return pow_recurse(base*base,exponent//2)
            return pow_recurse(base * base, exponent>>1)
        #!!!!!注意了，这里一定要用//去除2.因为有时候。exponent是类似
        #2.0的形式，所以不能够&。一定要保证exponent是整数
            """>>1是除以2的意思啊"""
        else:
            return pow_recurse(base*base,exponent>>1)*base
    result=pow_recurse(base,exponent)
    return result if not isminus else 1/result
base_list=[0,1,4,0.2]
exponent_list=[0,1,-1,-2,0.1]
result=[pow_my(base,exponent) for base in base_list for exponent in exponent_list]
print(result)
#print([(x,y) for x in [1,2,3] for y in [4,5,6]])
print(pow_my(2,4))