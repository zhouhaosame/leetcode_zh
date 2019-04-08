def bag(n, c, w, v):#普通的方法就是填二维数组
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    # for x in value:
    #     print(x)
    return value[-1][-1]

def using_jump_point(n,c,w,v):
    def merge_my(p,q):
        temp=p+q
        temp.sort(key=lambda x:x[0])
        for i in range(len(temp)-1):
            if temp[i]:
                for j in range(i+1,len(temp)):
                    if temp[j] and temp[j][1]<=temp[i][1]:
                        temp[j]=None
        return [item for item in temp if item]
    p=[(0,0)]
    for i in range(n):
        q=[(x+w[i],y+v[i]) for (x,y) in p if x+w[i]<=c]
        p=merge_my(p,q)
    ans=float("-inf")
    for item in p:
        if item[1]>ans:
            ans=item[1]
    return ans
n = 4
c = 8
w = [2, 2, 4, 1]
v = [2, 3, 7, 5]
print(bag(n,c,w,v))
print(using_jump_point(n,c,w,v))
