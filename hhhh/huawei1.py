while 1:
    try:
        n=int(input())
        str1=[]
        for _ in range(n):
            str1.append(input())
        count=0
        ans=[]
        for item in str1:
            for i in range(0,len(item),8):
                ans.append(item[i:i+8])
            while(len(ans[-1])<8):
                ans[-1]=ans[-1]+"0"
        print(" ".join(sorted(ans)))
    except:
        break