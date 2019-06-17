# !/usr/bin/env python
# encoding: utf-8
from math import pow
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from numba import jit
#@jit
def matrix_factorization(R,P,Q,K,steps=10000,alpha=0.0002):
    Q=Q.T  # .T操作表示矩阵的转置
    
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j]>=0:
                    eij=R[i][j]-numpy.dot(P[i,:],Q[:,j]) # .dot(P,Q) 表示矩阵内积
                    for k in range(K):
                        temp=P[i][k]
                        temp2=P[j][k]
                        P[i][k]=P[i][k]+alpha*(2*eij*Q[k][j]-2*(P[i][k]-Q[k][i]))
                        Q[k][j]=Q[k][j]+alpha*(2*eij*temp+2*(temp2-Q[k][j]))
        e=0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j]>=0:
                    e=e+pow(R[i][j]-numpy.dot(P[i,:],Q[:,j]),2)
        if step%100==0:
            print("steps is %d"%step)
            print("mse is %d"%e)
        if result[-1]==e and result[-2]==e and result[-3]==e and result[-4]==e and result[-5]==e and \
                result[-6]==e and result[-7]==e:
            break
        result.append(e)
    return P,Q.T

if __name__ == '__main__':
    R=numpy.array([[1,.3,.1,.1],[.3,1,0,.1],[.1,0,1,.5],[.1,.1,.5,1]])
    df=pd.DataFrame([[1],[2],[3],[4]],index = [1,2,3,4])
    #df = pd.read_csv('./df_temp.csv', nrows = 10, index_col = [0])
    df_pid=df.index.values
    #R=df.values
    N=len(R)
    M=len(R[0])
    K=2
    P=numpy.random.randn(N,K) #随机生成一个 N行 K列的矩阵
    Q=numpy.random.randn(M,K) #随机生成一个 M行 K列的矩阵
    result = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
              float('inf')]
    nP,nQ=matrix_factorization(R,P,Q,K)
    df_P=pd.DataFrame(nP,index = df_pid)
    df_Q = pd.DataFrame(nQ, index = df_pid)
    print(df_P)
    print(df_Q)
    df_P.to_csv('./P_MFdata.csv')
    df_Q.to_csv('./Q_MFdata.csv')
    print(result[-1])
    print("原始的评分矩阵R为：\n", R)
    R_MF = numpy.dot(nP, nQ.T)
    print("经过MF算法填充0处评分值后的评分矩阵R_MF为：\n", R_MF)

    # -------------损失函数的收敛曲线图---------------

    n = len(result)
    x = range(n)
    plt.plot(x, result, color = 'r', linewidth = 3)
    plt.title("Convergence curve")
    plt.xlabel("generation")
    plt.ylabel("loss")
    plt.show()