def groupAnagrams(strs):
    dct={}
    for index,item in enumerate(strs):
        temp = {}
        for c in item:
            if c not in temp:
                temp.update({c:1})
            else:
                temp[c]+=1
        dct.update({index:temp})
    result,dct=[],list(dct.items())
    while(dct):
        res,temp,index_del=dct[0],[],[]
        for item in dct:
            if item[1]==res[1]:
                temp.append(strs[item[0]])
                index_del.append(item)#extend与append的区别就是extend可以同时添加多个元素
        [dct.remove(item) for item in index_del]
        #如果删除的元素（按照values删除元素，用remove--只会删除第一个元素）在列表中，只能用这种方法删除，不能够
        #直接一下子删除
        result.append(temp)
    """方法是正确的，但是时间超出限制"""
    return result
def correct(strs):
    #list is unhashable
    #tuple is hashable
    import collections
    ans = collections.defaultdict(list)
    """Python中通过Key访问字典，当Key不存在时，会引发‘KeyError’异常。为了避免这种情况的发生，
    可以使用collections类中的defaultdict()方法来为字典提供默认值。
    使用上述的方法创建一个字典时，当字典中没有的键第一次出现时，default_factory自动为其返回一个空列表，list.append()
    会将值添加进新列表；再次遇到相同的键时，list.append()将其它值再添加进该列表。"""
    for s in strs:
        ans[tuple(sorted(s))].append(s)#list时unhashable，所以不能够时key，而tuple时hashable
    return list(ans.values())
#10%
def fastest(strs):
    import collections
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1#ord，返回相应的ascii值
        ans[tuple(count)].append(s)
    return list(ans.values())
"""之所以这个比correct快，是因为correct中有一个sorted函数，其时间复杂度是KlogK"""
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
print(correct(strs))
print(fastest(strs))