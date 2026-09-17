#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对照图：五行 72° 嵌套 vs 毕达哥拉斯（五角星）36° 嵌套"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2
def pent(R,rot): return np.array([[R*np.cos(np.radians(rot+72*k)),R*np.sin(np.radians(rot+72*k))] for k in range(5)])
def close(P): return np.vstack([P,P[0]])

fig,axes=plt.subplots(1,2,figsize=(13.5,7.4),dpi=155)
RED="#c0392b"; BLUE="#2c5f8a"; GREEN="#27865a"; GREY="#b8bcc4"

# ---- 左：五行 72° 嵌套（周期5）----
ax=axes[0]; ax.set_aspect("equal"); ax.axis("off")
ax.set_title("① 五行构造：每层转 72°（周期 5）", fontsize=14, weight="bold", pad=14)
colors=["#c0392b","#27865a","#2c5f8a","#c9a227","#a0522d"]  # 火木水金土
labels=["火","木","水","金","土"]
fire=[]
for n in range(5):
    H=1.0*(0.72**n) if False else 1.0*(1/phi)**n
    P=pent(H,90+72*n)
    ax.plot(*close(P).T, color=GREY, lw=1.6, zorder=1)
    # 火 = 该层顶部顶点（角度 90+72n）
    f=P[0]; fire.append(f)
    ax.plot(P[:,0],P[:,1],".",color="#888",ms=4,zorder=2)
    ax.plot(*f,"o",color=RED,ms=9,zorder=4)
    ax.annotate(str(n),f,textcoords="offset points",xytext=(8,6),fontsize=11,color=RED,weight="bold")
fire=np.array(fire)
ax.plot(fire[:,0],fire[:,1],"-",color=GREEN,lw=2.2,alpha=.85,zorder=3)
ax.text(0,0,"回到起点",ha="center",va="center",fontsize=10,color=RED)
ax.text(0.02,-1.28,"火的位置：90→162→234→306→18→90°，5 次回到正上方",ha="center",fontsize=10.5,color="#444")

# ---- 右：五角星自然嵌套（36°, 1/φ²，真·毕达哥拉斯）----
ax=axes[1]; ax.set_aspect("equal"); ax.axis("off")
ax.set_title("② 毕达哥拉斯构造：每层转 36°、缩放 1/φ²", fontsize=14, weight="bold", pad=14)
R=1.0; rot=90.0
for n in range(4):
    P=pent(R,rot)
    ax.plot(*close(P).T,color=GREEN,lw=2.0 if n==0 else 1.5,alpha=1 if n==0 else .8,zorder=2)
    # 五角星 = 隔点相连
    star=P[[0,2,4,1,3,0]]
    ax.plot(star[:,0],star[:,1],color=RED,lw=1.6,alpha=.9,zorder=3)
    ax.plot(P[:,0],P[:,1],"o",color=BLUE,ms=5,zorder=4)
    R*=1/phi**2; rot+=36
ax.text(0,-1.34,"半径每层 ×1/φ²，方位每层 +36°；5 层转 180°（倒置），10 层才 360°",
        ha="center",fontsize=10.5,color="#444")
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/wuxing_pythagoras_nesting.png",bbox_inches="tight",facecolor="white",pad_inches=0.18)
print("已生成 output/wuxing_pythagoras_nesting.png")
