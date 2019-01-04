def devide(dividend,divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
def 非常快的方法(dividend,divisor):
    positive = (dividend < 0)==(divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            """>> 和 <<都是位运算，对二进制数进行移位操作。            
<< 是左移，末位补0，类比十进制数在末尾添0相当于原数乘以10，
x<<1是将x的二进制表示左移一位，相当于原数x乘2。
比如整数4在二进制下是100，4<<1左移1位变成1000(二进制)，结果是8。
>>是右移，右移1位相当于除以2。
而>>=和<<=，就是对变量进行位运算移位之后的结果再赋值给原来的变量，
可以类比赋值运算符+=和-=可以理解。"""
            i <<= 1
            temp <<= 1
            """这里是两个while循环，当temp足够大的时候，就跳出内部循环
            其实就是变相的使用了2倍啊？？"""
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
#这种方法，如果dividend很大，且divisor很小，就超时了。
x=20
y=2
print(非常快的方法(x,y))