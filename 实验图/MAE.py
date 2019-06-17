import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_axis = [20,40,60,80,100]

rf = [184,174,166,159,157.5]
anns = [186,179,170,164,161]
adaboost = [187.5,176,172,163,162]


x = np.arange(len(x_axis))  #首先用第一个的长度作为横坐标
width = 0.2   #设置柱与柱之间的宽度
fig,ax = plt.subplots()
p_rf = ax.bar(x-width,rf,width,alpha = 0.9,)
p_anns = ax.bar(x,anns,width,alpha = 0.9,color= 'red')
p_adaboost = ax.bar(x+width,adaboost,width,alpha = 0.9,color= 'green')
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x_axis)#将横坐标替换成
plt.legend((p_rf[0],p_anns[0],p_adaboost[0]),('RF','ANNs','AdaBoost'),loc='best',fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(150,200)  # 指定Y轴的高度
plt.xlabel('训练集大小(%)',fontsize=20)
plt.ylabel('MAE(s)',fontsize=20)
plt.show()
#plt.savefig('MAE.png', dpi=3600)