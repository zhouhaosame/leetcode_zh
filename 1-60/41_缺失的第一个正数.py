def firstMissingPositive(nums):
    pre_list,post_list,nums=set(),set(),nums+[0]
    for i in nums:
        post_list.add(i+1)
        pre_list.add(i)
    result=min([x for x in list(post_list-pre_list) if x >0])
    return result
"""
a = t | s          # t 和 s的并集

b = t & s          # t 和 s的交集

c = t – s          # 求差集（项在t中，但不在s中）

d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）"""
nums=[-5,10]
print(firstMissingPositive(nums))


