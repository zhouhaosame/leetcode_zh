import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x_axis = [300,400,500,600,700]

pw1 = [4,14,18,25,36]
pw2 = [5,18,24,32,40]
pw3 = [7.5,21,26,35,42]
pw4 = [7.5,23,35,42,45]
pw5 = [9,29,38,48,51]


x = np.arange(len(x_axis))  #首先用第一个的长度作为横坐标
width = 0.15   #设置柱与柱之间的宽度
fig,ax = plt.subplots()
p_pw1 = ax.bar(x-2*width,pw1,width,alpha = 0.9,color= 'red')
p_pw2 = ax.bar(x-width,pw2,width,alpha = 0.9,color= 'blue')
p_pw3 = ax.bar(x,pw3,width,alpha = 0.9,color= 'orange')
p_pw4 = ax.bar(x+width,pw4,width,alpha = 0.9,color= 'green')
p_pw5 = ax.bar(x+2*width,pw5,width,alpha = 0.9,color= 'yellow')

ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(x_axis)#将横坐标替换成
plt.legend((p_pw1[0],p_pw2[0],p_pw3[0],p_pw4[0],p_pw5[0]),('p.w=200','p.w=250','p.w=300',"p.w=350","p.w=400"),ncol=3,loc='best',fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(0,65)  # 指定Y轴的高度
plt.xlabel('骑行可达参数p.k',fontsize=20)
plt.ylabel('运行时间(ms)',fontsize=20)
plt.show()
#plt.savefig('MAE.png', dpi=3600)