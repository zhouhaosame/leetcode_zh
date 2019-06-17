import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_axis = [1,2,3,4,5]

bike = [272,567,943,1203,1703]#rf
taxi = [214,317,398,489,585]#anns
mixed = [164,258,317,420,525]#adaboost


x = np.arange(len(x_axis))  #首先用第一个的长度作为横坐标
width = 0.2   #设置柱与柱之间的宽度
fig,ax = plt.subplots()
p_rf = ax.bar(x-width,bike,width,alpha = 0.9,color='green')
p_anns = ax.bar(x,taxi,width,alpha = 0.9,color= 'red')
p_adaboost = ax.bar(x+width,mixed,width,alpha = 0.9,color= 'blue')
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x_axis)#将横坐标替换成
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend((p_rf[0],p_anns[0],p_adaboost[0]),('Bike-only','Taxi-only','TTCA'),loc='best',fontsize=20)

# 设置图例字体大小

plt.ylim(0,1800)  # 指定Y轴的高度
plt.xlabel('行程距离(km)',fontsize=20)
plt.ylabel('平均行程时间(s)',fontsize=20)
plt.show()
plt.savefig('baseline.png', dpi=3600)