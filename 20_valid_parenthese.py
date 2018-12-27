#很明显，这里面用栈的性质
def validParentheses(s):
    if s:
        list_right=["(","[","{"]
        dct={")":"(","]":'[','}':'{'}
        list_stack,l=list(),len(s)
        for i in range(l):
            if s[i] in list_right:
                list_stack.append(s[i])
            elif list_stack!=[] and dct[s[i]]==list_stack[-1]:
                list_stack.pop()
            else:return False
        return False if list_stack else True
    else:return True
#Python中，False,0,'',[],{},()都可以视为假。
s="]"
print(validParentheses(s))