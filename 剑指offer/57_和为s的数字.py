def FindNumberWithSum(array,tsum):
    left,right=0,len(array)-1
    while(left<=right):
        temp=array[left]+array[right]
        if temp==tsum:
            return array[left],array[right]
        elif temp<tsum:
            left+=1
        else:
            right-=1
    return []
array=[1,2,4,7,10,19]
print(FindNumberWithSum(array,14))
