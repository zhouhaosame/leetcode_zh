def f(nums):
    if not nums:
        return nums
    def find_index_has_one_from_right(number):
        #for i in range(len(binary_number)-1,-1):
        #    if binary_number[i]=="1":
        #        return i

        """上述方式完全是错误的，因为每个binary的长度是不一样的(验证过了)"""
        count=0
        while(number):
            if number&1==1:#这个是取最后一位
                return count
            else:
                number=number>>1
                count+=1
        return count
    def is_one_in_index_i(number,count):
        if number>>count&1==1:
            return True
        else:
            return False
    result_binary=0
    for item in nums:
        result_binary^=item
    count=find_index_has_one_from_right(result_binary)
    a,b=[],[]
    for item in nums:
        if is_one_in_index_i(item,count):
            a.append(item)
        else:
            b.append(item)
    if not a or not b:
        return False
    result=[0,0]
    for index,l in enumerate([a,b]):
        result_binary=0
        for item in l:
            result_binary^=item
        result[index]=result_binary
    return result
"""虽然用到了二进制的操作，但是上下一个bin函数都没有发现"""
nums=[1,2,1,2,100000,4,4,5,7,7]
print(f(nums))
def jinzhizhuanhuan():
    print(bin(3))  # 0b11.注意转换成二进制之后，是str类型的
    print(int(bin(3), 2))  # 3，转化成十进制，要在后面加上参数2，表示前面的是二进制
    print(hex(10))  # 0xa,<class 'str'>也是str类型的
    print(int(hex(10), 16))  # 10，和二进制同理
    print(bin(0xa))  # 16进制转化成二进制
    # 只有int需要加参数的
print(len(bin(3)))
print(bin(3))
print(len(bin(10)))
print(bin(10))
