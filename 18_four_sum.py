#这个可以直接计算N_sum了！！
def four_sum(nums,target):
    def N_sum(nums,target,N,result,results):#这里的result是其中的一个结果
        if len(nums) < N or N < 2 or target<nums[0]*N or target>nums[-1]*N:
            # this reduces ~500ms running time.
            return#不返回任何东西，只是结束它
        if N==2:
            left, right = 0, len(nums) - 1
            while(left<right):
                s=nums[left] + nums[right]
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    results.append(result+[nums[left],nums[right]])
                    while(left<right and nums[right]==nums[right-1]):
                        right-=1
                    while(left<right and nums[left]==nums[left+1]):
                        left+=1
                    right-=1
                    left+=1
        else:#N!=2
            for i in range(len(nums)-N+1):
                if i==0 or (i>0 and nums[i]!=nums[i-1]):
                    N_sum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
                    #这里必须要是result+[nums[i]]，列表才能加上列表
    results=[]
    N_sum(sorted(nums),target,4,[],results)#result里面存的是最终结果，[]里面存的是一组指针对应的数
    #这里的result可以理解成是地址，也可以理解成是全局变量。具体test在“test.py”文件中的"函数中的函数"里面说明
    return results
nums=[1, 0, -1, 0, -2, 2]
print(four_sum(nums,0))


