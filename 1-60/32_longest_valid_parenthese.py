def longestValidParentheses(s):#暴力法肯定超时
    if not s:return 0
    longest_l,i,bar,s_len=0,0,0,len(s)
    while(i<s_len-longest_l+1):
        j=i
        while(bar>=0 and j<s_len):
            if s[j]=="(":bar+=1
            else:
                bar-=1
            if bar==0 and longest_l<j-i+1:
                longest_l=j-i+1
            j+=1
        i+=1
        bar=0
    return longest_l

def uesing_stack(s):
    if not s:return 0
    stack,i,s_len=[-1],0,len(s)
    while(i<s_len):
        if s[i]=="(":
            stack.append(i)
        elif stack[-1]!=-1 and s[stack[-1]]=="(":
            stack.pop()
        else:
            stack.append(i)
        i+=1
    longest=0
    if len(stack) == 1: return s_len
    stack[0]=-1 if s[1]!=0 else 0
    if stack[-1]!=s_len-1:
        stack.append(s_len)#这里要看一下边界，也就是第一个和最后一个括号有没有被用到
    stack_len=len(stack)

    for i in range(stack_len-1,0,-1):
        if longest<stack[i]-stack[i-1]-1:
            longest=stack[i]-stack[i-1]-1
    return longest
s=")()())()()("
#print(longestValidParentheses(s))
print(uesing_stack(s))