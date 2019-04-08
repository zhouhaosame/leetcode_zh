"""按理说在别的语言会有大的值溢出的问题，但是在python里是没有的
，但是还是要算一下"""
def print_1_Nnumber(n):
    """因为每个位置都有10中选择0-9.所以一种方式是
    先将第n-1位赋值为0-9.然后递归生成0-（n-2）位置上的所有可能"""
    ans=[]
    if n==0:
        return 0
    def create_N(res,index):#这样的话，也算是回溯的一种了
        if index==n:
            ans.append(res)
        else:
            for i in range(0,10):
                create_N(res+chr(ord("0")+i),index+1)
    create_N("",0)
    return ans

def using_reduce(n):
    import functools
    ans=functools.reduce(lambda res_list,n_list:[res+chr(ord("0")+i) for res in res_list for i in n_list],
                         [[x for x in range(0,10)]]*n,[""])
    return ans
print(print_1_Nnumber(0))
print(print_1_Nnumber(5))
print(using_reduce(0))
print(using_reduce(5))
#print([[x for x in range(0,10)]]*5)
#print([None] * 5)#[None, None, None, None, None]
#print([[None]*5])#[[None, None, None, None, None]]
#print([[None]]*5)#[[None], [None], [None], [None], [None]]

def print_my(ans):
    return
#打印很简单，从第一个不为0的开始。可以设置一个isstart表示出现的0是否在
#开头


