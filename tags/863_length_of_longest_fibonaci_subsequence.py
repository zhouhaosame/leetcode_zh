import numpy as pd
#暴力法，因为斐波那契数列有一个特点，那就是只要给出任意两个最前面的数，就下来所有的数就都是固定的了
def force_brute(A):
    l,ans=len(A),0
    if len(A)<2:return 0
    A_dct=dict.fromkeys(A,0)
    for i in range(len(A)):
        for j in range(i+1,l):
            temp,flag,count,pre,post=A[i]+A[j],0,0,A[i],A[j]
            while(temp in A_dct):
                flag=1
                count+=1
                pre,post=post,temp
                temp=pre+post
            if flag==1:count+=2
            ans=max(ans,count)
    return ans
#我自己写的竟然超时了，同样是暴力法,而且提供的solution也是超时的


#动态规划是标准的，类似求最长上升序列，这里关键点在于当前的值能够通过之前的两个得到。看代码更容易理解
def dynamic_program(A):
    #关键点在于使用字典去记录index的连接（在图中也可以这样表示）
    import collections
    ans=0
    dct=collections.defaultdict(lambda:2)
    index_list=[i for i in range(len(A))]
    search_dct=dict(zip(A,index_list))
    for index,value in enumerate(A):
        for i in range(index):
            pre_pre_index=search_dct.get(value-A[i],-1)#如果指定键的值不存在时，返回该默认值=None。
            if pre_pre_index>=0 and i>pre_pre_index:
                dct[(i,index)]=dct[(pre_pre_index,i)]+1
                ans=max(dct[(i,index)],ans)
    return ans
#40%

A=[3,5,7,8,11]
print(force_brute(A))
print(dynamic_program(A))