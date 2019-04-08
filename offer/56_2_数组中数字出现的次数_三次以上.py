def f(nums):
    """3>>1，得1.
    -3>>1,得-2.
    对待复数我们要先将他变成正数，一块统计"""
    binary_nums=[0]*65#第一位是符号位
    def update_binary_nums(number):
        if number<0:
            binary_nums[0]+=1
            number=abs(number)
        index=len(binary_nums)-1
        while(number):
            if number&1==1:
                binary_nums[index]+=1
            index -= 1
            number = number >> 1
    for item in nums:
        update_binary_nums(item)
    for index,item in enumerate(binary_nums):
        binary_nums[index]=item%3
    flag="-" if binary_nums[0]==1 else "+"
    number=flag+"0b"+"".join(list(map(str,binary_nums[1:])))
    return int(number,2)
nums=[-1,-1,-1,2,3,3,3,4,2,2,4,4,6,7,7,7]
print(f(nums))
print(bin(-3))
print(-3>>1)
print(3>>1)
print(bin(-2))


