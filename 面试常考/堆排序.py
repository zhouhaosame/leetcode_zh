"""先写上堆排序"""
def heap_sort(nums):
    #以堆的思想进行排序，因为我们是想从1进行编号，所以可以在nums的前面添加一个0
    nums=[0]+nums
    def heap_adjust(root_index,end):
        #进行堆的调整的时候，除了root节点是新插入的，root的左右子树都是满足堆的性质的
        temp=nums[root_index]
        i=root_index
        j=i*2#先看左子树的节点
        while(j<=end):
            if j<end and nums[j]<nums[j+1]:
                j+=1#取左右孩子较大的那个位置
            if temp<nums[j]:
                nums[i]=nums[j]
                i=j
                j=2*i
            else:
                break
        nums[i]=temp#这样的话，root节点到了它应该在的位置
        """一定要注意，这里我们认为除了root_index以外，root的左右子树都是满足大顶堆的性质的"""
        """
        a=[1,2]
        a[0],a[1]=a[1],a[0]
        print(a)
        """
    def heap_sort(nums):
        index_HasChildren=(len(nums)-1)//2
        #从1开始，到index_HasChildren，他们都是有孩子节点的
        #堆是从下往上，从右往左开始调整的，正好是nums中的逆序
        for i in range(index_HasChildren,0,-1):
            heap_adjust(i,len(nums)-1)
        #这样的话，现在nums就是一个大顶堆啦
        for i in range(len(nums)-1,1,-1):#当最后只剩下一个就不需要再算了
            #因为index=1的位置存的是堆顶，所以每次要和“最后”一个交换
            nums[i],nums[1]=nums[1],nums[i]
            heap_adjust(1,i-1)
        return nums[1:]
    return heap_sort(nums)
import random
nums=[random.randint(1,100) for _ in range(20)]
print(heap_sort(nums))
#https://www.jianshu.com/p/d174f1862601
