while 1:
    try:
        n,m=list(map(int,input().split()))
        p_1=[]
        for _ in range(n):
            p_1.append(list(map(int,input().split())))
        x1,y1,x2,y2=list(map(int,input().split()))
        ans=[0]
        def find_path(res,i,j,visited):
            if i==x2 and j==y2:
                ans[0]+=1
                return
            for (q,p) in [(q,p) for (q,p) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] \
                          if 0<=q<n and 0<=p<m and (q,p) not in visited and p_1[q][p]>=p_1[i][j]]:
                find_path(res+[(i,j)],q,p,visited|set([(i,j)]))
        find_path([],x1,y1,set())
        print(ans[0]%(10**9))
    except:
        break
"""
4 5
0 1 0 0 0
0 2 3 0 0
0 0 4 5 0
0 0 7 6 0
0 1 3 2

"""