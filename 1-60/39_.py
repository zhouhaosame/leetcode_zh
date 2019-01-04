def combinationSum(candidates, target):
    if not candidates:return False
    ans = []
    candidates.sort()
    def find_candidates(target, start, res):
        #这个函数的含义是，已经在0-start-1内找到了和为target_raw-target的可能组合，其中res是一种可能组合，接下来就是从
        #start-len(candidates)-1找到目标值为target，前段为res的所有组合，最后判断是否能够加入ans
        if target==0:#题目要求了target是==0的，也就是说当成立的时候，res中存的就是一个可能集合
            ans.append(res)
            return
        if start==len(candidates):
            return
        #这是一个出口，就是说当找到最后，target都不为0，就是说这种可能结束，return
        for i in range(start,len(candidates)):#在start到len(candidates)-1之间先找一个数，加入res，继续递归
            if candidates[i]>target:#当前i位置大于目标值，因为是升序，所以i之后所有的值都是大于target的，
                #这种情况下，说明这种可能可以提前直接结束了，可以用continue，一步步结束for循环，更快的是用return，直接
                #一步就退出这种start开始的所有可能
                #continue
                return
            else:
                find_candidates(target-candidates[i],i,res+[candidates[i]])
                #一种可能执行后，target和res都没有变
                """
                res.append(candidates[i])
                find_candidates(target-candidates[i],i,res)
                res.pop()
                这种方法是错误的，res append一个值，ans.append(res)后ans改变，但是当res pop之后，ans里面的值也相应的pop了
                一种解决方法是向上面的那种，find_candidates(target-candidates[i],i,res+[candidates[i]])，不改变target，res的
                状态，另一种是ans.append(copy.deepcopy(res)),深度拷贝
                """
    find_candidates(target,0,[])
    return ans
can=[2,3,5]
target=8
print(combinationSum(can,target))