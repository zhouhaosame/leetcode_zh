def solveNQueens(n):
    import copy
    ans=[]
    canditates_set=set([i for i in range(0,n)])
    def find_candidates(i,res):
        temp=[]
        canditates_set_sub=canditates_set^(set(res))
        for item in canditates_set_sub:
            count=-1
            for row,col in enumerate(res):
                if i-item==row-col or i+item==row+col:
                    break
                else:
                    count = row
            if count==len(res)-1:temp.append(item)
        return temp
    def search(i,res):
        if len(res)==n:
            ans.append(copy.deepcopy(res))
            return
        candidates=find_candidates(i,res)
        if not candidates:
            return
        for item in candidates:
            search(i+1,res+[item])
    search(0,[])
    ans_1=[]
    for i in ans:
        temp=[]
        for row,col in enumerate(i):
            temp.append('.'*col+'Q'+'.'*(n-col-1))#字符串时不可变对象，不能直接通过下标的方式进行修改
        ans_1.append(copy.deepcopy(temp))
    return ans_1

n=4
print(solveNQueens(n))