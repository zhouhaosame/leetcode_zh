"""
python 存储数据是 number，对于整型，不区分 int, byte, long
"""
"""
这里面是在c语言中的
n1 = 0x80000000; #在c中是最小负数，-2147483648
n2 = 0x7fffffff; #在c中是最大正数，2147483647

printf("%d\n", n1);-2147483648
printf("%d\n", n2);2147483647
printf("%d\n", (n1-1)); // 最小负数减去1变成最大正数
printf("%d\n", (n1) & (n1-1));0
"""
"""
在python中，为什么负的整数的二进制是0b前面加负号呢？？因为python3是没有整数的溢出的，所以不管多大都可以
，这样的话，你就不知道符号位在什么位置。所以就在前面加上-，表示负的 。但是这样的形式只是原码形式。
原码是给人看和计算的。补码是给计算机看和计算的。反码是中间过渡。

"""
print(bin(-9))#-0b101，这里得到的是原码的形式。但是实际上-9存在计算机中是以反码的形式存储的，什么样的呢？
print(bin(-9&0xffffffff))#0b11111111111111111111111111110111
"""&0xffffffff的意思就是普通的意思，之前之所以搞错了，是以为参加运算的-9的二进制表示是-0b101，
原码是-0b00..00101，前面有多少个0我们不知道。0xffffffff一共是32位
，然后-9的补码是-111...1011,除去-不知道有多少位，但是只有后面的32位是“有效的”，因为0xffffffff
前面都是0。而且0xffffffff是正的。&之后负号（可能用1表示）被消掉了。最后的结果是0b11111111111111111111111111110111。
！！！！！！
所以里面最重要的就是-9参加运算的时候是补码的形式。
原来bin显示的是原码啊！！"""
print("%x"%-10)#-a
n1 = 0x80000000
n2 = 0x7fffffff
print(n1) # 2147483648
print(n2) # 2147483647
#都是正的

n3 = -2147483648
n4 = 2147483647
print(n3)#-2147483648
print(bin(-n3))#0b10000000000000000000000000000000，这里显示的是原码
"""注意了，这里0b之后的是32位"""
print(bin(n3))#-0b10000000000000000000000000000000，原码
#由此可见，正负只是最前面有没有负号而已
print(n4)
print (n3 - 1) # -2147483649
n3 = n3 & 0xffffffff # 就是n3的补码&0xffffffff。
print(bin(n3))#0b10000000000000000000000000000000
print(n3) # 2147483648。这里得到的是n3的补码。直接print的话是将其当做原码。只是很巧，这个原码和补码相同而已
"""python中负数&ffffffff，就变成了正数"""
print(n3 - 1) # 2147483647

n5 = -2147483647
print(bin(n5))#-0b1111111111111111111111111111111，原码。其补码是-0b100000....001
"""注意了，这里是31个1，因为最前的那个0被省掉啦，并不是说前面的那个负号也是一个1,补码最前面还有个1呢"""
n5 = n5 & 0xffffffff # 转换成正数，不受int范围限制的
print(n5) # 2147483649。这里之前怎么都不理解。原来是补码是上面的，print是将其当做原码并且输出对应的十进制
print(bin(n5))#0b10000000000000000000000000000001



