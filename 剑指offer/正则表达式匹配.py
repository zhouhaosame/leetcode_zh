# -*- coding:utf-8 -*-
def match(s, p):
    isMatch = [0]
    if not s and not p:
        return True
    if s and not p:
        return False
    def mymatch(i, j):  # i，j之前是匹配的，从i，j开始继续去匹配
        if i >= len(s) and j >= len(p):
            isMatch[0] = 1
        elif j >= len(p):
            return
        else:
            if j + 1 < len(p) and p[j + 1] == "*":
                if i < len(s) and p[j] in [s[i], "."]:
                    mymatch(i + 1, j)
                if not isMatch[0]:
                    mymatch(i, j + 2)
            elif i>=len(s):
                return
            elif p[j] in [s[i], "."]:
                mymatch(i+1,j+1)
    mymatch(0,0)
    return isMatch[0]
a='a'
b='.'
print(match(a,b))
