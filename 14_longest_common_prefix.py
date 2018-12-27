"""
第一种方式horizontal scanning
LCP（s1,s2,s3...sn）=LCP(LCP(LCP(s1,s2),s3)...sn)
这种方式时间复杂度O(m*n)=O(S),S是数组中所有字符的个数
第二种方式
vertical scanning（第一次想的方式）
先比较所有的s的第一个char，然后第二个...
时间复杂度O(m*n)
第三种方式
因为LCP函数只能计算两个的。所以可以将他们分成两个两个一组的（与第一种类似）
！！第四种方式 binary search（二分的方法）。
把最短的分成两份，如果第一份不是common prefix，那么后面的就可以删除不要考虑了。
如果第一份是common prefix，那么第一个就保存下来，然后不需要考虑了
因为需要比较m*n次，使用二分法后，时间复杂度是O(logn*S).
这种是最省时间的
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:#空的数组
        return ""
    str_min,str_min_l,str_min_index,str_num,flag="",len(strs[0]),0,len(strs),0
    for index,value in enumerate(strs):
        if value == "": flag = 1
        if len(value)<str_min_l:
            str_min_l=len(value)
            str_min_index=index
    if flag==1:return ""
    i,i_left,j_right=0,0,str_min_l-1
    while(i_left<=j_right):#二分法肯定要左右相遇
        mid = (i_left + j_right) // 2
        while(i<len(strs)):
            if strs[i][i_left:].startswith(strs[str_min_index][i_left:mid+1]):
                #注意，s[0:1]只取index=0位置的字符，mid+1位置上的字符实际上没有取到
                #s[0,0]表示没有取到
                i+=1
            else:
                if i_left==j_right:return str_min#这一步很关键，当左右相等在，既然出现在zhege
                #地方，说明最后的匹配结束了，没有成功，所以直接返回str_min即可
                j_right=mid#这里可以大胆放心的不怕out of range。因为的确mid位置在
                #这种情况下没必要比较，而且即使out了，内循环结束，也不符合外循环条件了
                break
        if i==len(strs):
            str_min=str_min+strs[str_min_index][i_left:mid+1]
            i_left = mid + 1
        i = 0
    return str_min if str!="" else None
def correct(strs):
    if not strs:#判断是否为空。
        """
        dct,l,str1,l_str,dct_str={},[],"",[""],{"":""}
        if not dct:print("dct为空")
        if not l:print("列表为空")
        if not str1:print("字符串为空")
        if not l_str:print("只包含空字符串的列表")
        if not dct_str:print("字典-只有空字符串为空")
        结果
        dct为空
        列表为空
        字符串为空
        """
        return ""
    shortest = min(strs, key=len)#shorttest只是最短的str
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest
strs=["ab","abd","abgggg"]
print(longestCommonPrefix(strs))
print(correct(strs))
