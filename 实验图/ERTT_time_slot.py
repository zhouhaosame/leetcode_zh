import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_axis = [i for i in range(6,24)]

d=[5943, 4262, 4200,6342,9754 ,10923, 7003, 13834 ,10425, 8234, 12834, 9345,\
 7842 ,5843, 6265, 7324, 4032, 4432, 7876, 4154, 4578, 7452, 4342 ,4666,\
 6956 ,4023, 4789, 6753, 4332 ,4700, 6997, 6888, 6910, 7752, 12935, 10000,\
 8789 ,14243, 11356, 7843, 12943, 10235, 6076 ,7854, 6888, 6453, 5732, 6956,\
 6245 ,4754 ,5890, 6425, 4278, 4300]
bike=[item+6000 for item in d[::3]]
taxi=[item+6000 for item in d[1::3]]
ttca=[item+6000 for item in d[2::3]]



x = np.arange(len(x_axis))  #首先用第一个的长度作为横坐标
width = 0.25   #设置柱与柱之间的宽度
fig,ax = plt.subplots()

p_pw2 = ax.bar(x-width,bike,width,alpha = 0.9,color= 'green')
p_pw3 = ax.bar(x,taxi,width,alpha = 0.9,color= 'orange')
p_pw4 = ax.bar(x+width,ttca,width,alpha = 0.9,color= 'blue')


ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x_axis)#将横坐标替换成
plt.legend((p_pw2[0],p_pw3[0],p_pw4[0]),('Bike-only','Taxi-only','TTCA'),ncol=3,loc='best',fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(-1,18)  # 指定Y轴的高度
plt.ylim(9000,22222)  # 指定Y轴的高度
plt.xlabel('时间槽（h）',fontsize=20)
plt.ylabel('ERTT的均值',fontsize=20)
plt.show()
#plt.savefig('MAE.png', dpi=3600)