def subarray_to_sum(tsum):
    ans,res=[],[tsum-1,tsum-2]
    while(res[-1]>0):
        temp_sum=sum(res)
        """当然这里可以使用一个小技巧，就是用一个sum_new去保存滑动窗口的sum"""
        if temp_sum>tsum:
            res=list(map(lambda a:a-1,res))
        elif temp_sum<tsum:
            res.append(res[-1]-1)
        else:
            ans.append(res[::-1])
            res = list(map(lambda a: a - 1, res))
    return sorted(ans)
print(subarray_to_sum(15))
