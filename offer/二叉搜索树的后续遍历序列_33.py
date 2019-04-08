def isPostorder(nums):
    i,j=0,len(nums)-1
    def find_bound_index(start,end,x):
        """这个函数的作用是用来：
        在nums中，从start到end的索引对应的数与x进行比较。然后找到bound
        bound之前的数是小于x的，bound（包括bound）之后的数是大于x的。
        很明显，都大于或者都小于x的情况需要考虑。
        当都大于的时候，bound就是i。从i到j都是大于x的。所以是符合的
        当都小于的时候，bound就是j+1。这个bound是否能使用呢？？"""
        if start>end:
            return -1
        while(start<=end and nums[start]<x):
            start+=1
        bound=start
        while(start<=end and nums[start]>x):
            start+=1
        return -1 if not start>end else bound
    if not nums or len(nums)==1:
        return True
    bound=find_bound_index(i,j-1,nums[j])
    if bound==-1:
        return False
    return isPostorder(nums[i:bound]) and isPostorder(nums[bound:j])
"""如果在某个sub_nums中，都是小于nums[j]的，此时bound其实就是等于j的。这时候说明它没有右子树
正好  nums[bound:j]表示为空。拓展nums[len(nums),k]为空。nums[i:i]为空"""
nums=[5,7,6,9,11,10,8]
nums1=[7,4,6,5]
nums2=[5,7,6,4,2]#root只有右子树
nums3=[5,7,6,4,8]#root只有左子树
nums4=[1,2,3,9,4,8]
print(isPostorder(nums))
print(isPostorder(nums1))
print(isPostorder(nums2))
print(isPostorder(nums3))
print(isPostorder(nums4))