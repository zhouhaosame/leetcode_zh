"""关于shell排序
shell排序本质上也是插入排序
由于开始时，increment的取值较大，每个子序列中的元素较少，排序速度较快，
到排序后期increment取值逐渐变小，子序列中
元素个数逐渐增多，但由于前面工作的基础，大多数元素已经基本有序，
所以排序速度仍然很快。
增量increment的取法有各种方案。最初shell提出取increment=n/2向下取整，
increment=increment/2向下取整，直到increment=1。但由于直到最后一步，
在奇数位置的元素才会与偶数位置的元素进行比较，
这样使用这个序列的效率会很低。后来Knuth提出取increment=n/3向下取整+1.
还有人提出都取奇数为好，也有人提出increment互质为好。
应用不同的序列会使希尔排序算法的性能有很大的差异。
希尔排序是一种不稳定的排序算法。
时间复杂度是n^1.3 ，不管增量序列如何取值，都应该满足最后一个增量值为1.
"""
def shell_sort(nums):
    increment=len(nums)//3+1#增量从这个开始
    def insert_sort(start,increment):
        #以start开始，increment为增量
        for i in range(start+increment,len(nums),increment):
            for j in range(start,i,increment):
                if nums[j]>nums[i]:#查找
                    temp=nums[i]
                    for k in range(i,j,-1):#移动
                        nums[k]=nums[k-1]
                    nums[j]=temp
    while(increment>=1):
        for start in range(0,increment):
            insert_sort(start,increment)
        increment=increment//3+1 if increment>1 else 0
    return nums
import random
nums=[random.randint(1,100) for _ in range(1,20)]
print(shell_sort(nums))

a="123"
b="3456"
print(id(a))
print(id(b))
a,b=b,a
print(a)
print(id(a))
"""
2252629939176
2252629939344
3456
2252629939344
"""
a=[1,2,3,4,5]
print(id(a))
print(id(a[1]))
b=[0,9]
a[1:3]=b
print(a)
print(id(a))
print(id(a[1]))
"""
1351816794440
1565352128
[1, 0, 9, 4, 5]
1351816794440
1565352064
真的就是直接改变了啊，list的首地址是不变的，
因为list中存的都是引用，指向不同的地方
然后切片修改了之后，相应的引用方向也改变啦
"""
a[2:3]=b
print(a)#[1, 0, 0, 9, 4, 5]
print(id(a[1]))
print(id(a[2]))