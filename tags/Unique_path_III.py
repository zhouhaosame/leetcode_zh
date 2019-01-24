def Unique_Paths_III(grid):
    if not grid:
        return 0
    row_len,col_len,ans,ans_num,count_zero=len(grid),len(grid[0]),[],[0],0
    first=[]
    for row in range(len(grid)):
        for x in grid[row]:
            if x==0:
                count_zero+=1
    for row_index,row in enumerate(grid):
        for col_index,col in enumerate(grid[row_index]):
            if col==1:
                first.append((row_index,col_index))
    def backtracking(res,i,j,n,visited):
        if n==count_zero and grid[i][j]==2:
            ans_num[0]+=1
            ans.append(res+[grid[i][j]])
            visited.add((i,j))
        elif n==count_zero:
            return
        elif grid[i][j]==0:
            for (a,b) in [(a,b) for (a,b) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                          if 0<=a<row_len and 0<=b<col_len and (a,b) not in visited]:
                backtracking(res+[(i,j)],a,b,n+1,visited|set([(i,j)]))
    for (i,j) in first:
        for (a, b) in [(a, b) for (a, b) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                       if 0 <= a < row_len and 0 <= b < col_len]:
            backtracking([(i, j)],a,b,0,set())
    return len(ans),ans_num[0]

grid=[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
grid=[[0,1],[2,0]]
print(Unique_Paths_III(grid))


