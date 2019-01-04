"""关于next_permutation以及pre_permutation
next_permutation
是一个从升序到降序的过程，下一个序列的求法。
1、从右到左，找到第一个不满足左边大于右边的位置
（不满足升序的位置--从左到右就是降序啦），计为i，s[i]<s[i+1]。i位置之后从左到右都是满足降序的
2、再从右到左，找到第一个大于s[i]的位置j，s[i]<s[j]且s[i]>s[j+1]
3、交换i和j的内容，然后再将i位置后面逆序reverse。
pre_permutation
是一个降序到升序的过程。相当于下一个序列的求法。
1、从右到左，找到第一个不满足降序的位置，即为i，s[i]>s[j].i位置之后都是从左到右都是满足升序的。
2、从右到左，找到第一个小于i位置的元素
3、交换i和j的内容，然后再将i位置后面的元素逆序
"""
def nextPermutation(nums):
    def swap(i,j):
        """
        x=x+y
        y=x-y
        x=x-y
        如果使用这种方法，很可能会出现溢出的问题，所以要使用异或的二进制的方式
        
        x=x^y
        y=x^y
        x=x^y
        这种方式其实是把值传到了x,y里面，然后x,y交换，并没有对列表的数据进行修改
        所以要传进去列表的位置
        """
        nums[i] = nums[i] ^ nums[j]
        nums[j] = nums[i] ^ nums[j]
        nums[i] = nums[i] ^ nums[j]
        #return x,y
        #加了返回就不是inplace了，去掉返回+修改的列表中的元素。所以相当于传入的地址
        #能够直接修改作为全局变量的列表元素
    def reverse_in_place(i):
        j=len(nums)-1
        while(i<j):
            swap(i,j)
            i+=1
            j-=1
    if not nums:return None
    i,j,nums_len=len(nums)-1,len(nums)-1,len(nums)

    while(j>0):
        if nums[j]<=nums[j-1]:
            j-=1
        else:break
    j-=1
    if j==-1:return
    while(i>j):
        if nums[i]<=nums[j]:#样例[1,5,1]，说明里面可能有重复的数，所以要小于等于
            i-=1
        else:break
    swap(i,j)
    reverse_in_place(j+1)
    print(nums)

s=[1,1]
nextPermutation(s)
