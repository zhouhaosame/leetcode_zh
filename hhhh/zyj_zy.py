# encoding: utf-8
__author__ = 'Scarlett'
import matplotlib.pyplot as plt
from math import pow
import pandas as pd
min_err=1e-15
import numpy
def matrix_factorization(R,P,K,steps=5000):
    for step in range(steps):
        estimate_R=P*(P.T)
        E=R-estimate_R
        err=0
        for i in range(len(R)):
            for j in range(len(R[i])):
                err+=E[i,j]*E[i,j]
        print(err)
        #if err<min_err:
        #    break
        a = P.T * R
        b = P.T * P * P.T
        for i_1 in range(K):
            for j_1 in range(len(R[0])):
                if b[i_1, j_1] != 0:
                    (P.T)[i_1, j_1] = (P.T)[i_1, j_1] * a[i_1, j_1] / b[i_1, j_1]

        c = R * P
        d = P * P.T * P
        for i_2 in range(len(R)):
            for j_2 in range(K):
                if d[i_2, j_2] != 0:
                    P[i_2, j_2] = P[i_2, j_2] * c[i_2, j_2] / d[i_2, j_2]
        
    return P

if __name__ == '__main__':
    R=[
        [1,0.6,0.9,0.7],
        [0.6,1,0.4,0.7],
        [0.9,0.4,1,0.8],
        [0.7,0.7,0.8,1],
    ]
    #df=pd.read_csv('./df_temp.csv',nrows=10,index_col=[0])
    R=numpy.mat(R)
    N=len(R)
    M=len(R[0])
    K=1
    P=numpy.mat(numpy.random.random((N,K)))
    nP=matrix_factorization(R,P,K)
    print("原始的评分矩阵R为：\n",R)
    R_MF=nP*nP.T
    print("经过MF算法填充0处评分值后的评分矩阵R_MF为：\n",R_MF)
