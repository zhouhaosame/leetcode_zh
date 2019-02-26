import heapq
nums=[1,2,3,4,-3,5,6,3,4,5,6,76,87,4,5,63,3,2,6,6,3]
print(heapq.nsmallest(3,nums))

def get_least_numbers_big_data(nums, k):
    heap = []
    length = len(nums)
    if not nums or k <= 0 or k > length:
        return
    for item in nums:
        item = -item
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif item>heap[0]:#这行代码其实是最重要的。
            heapq.heapreplace(heap, item)
            #用item去替换最小堆的最小值，也就是root节点
    return list(map(lambda x:-x, heap))
    """这里又一个很大的误导，就是虽然求的是最小的k个，使用最大堆，但是python中没有最大堆，因为用加负号的方式，用
    最小堆来表示“最大堆”。
    但是真的就是“最大堆”吗？
    """
print(get_least_numbers_big_data(nums,3))