import heapq
def find_mid_number(nums):
    if not nums:
        return nums
    max_heap,min_heap=[-nums.pop()],[]
    count=1
    for item in nums:
        count+=1
        if count%2==0 and -item>max_heap[0]:
            heapq.heappush(min_heap,-heapq.heapreplace(max_heap,-item))
        elif count%2==0:
            heapq.heappush(min_heap,item)
        elif item>min_heap[0]:
            heapq.heappush(max_heap, -heapq.heapreplace(min_heap, item))
        else:
            heapq.heappush(max_heap,-item)
    if count%2==0:
        return (-heapq.heappop(max_heap)+heapq.heappop(min_heap))/2
    else:
        return -heapq.heappop(max_heap)
nums=[1,2,3,5,6,-3,4,0,3,1,9,9,9]
nums=[1,2,3,4.5,5]
print(sorted(nums))
print(find_mid_number(nums))