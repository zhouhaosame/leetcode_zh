import heapq
def find_mid_number(nums):
    if not nums:
        return nums
    max_heap,min_heap=[-nums.pop(0)],[]
    count=1
    for item in nums:#大顶堆在左边，小顶堆在右边，小顶堆中存大的数
        count+=1
        if count%2==0 and item<-max_heap[0]:
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
#nums=[1,2,3,4.5,5]
print(sorted(nums))
print(find_mid_number(nums))


#在变态的牛客网中
import heapq
class Solution:
    def __init__(self):
        self.heapq_min,self.heapq_max=[],[]
        self.count=0
    def Insert(self, num):
        if self.count==0:
            heapq.heappush(self.heapq_min,-num)
            self.count+=1
        else:
            self.count+=1
            if self.count%2==0:
                if -num>self.heapq_min[0]:
                    heapq.heappush(self.heapq_max,-heapq.heapreplace(self.heapq_min,-num))
                else:
                    heapq.heappush(self.heapq_max,num)
            else:
                if num>self.heapq_max[0]:
                    heapq.heappush(self.heapq_min,-heapq.heapreplace(self.heapq_max,num))
                else:
                    heapq.heappush(self.heapq_min,-num)
            print(self.heapq_min)
    def GetMedian(self,f):
        return -self.heapq_min[0] if self.count%2!=0 else (-self.heapq_min[0]+self.heapq_max[0])/2.0
    """2.0才是精确除的意思！！！！！！！"""