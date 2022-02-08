# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

plt.rcParams['font.sans-serif']=['Arial']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号

x = np.array([1,2,3,4,5,6,7,8,9,10])
A = np.array([0.1617663,0.03453338, 0.018932, 0.01217081705729167, 0.008346,0.0060745496, 0.004583529196, 0.00349862757, 0.0027513918, 0.0022762045264])
A1= np.array([0.1402837,0.1142785,0.0899995,0.085883326,0.0825176686,0.07276377,0.06920089572,0.073581501,0.0695975422,0.069687195123])


plt.figure(figsize=(13,5))
plt.grid(linestyle = "--") #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框



plt.plot(x,A,'#FF6347',label="Train loss",linewidth=1.5,marker='o',markersize=5,markerfacecolor='#FF6347',markeredgewidth=1.5 )
plt.plot(x,A1,"#696969",label="Validate loss",linewidth=1.5,markersize=5,marker='s',markerfacecolor='#696969',markeredgewidth=1.5)

plt.xticks(x,fontsize=16,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=16,fontweight='bold')
#plt.title("Computing time of anytime adaptation",fontsize=14,fontweight='bold') #默认字体大小为14
plt.xlabel("Epoches",fontsize=18,fontweight='bold')
plt.ylabel("Loss",fontsize=18,fontweight='bold')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=18,fontweight='bold') #设置图例字体的大小和粗细

plt.show()

plt.figure(figsize=(13,5))
plt.grid(linestyle = "--") #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

A = np.array([0.19359950,0.0664206, 0.0463432, 0.03575077, 0.0289951190,0.023842338, 0.02073209, 0.01546410, 0.0133139, 0.010993383])
A1= np.array([0.14958,0.1189645752,0.0952186,0.095684,0.081059,0.076177,0.072686,0.0666441,0.06020,0.06115377])
plt.plot(x,A,'#FF6347',label="Train loss",linewidth=1.5,marker='o',markersize=5,markerfacecolor='#FF6347',markeredgewidth=1.5 )
plt.plot(x,A1,"#696969",label="Validate loss",linewidth=1.5,markersize=5,marker='s',markerfacecolor='#696969',markeredgewidth=1.5)


plt.xticks(x,fontsize=16,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=16,fontweight='bold')
#plt.title("Computing time of anytime adaptation",fontsize=14,fontweight='bold') #默认字体大小为14
plt.xlabel("Epoches",fontsize=18,fontweight='bold')
plt.ylabel("Loss",fontsize=18,fontweight='bold')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=18,fontweight='bold') #设置图例字体的大小和粗细

plt.show()

plt.figure(figsize=(13,5))
plt.grid(linestyle = "--") #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

A = np.array([0.18670,0.06020, 0.0456914, 0.0392, 0.03576,0.032337941, 0.03054598,0.0293421596288, 0.027772437, 0.026291])
A1= np.array([0.14217,0.117646,0.089543, 0.0811308,0.07027,0.0704532,0.0711851, 0.0678,0.070699,0.06767])
plt.plot(x,A,'#FF6347',label="Train loss",linewidth=1.5,marker='o',markersize=5,markerfacecolor='#FF6347',markeredgewidth=1.5 )
plt.plot(x,A1,"#696969",label="Validate loss",linewidth=1.5,markersize=5,marker='s',markerfacecolor='#696969',markeredgewidth=1.5)

plt.xticks(x,fontsize=16,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=16,fontweight='bold')
#plt.title("Computing time of anytime adaptation",fontsize=14,fontweight='bold') #默认字体大小为14
plt.xlabel("Epoches",fontsize=18,fontweight='bold')
plt.ylabel("Loss",fontsize=18,fontweight='bold')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=18,fontweight='bold') #设置图例字体的大小和粗细

plt.show()


plt.figure(figsize=(13,5))
plt.grid(linestyle = "--") #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

x = np.array([0,1,2,4,6,8,10,12,14,16])
A = np.array([12, 93.5, 95.55,97.25, 97.349, 97.639, 97.959,97.8799, 98.089996, 98.0999])-0.4
A2 = np.array([20,95.55,97.25, 97.349, 97.639, 97.959,97.8799, 98.089996, 98.0999, 98.2])

plt.plot(x,A,'#FF6347',label="Accuracy",linewidth=1.5,marker='o',markersize=5,markerfacecolor='#FF6347',markeredgewidth=1.5 )
ax.fill_between(x, (A-A2+A), (A2), color='r', alpha=.4)
plt.xticks(x,fontsize=16,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=16,fontweight='bold')
#plt.title("Computing time of anytime adaptation",fontsize=14,fontweight='bold') #默认字体大小为14
plt.xlabel("Epoches",fontsize=18,fontweight='bold')
plt.ylabel("Accuracy",fontsize=18,fontweight='bold')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=18,fontweight='bold') #设置图例字体的大小和粗细

plt.show()

plt.figure(figsize=(13,5))
plt.grid(linestyle = "--") #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

x = np.array([1,2,3])
A = np.array([98.11,98.18,98.21])
A1 = np.array([0.1,0.086,0.11])

plt.plot(x,A,'#FF6347',label="Accuracy",linewidth=1.5,marker='o',markersize=5,markerfacecolor='#FF6347',markeredgewidth=1.5 )
ax.fill_between(x, (A-A1), (A+A1), color='r', alpha=.2)
plt.xticks(x,fontsize=16,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=16,fontweight='bold')
#plt.title("Computing time of anytime adaptation",fontsize=14,fontweight='bold') #默认字体大小为14
plt.xlabel("Model",fontsize=18,fontweight='bold')
plt.ylabel("Accuracy",fontsize=18,fontweight='bold')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=18,fontweight='bold') #设置图例字体的大小和粗细

plt.show()