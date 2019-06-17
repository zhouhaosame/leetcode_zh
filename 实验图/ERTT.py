import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_axis = [20,40,60,80,100]

rf = [22256,20087,18567,17956,16875]
anns = [23333,21111,19865,18111,17324]
adaboost = [23111,22145,20457,19099,17546]


x = np.arange(len(x_axis))  #首先用第一个的长度作为横坐标
width = 0.2   #设置柱与柱之间的宽度
fig,ax = plt.subplots()
p_rf = ax.bar(x-width,rf,width,alpha = 0.9,)
p_anns = ax.bar(x,anns,width,alpha = 0.9,color= 'red')
p_adaboost = ax.bar(x+width,adaboost,width,alpha = 0.9,color= 'green')
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x_axis)#将横坐标替换成
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend((p_rf[0],p_anns[0],p_adaboost[0]),('RF','ANNs','AdaBoost'),loc='best',fontsize=20)

# 设置图例字体大小

plt.ylim(16000,24500)  # 指定Y轴的高度
plt.xlabel('训练集大小(%)',fontsize=20)
plt.ylabel('ERTT的均值',fontsize=20)
plt.show()
plt.savefig('ERTT.png', dpi=3600)