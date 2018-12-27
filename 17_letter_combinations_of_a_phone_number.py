def letterCombinations(digits):
    dct={"2":"abc","3":"def","4":"ghi","5":"jkl","6":'mno',"7":'pqrs',"8":"tuv","9":"wxyz"}
    result,l,i=[],len(digits),1
    if digits=="":return []
    for j in range(len(dct[digits[0]])):
        result.append(dct[digits[0]][j])
    while(i<l):
        result_temp=[]
        for j in range(len(dct[digits[i]])):
            for item in result:
                item=item+dct[digits[i]][j]
                result_temp.append(item)
        result=result_temp
        i+=1
    return result
s="23"
def correct(digits):
    from functools import reduce
    dct = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": 'mno', "7": 'pqrs', "8": "tuv", "9": "wxyz"}
    if digits == "": return []
    #函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第
    # 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
    #print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5],1))#表示1+2+3+4+5+1最后的1是初始参数
    #这个初始化1的意思是，将初始化的1和列表中的第一个作为函数的前两个输入
    return reduce(lambda acc, digit: [x + y for x in acc for y in dct[digit]], digits, [''])
    #这里必要要初始化[""]
print(letterCombinations(s))
print(correct(s))
