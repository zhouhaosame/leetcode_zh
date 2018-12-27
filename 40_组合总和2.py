def combinationSum2(candidates,target):
    ans=[]
    candidates.sort()
    def dfs(target,start,res):
        if target==0:
            if res not in ans:
                ans.append(res)
            return
        if start==len(candidates):
            return
        for i in range(start,len(candidates)):
            if candidates[i]>target:
                return
            else:
                dfs(target-candidates[i],i+1,res+[candidates[i]])
    dfs(target,0,[])
    return ans
candidates=[10,1,2,7,6,1]
target=8
print(combinationSum2(candidates,target))