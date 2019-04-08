def f(s):
    if not s:
        return 0
    dct={}
    max_len=0
    for index,item in enumerate(s):
        if item not in dct:
            dct.update({item:index})
        else:
            max_len=max(max_len,len(dct))
            dct=dict([(value,index+dct.get(item)+1) for index,value in enumerate(s[dct.get(item)+1:index+1])])
            ###
            """这一行非常的重要，错了两次了
            首先是----dct=dict([(item,index) for index,item in enumerate(s[dct.get(item)+1:index+1])])
            这样错误的原因是，我的本意是index是在s中的索引，但是这里明显是在s[dct.get(item)+1:index+1])]中的索引
            然后我改成了
            dct=dict([(item,index+dct.get(item)+1) for index,item in enumerate(s[dct.get(item)+1:index+1])])
            结果还是出错了。dct.get(item)+1我想找的是重复的那个c在s中的索引，但是里面我有重新定义了item.当然会有问题啊！！！
            """
    return max(max_len,len(dct))
#我的这个还是太慢了，主要是存储结构选的不好，为什么要用字典呢？
#看看人家的
def lengthOfLongestSubstring(self, s: 'str') -> 'int':
    sub = ''
    res = ''
    for i in s:
        if i not in sub:
            sub += i
        else:
            if len(res) <= len(sub):
                res = sub
            sub = sub.split(i)[-1] + i
    return max(len(res), len(sub))

print(f("bpfbhmipx"))
