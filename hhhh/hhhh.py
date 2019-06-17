import math

import numpy as np
import pandas as pd
from numba import vectorize, jit

pd.options.display.max_columns = None

df_profiles = pd.read_csv(r'./profiles_moderate_importance.csv', nrows=10)
fea_importance = pd.read_csv(r'./fea_importance_by_lgb.csv')
p_fea = ['p' + str(i) for i in range(0, 66)]
fold_1 = fea_importance[fea_importance['fold'] == 1][['feature', 'importance']].set_index('feature').loc[p_fea, :]
fold_2 = fea_importance[fea_importance['fold'] == 2][['feature', 'importance']].set_index('feature').loc[p_fea, :]
fold_3 = fea_importance[fea_importance['fold'] == 3][['feature', 'importance']].set_index('feature').loc[p_fea, :]
fold_4 = fea_importance[fea_importance['fold'] == 4][['feature', 'importance']].set_index('feature').loc[p_fea, :]
fold_5 = fea_importance[fea_importance['fold'] == 5][['feature', 'importance']].set_index('feature').loc[p_fea, :]
df_p_fea = pd.DataFrame(
    pd.concat([fold_1, fold_2, fold_3, fold_4, fold_5], axis=1).apply(lambda x: sum(x) // 5, axis=1))
df_p_fea.rename(columns={0: 'importance'}, inplace=True)
df_p_fea = df_p_fea['importance']
df_p_fea = list(map(lambda x: x / sum(df_p_fea), df_p_fea))
df_pid = list(df_profiles['pid'])
df_p = df_profiles[p_fea]
mode_list = [str(i) + 'mode' for i in range(0, 12)]
df_mode = df_profiles[mode_list]
df_p = df_p.values
df_mode = df_mode.values
p_ans = [[0] * len(df_pid) for i in range(len(df_pid))]
mode_ans = [[0] * len(df_pid) for i in range(len(df_pid))]


@vectorize("int64(float64, float64)",nopython=True, target="parallel")#一定要写上输入类型,而且是64不是32
def create_judge(a, b):
    return 1 if a==b else 0

@vectorize("float64(float64, float64)",nopython=True, target="parallel")#其实这个就相当于applay函数
def create_sim(a, b):
    return a*b
@jit
def starting_exe_p(df_p, p_ans):
    print("starting_comupting_p")
    for k in range(len(df_p)):
        for i in range(k,len(df_p)):
            judge = create_judge(df_p[k], df_p[i])
            p_ans[k][i]=sum(create_sim(judge,df_p_fea))

starting_exe_p(df_p, p_ans)
df_p = pd.DataFrame(p_ans, columns=[*df_pid], index=[*df_pid])
df_p.to_csv(r'./p_matrix.csv')
print("computing_p_end")
@vectorize("float64(float64,float64)",nopython=True,target="parallel")
def com_mode_cha(a,b):
    return abs(a-b)
@jit
def starting_exe_mode(df_mode, mode_ans):
    print("starting_comupting_mode")
    for k in range(len(df_mode)):
        res = []
        if np.isnan(df_mode[k]).any():
            for i in range(k,len(df_mode)):
                if np.isnan(df_mode[i]).any():
                    mode_ans[k][i]=1
                else:
                    mode_ans[k][i] = 0
        else:
            for i in range(k,len(df_mode)):
                if np.isnan(df_mode[i]).any():
                    mode_ans[k][i] = 0
                else:
                    mode_ans[k][i]=math.exp(-sum(com_mode_cha(df_mode[k],df_mode[i]))/ len(df_mode[k]))

starting_exe_mode(df_mode, mode_ans)
df_mode = pd.DataFrame(mode_ans, columns=[*df_pid], index=[*df_pid])
print("computing_mode_end")
df_mode.to_csv(r'./mode_matrix.csv')

# print(sum(df_p_fea[0:7]+df_p_fea[9:26]+[df_p_fea[27]]+df_p_fea[29:36]+df_p_fea[38:48]+\
# df_p_fea[49:59]+df_p_fea[60:63]+df_p_fea[64:66]))
