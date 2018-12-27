def strStr(haystack,needle):
    i,j,l_i,l_j=0,0,len(haystack),len(needle)
    while(i<=l_i-l_j+j and j<l_j):
        #这里范围既然要准确点就不要弄错了
        #当 l_i-i>=l_j-j时，比较才是有意义的
        #幻化过来就是 i<=l_i-l_j+j
        if haystack[i]==needle[j]:
            i+=1
            j+=1
        elif j!=0:
            i=i-j+1#当j归0的时候，i也要改变回去的（到j对齐的下一位）
            j=0
        else:i+=1
    return i-l_j if j==l_j else -1
haystack="mississippi"
needle="issip"
print(strStr(haystack,needle))