while 1:
    try:
        str1=input()
        s1,s2="",[]
        ans=""
        left=["(","[","{"]
        right=[")","]","}"]
        change=0
        for item in str1:
            if "0"<=item<="9" and change==0:
                s2.append(item)
                change=1
            elif "0"<=item<="9" and change:
                s2[-1]=s2[-1]+item
            elif item in left:
                s1=s1+item
                change = 0
            elif item in right:
                divide=s1.rindex(left[right.index(item)])#只有字符串才有rindex
                old_s1=s1
                s1=s1[:divide]
                temp=old_s1[divide:][1:]
                temp=temp*int(s2.pop())
                if len(s1):
                    s1=s1+temp
                else:
                    ans=ans+temp
                change = 0
            else:
                s1=s1+item
                change = 0
        print((ans+s1)[::-1])
    except:
        break
