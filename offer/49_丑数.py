def f(n):
    container=set([1])
    count=1
    number=2
    while(count<n):
        if (number%2==0 and number/2 in container) or (number%3==0 and number/3 in container) or \
                (number%5==0 and number/5 in container):
            count+=1
            container.add(number)
        number+=1
    return number-1
#这个是正确的但是时间超时了！！！！
print(f(9))
def f_new(n):
    nums=[1]
    f2,f3,f5=0,0,0
    while(len(nums)<n):
        while(nums[f2]*2<=nums[-1]):
            f2+=1
        while(nums[f3]*3<=nums[-1]):
            f3+=1
        while(nums[f5]*5<=nums[-1]):
            f5+=1
        nums.append(min(nums[f2]*2,nums[f3]*3,nums[f5]*5))
    return nums[-1]
