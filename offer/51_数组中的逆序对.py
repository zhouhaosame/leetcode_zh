"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

    对于%50的数据,size<=10^4

    对于%75的数据,size<=10^5

    对于%100的数据,size<=2*10^5
归并排序,
f(nums)
f(nums[前])，f(nums[后])--已经排好序了
merge（f(nums[前])，f(nums[后])）
"""
def f(data):
    if not data:
        return 0
    count=[0]
    def my_merge(data_first, data_second):
        nums=[]
        # 与归并排序不同，这里是一边排序一边记录逆序对
        first_index, second_index = len(data_first) - 1, len(data_second) - 1
        while(first_index>=0 and second_index>=0):
            if data_first[first_index]<=data_second[second_index]:
                nums.append(data_second[second_index])
                second_index-=1
            else:
                nums.append(data_first[first_index])
                count[0]+=second_index+1
                first_index-=1
        if first_index<0:
            nums.extend(data_second[:second_index+1][::-1])
        else:
            nums.extend(data_first[:first_index+1][::-1])
        return nums[::-1]
    def guibing_sort(data):
        if len(data)<=1:
            return data
        else:
            return my_merge(guibing_sort(data[0:len(data)//2]),guibing_sort(data[len(data)//2:]))
    print(guibing_sort(data))
    return count[0]
nums=[7,5,6,4]
print(f(nums))
def f(a,b):
    return a+b
def f(s):
    return s
print(f(1,2))
print(f(3))