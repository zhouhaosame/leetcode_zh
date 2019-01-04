def Max_chunks_to_make_sorted(arr):
    left, right = 0, 0
    count = 0
    while (right < len(arr) and left < len(arr)):
        if arr[left] == left:
            left += 1
            count += 1
        else:
            bound = arr[left]
            while (right <= bound):
                if arr[right] > bound:
                    bound = arr[right]
                right += 1
            count += 1
            left = right
    return count
"""这一题的思路就是各找各妈，各回各家。先假设left之前都是已经求过的，bound是
边界，left到right之间的最大值就是right所在位置的索引，left与right之间的所有的
数都是小于那个最大值的。也就是说，这些值都能够在right位置之前找到相应的位置。
然后这一波就确定了"""
#我的方法虽然后两个while，但是时间复杂度也是O(N)

def maxChunksToSorted(arr):#简化的方法
    ans = bound = 0
    for i, x in enumerate(arr):
        bound = max(bound, x)
        if bound == i: ans += 1
    return ans
arr=[1,0,2,3,4]

print(Max_chunks_to_make_sorted(arr))