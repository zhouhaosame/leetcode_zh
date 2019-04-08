"""一共是两种匹配模式，A[.[B]][e|EC],.B[e|EC]"""
"""
def stringIsRepresentNumber(chars):
    if not chars or not str.strip(chars):
        return False

    chars=str.strip(chars)#去掉头尾的空白字符
    #chars.strip()#在python3中，strip函数是str的一个函数，与python2不一样了
    print(chars)
    chars_len = len(chars)
    A_exsit,B_exsit,C_exsit=0,0,0
    A_isnumber,B_isnumber,C_isnumber=0,0,0
    def scan_unsignnumber(i):
        while(i<chars_len):
            if ord("0")<=ord(chars[i])<=ord("9"):
                i+=1
            else:
                return i
        return i
    def scan_signnumber(i):
        if chars[i] in ["+","-"]:
            i+=1
        while(i<chars_len):
            if ord("0")<=ord(chars[i])<=ord("9"):
                i+=1
            else:
                return i
        return i
    i=0
    cur_index=scan_signnumber(i)
    A_exsit=1 if cur_index>i else 0
    A_isnumber= A_exsit and chars[i:cur_index] not in ["+","-"]
    if cur_index<chars_len and chars[cur_index]==".":
        temp=cur_index+1
        if temp==chars_len:
            return True
        cur_index=scan_unsignnumber(temp)
        B_exsit=cur_index>temp
        B_isnumber=B_exsit
    if cur_index<chars_len and chars[cur_index] in ["e","E"]:
        temp=cur_index+1
        if temp==chars_len:
            return False
        cur_index=scan_signnumber(temp)
        C_exsit=cur_index>temp
        C_isnumber=C_exsit
    if cur_index>chars_len-1 and ((A_isnumber and  B_isnumber and C_isnumber)\
        or (A_isnumber and not B_exsit and C_isnumber)\
        or (A_isnumber and B_isnumber and not C_exsit) or (A_isnumber and not B_exsit and not C_exsit) or\
        (not A_exsit and B_isnumber and C_isnumber) or (not A_exsit and B_isnumber and not C_exsit)):
        return True
    else:
        return False
    """

#按理说的确是从左到右的检测。分别用bool来标识A,B,C是否存在。
def stringIsRepresentNumber(chars):
    if not chars or not str.strip(chars):
        return False
    chars=str.strip(chars)#去掉头尾的空白字符 “1    ”也是的，竟然
    #chars.strip()#在python3中，strip函数是str的一个函数，与python2不一样了
    chars_len = len(chars)
    IsNumberToCur=0
    def scan_unsignnumber(i):#
        while(i<chars_len):
            if ord("0")<=ord(chars[i])<=ord("9"):
                i+=1
            else:
                return i
        return i
    def scan_signnumber(i):
        if i<chars_len and chars[i] in ["+","-"]:
            i+=1
        return scan_unsignnumber(i)
    #开始匹配A,
    i=0
    cur_index=scan_signnumber(i)
    IsNumberToCur=(cur_index>i and chars[i:cur_index] not in ["+","-"])
    #这是IsNumberToCur==0标识A并不存在
    if cur_index<chars_len and chars[cur_index]==".":
        cur_index+=1
        temp=cur_index
        cur_index=scan_unsignnumber(temp)
        IsNumberToCur=cur_index>temp or IsNumberToCur
    if cur_index<chars_len and chars[cur_index] in ["e","E"]:
        cur_index+=1
        temp=cur_index
        cur_index=scan_signnumber(temp)
        IsNumberToCur = cur_index > temp and chars[temp:cur_index] not in ["+", "-"] and IsNumberToCur
    return IsNumberToCur and cur_index==chars_len

chars="+3.4e-9"
print(stringIsRepresentNumber(chars))






