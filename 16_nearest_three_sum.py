def nearest_3_sum(nums,target):
    nums.sort()
    i,sum_closest,sum_error,l=0,sum(nums[0:3]),abs(target-sum(nums[0:3])),len(nums)
    for i in range(l-2):
        start,end=i+1,l-1
        while(start<end):
            if i>0 and nums[i]==nums[i-1]:
                break
            sum_temp=target - nums[i] - nums[start] - nums[end]
            if abs(sum_temp)>=sum_error:
                if sum_temp<0:
                    end-=1
                elif sum_temp>0:
                    start+=1
                else:return nums[i] + nums[start] + nums[end]
            else:
                sum_closest= nums[i] + nums[start] + nums[end]
                sum_error=abs(sum_temp)
                while start<end and nums[start]==nums[start+1]:
                    start+=1
                while start<end and nums[end]==nums[end-1]:
                    end-=1
                #start += 1
                #end -= 1
                if sum_closest>target:
                    end-=1
                elif sum_closest<target:
                    start+=1
                #这个地方和之前的三数相加==0不一样。因为在==0的情况下，对于g,i,i+1,i+2
                #当g+（i）+（i+2）==0且i+1和两边不等的时候，此时g+（i）+（i+1）！=0且
                #g+（i+1）+（i+2）！=0，然后start和end同时改变即可
                #但是在closeest的情况下，比如（-3，0，1，2）,target=1。先-3，0，2=1
                #比初值-3，0，2=-1更靠近，然后如果都改变的话，1就考虑不到了，-3，1，2=0，、
                #很明显这个才是正确答案
                ##!!!!还有个知识点，就是如果在这个地方选错了怎么办，那岂不是永远找不到最合适的
                #一组了？？是的。因为既然制定了原则（和container那题一样），就要从头到尾的
                #遵守，半路更换，当然不合适
    return sum_closest

nums=[0,2,1,-3]
target=1
print(nearest_3_sum(nums,target))

