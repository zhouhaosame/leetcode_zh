def permutation(str):
    import functools
    return functools.reduce(lambda ans,c:[item[0:i]+c+item[i:] for item in ans for i in range(len(item)+1)],str,[""])

def combination(str):
    import functools
    return functools.reduce(lambda ans,c:[item +c for item in ans]+ans,str,[""])
str="abc"
print(permutation(str))
print(combination(str))
#['abc', 'bc', 'ac', 'c', 'ab', 'b', 'a', '']如果不需要''的话，可以直接删掉

