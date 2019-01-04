def findSubstring(s,words):
    #这是使用滑动窗口的方法
    if not (words and s):return []
    res=[]
    dct=dict(zip(words,[-1]*len(words)))
    word_len,left,right,s_len,word_num,num,i=len(words[0]),0,0,len(s),len(words),0,0
    if False in list(map(lambda x:len(x)==word_len, words)):return []
    while (i<s_len-word_len*word_num+1):
        if not right<s_len-word_len+1:left=right=i
        while (((right-left)/word_len)<word_num and right<s_len-word_len+1):
            #其中left指向窗口的第一个，right指向窗口尾端的下一个
            word_temp=s[right:right+word_len]
            if word_temp in dct:
                if dct[word_temp]<left:
                    dct[word_temp]=right
                    right=right+word_len
                else:
                    left=dct[word_temp]+word_len
                    right=right+word_len
            else:
                right+=word_len
                left=right
        if (right-left)/word_len==word_num:
            res.append(left)
            left=right
        if not right<s_len-word_len+1:i+=1
    return res
"""自己写地稍微有一点问题，主要是words里面可能有两个重复的单词，这样的话怎么能够将它
变成字典呢？？"""



def correct_findSubstring(s, words):
    def _findSubstring(l, r, n, k, t, s, req, ans):
        # 这种方式也是用到了字典的解决方案，看看是怎么用的
        #字典中keys是唯一的，如果将value表示成在words中的索引，那么肯定会重复的
        #因为words中的单词可能并不是唯一的
        #但是这道题目和那个求字符串中最长不重复子串是不一样的，那个里面left<index<right
        #是唯一的，这道题目可以将value看成是字符串的数量
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)
    if not s or not words or not words[0]:
        return []
    n = len(s)
    k = len(words[0])
    t = len(words) * k
    req = {}
    for w in words:
        req[w] = req[w] + 1 if w in req else 1
    ans = []
    for i in range(min(k, n - t + 1)):
        _findSubstring(i, i, n, k, t, s, req, ans)
    return ans
s="wordgoodgoodgoodbestword"
words=["word","good","best","word"]
print(correct_findSubstring(s,words))