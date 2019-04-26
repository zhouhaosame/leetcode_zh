while True:
    try:
        m,_=list(map(int,input().split()))
        n =sorted(list(map(int,input().split())))
        if len(n)<=m:
            print(n[-1])
        else:
            n_list=n[:m]
            min_t=n_list[0]
            ans=0
            for item in n[m:]:
                ans+=min_t
                n_list=[item_1-min_t for item_1 in n[1:]]+[item]
                min_t=n_list[0]
            print(ans+n_list[-1])
    except:
        break

