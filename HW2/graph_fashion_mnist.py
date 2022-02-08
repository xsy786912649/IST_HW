# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

plt.rcParams['font.sans-serif']=['Arial']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
A = np.array([0.5342,0.3873, 0.34702, 0.3216, 0.30393,0.28925, 0.2777844, 0.266898, 0.25806, 0.2527,0.2443,0.2351])
A1= np.array([0.42859, 0.3867,0.3861,0.3875,0.36913,0.34535,0.348537,0.3695798,0.39639,0.34511,0.333515,0.328143])


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

A = np.array([0.59252,0.4418, 0.398140, 0.3763417, 0.3606833,0.3465824, 0.333772, 0.32653, 0.32216,0.313421,0.306864,0.2967403])
A1= np.array([0.442470,0.4128,0.4030,0.4162206,0.367954,0.3625454, 0.36254,0.360546,0.34893,0.3309,0.3290935, 0.323668])
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

A = np.array([0.53201973,0.3893984,  0.3482333, 0.324502,0.30547,0.29257, 0.2811,0.27240, 0.2540879, 0.24805,0.2434,0.23542])
A1= np.array([0.43897682,0.398220,0.38814,0.40180, 0.360444,0.36212,0.37945,0.35868, 0.36398,0.3516515,0.33662730, 0.3220978])
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
A = np.array([88.1,87.95,88.2])
A1 = np.array([0.6,0.38,0.43])

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