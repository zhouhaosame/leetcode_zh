def jump(nums):
    jump_min=[len(nums)-1]*len(nums)
    jump_min[0]=0
    for i in range(len(nums)-1):
        for j in range(1,min(nums[i],len(nums)-i)+1):
            jump_min[i+j]=min(jump_min[i]+1,jump_min[i+j])
    return jump_min[len(nums)-1]
"""这样虽然是对的，但是时间是超时的，所以肯定有别的方式"""

def BFS(nums):
    if not nums:
        return False
    left,right,count=0,0,0
    while(right<len(nums)-1):
        left_new=right+1
        right=max(list(map(lambda x:x+nums[x],range(left,right+1))))
        left=left_new
        count+=1
    return count
    """以第一个元素为根节点，这个可以转化成一个BFS的格式，每一层都代表着一步，一步中包含着该步的所有可能"""



nums=[2,1]
print(BFS(nums))