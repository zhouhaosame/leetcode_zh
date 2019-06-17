# encoding=utf-8
from matplotlib import pyplot
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 600 #图片像素
plt.rcParams['figure.dpi'] = 600 #分辨率
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
str='5943 4262 4200 6342 10354 12023 7003 15834 10425 8234 12234 9345\
 7842 5843 6265 7324 4032 4432 7876 4154 4578 7452 4342 4666 6956 4023 4789\
 6753 4332 4700 6997 6888 6910 7752 12535 10000 8789 16543 11356 7843 13643 10235\
 6076 7854 6888 6453 5732 6956 6245 4754 5890 6425 4278 4300'
str=list(map(int,str.strip().split()))
bike_only=str[::3]
taxi_only=str[1::3]
ttca=str[2::3]
x = [i for  i in range(6,24)]
x_l = range(len(x))

plt.xlim(6, 24)  # 限定横轴的范围
plt.ylim(3000,17000)  # 限定纵轴的范围


plt.plot(x, bike_only, marker='D',ms=10,color='green')
plt.plot(x, taxi_only, marker = 'h', ms = 10,color='red')
plt.plot(x, ttca, marker = '.', ms = 10,color='blue')
plt.legend(('bike_only','taxi_only','TTCA'),loc='best',fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('时间槽',fontsize=15)  # X轴标签
plt.ylabel("EERT的均值",fontsize=15)  # Y轴标签
plt.show()
plt.savefig('f1.jpg', dpi = 1600)
