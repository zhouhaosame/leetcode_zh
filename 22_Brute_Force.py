def generateParenthesis(n):
    #递归，要考虑一下东西
    #1、递归的出口（结束条件及操作）
    #可能性1+子递归
    #可能性2+子递归
    #可能性n+子递归
    def generate(A=[]):
        if len(A)==2*n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append("(")
            generate(A)
            A.pop()
            A.append(")")
            generate(A)
            A.pop()#每个可能性的代码是类似的，所以这里一定要加上pop
    def valid(A):
        flag=0
        for i in A:
            if i=="(":flag+=1
            else:flag-=1
            if flag<0:return False###这里一定不要忘记，意思是消消乐之后，)不可能出现在第一个的！！
        return flag==0
    ans=[]
    generate()
    return ans
def correct_backtracking(n):
    #所谓（回溯）Backtracking都是这样的思路：在当前局面下，你有若干种选择。
    # 那么尝试每一种选择。如果已经发现某种选择肯定不行（因为违反了某些限定条件），就返回；
    # 如果某种选择试到最后发现是正确解，就将其加入解集
    #所以你思考递归题时，只要明确三点就行：选择 (Options)，限制 (Restraints)，结束条件 (Termination)。
    # 即“ORT原则”（这个是我自己编的）
    #对于这道题，在任何时刻，你都有两种选择：
    #1.    加左括号。
    #2.    加右括号。
    #同时有以下限制：
    #1.    如果左括号已经用完了，则不能再加左括号了。
    #2.    如果已经出现的右括号和左括号一样多，则不能再加右括号了。因为那样的话新加入的右括号一定无法匹配。
    #(这里右括号用完的条件已经包含在条件二中了，因为右括号用完，根据条件二，左括号也一定用完了，满足条件一)
    #结束条件是：
    #左右括号都已经用完。

    #结束后的正确性：
    #左右括号用完以后，一定是正确解。因为1.左右括号一样多，2.每个右括号都一定有与之配对的左括号。
    # 因此一旦结束就可以加入解集（有时也可能出现结束以后不一定是正确解的情况，这时要多一步判断）。
    ans = []
    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * n:
            ans.append(S)#或者这里去掉else，加上return
        else:
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
    backtrack()
    return ans

def use_reduce(n):#这是使用reduce，先生成所有的可能，再去掉
    def valid(A):
        flag=0
        for i in A:
            if i=="(":flag+=1
            else:flag-=1
            if flag<0:return False###这里一定不要忘记，意思是消消乐之后，)不可能出现在第一个的！！
        return flag==0
    from functools import reduce
    s=[["(",")"]]*2*n#为了迭代，这里初始化一个元素为["(",")"]，长度为2*n的列表
    l_all=reduce(lambda first,second:[a+b for a in first for b in second],s,[""])
    #上一行代码的最后，一定要赋一个初值----[""]。非常注意！！！s和初值都要是列表
    ans=[]
    for i in l_all:
        if valid(i):
            ans.append(i)
    return ans

print(generateParenthesis(4))
print(use_reduce(4))
print(correct_backtracking(4))