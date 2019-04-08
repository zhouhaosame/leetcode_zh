"""别忘了十进制如何转换成二进制"""
def inter_to_binary_and_computing_the_number_of_one(n):
    nums=[1] if n<0 else []
    n=abs(n)
    if not n:
        return 0
    while(n):
        nums.append(n%2)
        n=n//2
    count=0
    for x in nums:
        if x==1:
            count+=1
    return count
"""这个解法是错误的，因为在计算机中，负的二进制用补码表示，所以9是2，但是-9并不是3啊"""


def correct(n):
    #n整数 & 1，就知道了整数的二进制的最后一位是不是0了
    """最难得就是如果n是负的怎么办？？？"""
    #count=0
    #while(n):
       # if n&1==1:
      #      count+=1
     #   n=n>>1
    #return count
    """所以上述这种方法是不正确的，如果n是负的，那么会陷入死循环，那么该怎么办呢
    既然n与1可以看出来最后一个是不是1，那么n与2岂不是就能知道倒数第二位是不是1啦，然后与4.。。。
    #这样的话，有一个难点，就是比较的那个要增加到什么时候为止呢？？？"""
    """这里又涉及了一个知识点，那就是比如1，它表示成二进制的时候，有多少位呢？？
    在python中是用多少位表示的呢？因为python中是大数表示，所以这种方式不能使用"""
    count=0
    while(n):
        temp=n-1
        n=n&temp
        count+=1
    return count

def NumberOf1(n):
    if n >= 0:
        return bin(n).count('1')
    else:
        return bin(n & 0xffffffff).count('1')
    """这个才是正确的"""

def NumberOf_NEW(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
        #这个函数是得到n的补码的正二进制。默认输入的n是32位表示的。如果很大的话，相应的fff也会增多
    while n:
        count += 1
        n = (n - 1) & n
    return count

n=9

print(correct(n))
print(inter_to_binary_and_computing_the_number_of_one(n))
print((bin(-5)))#-0b101
m=-99999999
print(bin(m))#原码
print(NumberOf1(m))
print(NumberOf_NEW(m))
"""
print(n>>1)#4
print(n>>2)#2
print(n<<1)#18
print(n<<2)#36
n=-9
print(n>>1)#-5
print(n>>2)#-3
print(n//2)#-5
print(n<<1)#-18
print(9&2)#1001$10=0
print(9&1)#1,原来是将&两边的先自己转化成二进制的啊。n整数&1，就知道了整数的二进制的最后一位是不是0了
"""


"""python能表示的整数比C/C++大的多,事实上只要你有足够的存储空间python就能表示之.
而不象C/C++一般只有一个CPU字大小.
python内部好象都用正数表示整数, 表示负数时只是简单的在前面加个负号."""