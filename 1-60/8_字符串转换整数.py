"""请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2**31,  2**31 − 1]。如果数值超过这个范围，qing返回
 INT_MAX (231 − 1) 或 INT_MIN (−231) 。"""
def myAtoi(str):
    str=str.strip(" ")#用于移除字符串头尾指定的字符（默认为空格）或字符序列。
    #这里要用str承接。很奇怪，有点乱
    if str==None or str=="" or not (str[0]=="-" or str[0]=="+" or "0"<=str[0]<="9"):return 0#str[0]必须放在最后
    else:
        index=0
        sign=[1,-1][str[0]=="-"]
        if sign==-1 or str[0]=="+":str=str[1:]
        s=""
        while(index<len(str) and "0"<=str[index]<="9"):
            #一定要是判断index的放在前面，而不能是while("0"<=str[index]<="9" and index<len(str)):
            s=s+str[index]
            index+=1
        if s != "":
            s = sign * int(s)
        else:
            return 0
        if s>=2**31:return  2**31-1
        elif s<-2**31:return -2**31
        else:
            return s

def correct_convert(s):
    if len(s) == 0: return 0
    ls = list(s.strip())

    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-', '+']: del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))
print(correct_convert("  -99oo000888"))
print(myAtoi("  +1999999999999999999999"))