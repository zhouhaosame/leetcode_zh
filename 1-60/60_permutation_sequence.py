def getPermutation(n,k):
    from functools import reduce
    n_list=[str(i) for i in range(1,n+1)]
    n_list="".join(n_list)#如果是n_list=" ".join(n_list)。这里" "里面是有空格的，则生成的字符串之间都是有空格的
    #permutations=reduce([lambda s,c:p[:i]+c+p[i:] for i in range(len(p)) for p in s],n_list,[])
    #生成全排列注意点
    permutations = reduce(lambda s, c: [p[:i] + c + p[i:] for p in s for i in range(len(p)+1)], n_list, [""])
    """1、n_list要先转换成字符串
       2、lambda函数的函数体用[]扩住，而不是整个lambda用[]扩住
       3、for i in range(len(p)+1),这里是最重要的。因为必须要len(p)+1，如果不+1，则最后只会生成[],因为刚开始跳不出""
       4、然后n_list, [""]，也重要的[""]里面必须有一个初始化的“”，要不然进不去for p in s 
       """
    permutations.sort(key=lambda x:x)
    return permutations[k-1]
"""这样虽然正确但是时间是远远超出的"""

def test_2(n,k):
    """这里的思想是，先生成一个n_list，有序，然后用k整除n-1的阶乘，这样就知道了
    k应该掉落在那个字符开头的permutations，然后%n-1的阶乘，表示的在这个permutations中
    的位置，如果j==0，这就意味着到了这个permutations集合的最后一个了，在当前n_list[n-1]之后的
    都已经排好序了，是逆序的
    """
    from functools import reduce
    n_list = [str(i) for i in range(1, n + 1)]
    result=""
    while(n_list):
        num=reduce(lambda a,b:a*b,[x for x in range(1,len(n_list))],1)
        i=k//num
        j=k%num
        if j == 0:
            result = result + n_list[i-1]
            n_list.pop(i-1)
            result=result+"".join(n_list[::-1])
            return result
        result=result+n_list[i]
        n_list.pop(i)
        k=j

n=2
k=2
#getPermutation(n,k)
print(test_2(n,k))