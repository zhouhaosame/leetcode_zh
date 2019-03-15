import sys
def f(nums):
    min1=[float("inf")]*4
    max1=[float("-inf")]*4
    if len(nums)<3:
        return 1
    if len(nums)<6:
        a=float("-inf")
        for index in range(len(nums)):
            for index1 in range(index+1,len(nums)):
                for index2 in range(index1+1,len(nums)):
                    b=nums[index]*nums[index1]*nums[index2]
                    a=b if b>a else a
        print(a)
    else:
        for item in nums:
            for i in range(0,3):
                if item<min1[i]:
                    min1=(min1[0:i]+[item]+min1[i:])[0:3]
                    break
            for i in range(0,3):
                if item>max1[i]:
                    max1=(max1[0:i]+[item]+max1[i:])[0:3]
                    break
        print(min1)
        print(max1)
        nums=min1+max1
        a=1
        for index in range(len(nums)):
            for index1 in range(index+1,len(nums)):
                for index2 in range(index1+1,len(nums)):
                    b=nums[index]*nums[index1]*nums[index2]
                    a=b if b>a else a
        return a
try:
    count=0
    while True:
        line = sys.stdin.readline().strip()
        if count%2==0:
            count+=1
            continue
        else:
            if line == '':
                break
            lines = list(map(int,line.split()))
            count+=1
            print(f(lines))
except:
    pass


