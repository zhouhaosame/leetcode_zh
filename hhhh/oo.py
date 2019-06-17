import numpy as np
import pandas as pd
a=[1,2,3]
b=[[2,3],[6,7],[9,0]]
m=[[1,3,8],[5,5,0],[7,7,0]]
k=pd.DataFrame(b,columns = ['2','o'])
t=pd.DataFrame(a,columns = ['i'])
t=t.join(k)
r=pd.DataFrame(m,columns=['i','o','p'])
print(r)
t=t.merge(r,how = "left",on=['i','o'])
a=set([(3,4)])
print(a)
a.add((1,2))
hh=pd.DataFrame(list(a),columns = ['1','3'])
print(hh)



