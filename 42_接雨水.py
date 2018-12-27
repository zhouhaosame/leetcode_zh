def trap(height):
    left,right,c=0,0,0
    def computing(left,right):
        #计算水的体积
        min=height[left] if height[left]<height[right] else height[right]
        return max(0,min*(right-left-1)-sum(height[left+1:right]))
    def find_right_for_left(left):
        #找到第一个大于left的right，如果找不到，那就说明left后面的所有都是小于right的，则找最大的right
        right=left+1
        max=right
        while(right<len(height)):
            if height[right]>=height[left]:
                break
            else:
                if height[right]>height[max]:
                    max=right
                right+=1
        return max if right==len(height) else right
    while(left<len(height)-2 and right<len(height)):
        right=find_right_for_left(left)
        c+=computing(left,right)
        left=right
    return c
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))



