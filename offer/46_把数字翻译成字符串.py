"""这个题很容易想到就是每个词一个台阶，然后一个人跳台阶。台阶之间的词段就是
一个字符。这样的话，遇到0怎么办呢，1101只有一个，这样的话res的下一个如果是0呢，0肯定要加在前面的，
那么到时候还需要在判断一下

leetcode上的，A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
是从1对应A的。"""
def f(n):
    n_len=len(n)
    ans=[]
    def back_tracking(res,i):
        if i>=n_len:
            ans.append(res)
            return#一定要加上return。要不然会向下执行判断从而出现index问题
        if n[i]=="0":
            return
        #当前面是res的时候，意味着正确的res，然后当下是0的时候，排除
        else:
            back_tracking(res+[n[i]],i+1)
            if i+1<len(n) and n[i:i+2]<="26":
                back_tracking(res+[n[i:i+2]],i+2)
    back_tracking([],0)
    return ans
"""正确的，但是内存超了，超了肯定是因为里面保存的是具体的词段，leetcode上只是要求返回数量，可以计数即可"""
n=226
print(f(str(n)))

