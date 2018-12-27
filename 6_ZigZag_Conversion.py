def convert(s,numRows):
    l=""#不能用列表，要用字符串。不过如果使用列表，列表转字符串是 ：str="".jion(list)。
    length=len(s)
    if numRows>=length or numRows==1:return s#这一行一定要加！！当numrows=1时下面的规律不成立
    for number in range(1,numRows+1):
        num_index = number-1
        l=l+s[num_index]
        while(num_index<length):#因为循环中有两种不同的趋势，虽然这两种趋势结合满足一个周期，但是无法直接用两种来判
            # 断，因为可能只有一个在后面出现，所以在循环内分成两种
            num_index += 2 * (numRows - number)
            if num_index<length:
                if(numRows - number):l=l+s[num_index]
                num_index += 2 * (number-1)
                if num_index < length:
                    if(number-1):l=l+s[num_index]
    return l
s="AB"
print(convert(s,1))