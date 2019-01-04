def max_area_of_island(grid):
    if not grid:return 0
    number_res=[[0]*(len(grid[0])+1) for _ in range(len(grid)+1)]
    max_area=0
    for row_index,row in enumerate(grid):
        for col_index,col in enumerate(row):
            if col==1:
                number_res[row_index+1][col_index+1]=number_res[row_index+1][col_index]+number_res[row_index][col_index+1]+1
                max_area=max(number_res[row_index+1][col_index+1],max_area)
    return max_area
#上述这种方法是错误的，因为会出现重复的区域。
#很明显，这个可以一眼看出是一群森林，然后找最大的子树啊！！！
"""从算法上来看，好像是广度优先搜索的，但是其实是对广度和深度理解的错误
所谓深度，与栈结合，所谓广度与队列结合"""
def depth_first_solve(grid):
    if not grid:return 0
    max_count=0
    visited=set()
    stack=[]
    for row_index,row in enumerate(grid):
        for col_index,col in enumerate(row):
            if grid[row_index][col_index]==1 and (row_index,col_index) not in visited:
                visited.add((row_index,col_index))
                stack.append((row_index,col_index))
                sub_count = 1
                while stack:
                    r,c=stack.pop()
                    for cr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                        if 0<=cr<len(grid) and 0<=cc<len(grid[0]) and grid[cr][cc]==1 and (cr,cc) not in visited:
                            visited.add((cr,cc))
                            stack.append((cr,cc))
                            sub_count+=1
                max_count=max(sub_count,max_count)
    return max_count

grid=[
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0]]
print(max_area_of_island(grid))
print(depth_first_solve(grid))
