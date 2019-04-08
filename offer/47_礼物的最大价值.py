"""这题非常的简单，就是DP解法即可，和leetcode 64题类似的，只不过那个是最小，这个是最大"""
def f(grid):
    if not grid or not grid[0]:
        return 0
    grid_values=[[0]*len(grid[0]) for _ in range(len(grid))]
    grid_values[0][0]=grid[0][0]
    for index in range(1,len(grid[0])):
        grid_values[0][index]=grid[0][index]+grid_values[0][index-1]
    for index in range(1,len(grid)):
        grid_values[index][0]=grid[index][0]+grid_values[index-1][0]
    for row_index in range(1,len(grid)):
        for col_index in range(1,len(grid[row_index])):
            grid_values[row_index][col_index]=min(grid_values[row_index][col_index-1],grid_values[row_index-1][col_index])+\
                grid[row_index][col_index]
    return grid_values[-1][-1]

def f_simple(grid):
    if not grid or not grid[0]:
        return 0
    grid_values=[[0]*len(grid[0]) for _ in range(len(grid))]

nums=[[1,3,1],[1,5,1],[4,2,1]]
print(f(nums))
for index in enumerate(nums):
    print(index)
