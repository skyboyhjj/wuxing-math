#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""36°临界线 与 双临界点：d=1/φ² 时分离，d=2/(√5φ) 时重合"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; s5=5**0.5; w=np.exp(2j*np.pi/5)

def draw(ax,d,title,mark36,markBi,note):
    A,B=np.meshgrid(np.linspace(-0.1,1.0,600),np.linspace(-0.3,0.7,600))
    L0=np.abs((1-d)+A-B); L1=np.abs((1-d)+A*w-B*(w**2))
    ax.contour(A,B,L0,levels=[1.0],colors="#2c5f8a",linewidths=2.2,linestyles="--")
    ax.contour(A,B,L1,levels=[1.0],colors="#c0392b",linewidths=2.6)
    if mark36:
        a=1/phi**2+d/phi; b=d-1/phi**2
        ax.plot(a,b,"*",color="#27865a",ms=26,mec="white",mew=1.8,zorder=9)
        ax.annotate(f"36° 点\n({a:.4f}, {b:.4f})",(a,b),textcoords="offset points",xytext=(20,-40),
                    fontsize=10,color="#27865a",weight="bold",arrowprops=dict(arrowstyle="->",color="#27865a"),
                    bbox=dict(boxstyle="round,pad=0.35",fc="#f2faf6",ec="#27865a",lw=1.3))
    if markBi:
        ax.plot(*markBi,"o",color="#8e44ad",ms=13,mec="white",mew=1.8,zorder=8)
        ax.annotate("双临界点\n(0.5357, 0.1537)\narg=24.78°",markBi,textcoords="offset points",xytext=(24,26),
                    fontsize=9.8,color="#8e44ad",weight="bold",arrowprops=dict(arrowstyle="->",color="#8e44ad"),
                    bbox=dict(boxstyle="round,pad=0.35",fc="#faf5ff",ec="#8e44ad",lw=1.3))
    ax.set_xlim(-0.1,1.0); ax.set_ylim(-0.3,0.7); ax.grid(alpha=.2)
    ax.set_xlabel("相生 a",fontsize=11); ax.set_ylabel("相克 b",fontsize=11)
    ax.set_title(title,fontsize=12.2,weight="bold",pad=9)
    ax.text(0.02,0.63,note,fontsize=10.6,color="#333",weight="bold",
            bbox=dict(boxstyle="round,pad=0.4",fc="#fbfcfd",ec="#aab",lw=1.2))
    h=[Line2D([0],[0],color="#c0392b",lw=2.6,label="相生临界 |λ1|=1"),
       Line2D([0],[0],color="#2c5f8a",lw=2.2,ls="--",label="均匀临界 |λ0|=1")]
    ax.legend(handles=h,fontsize=9.4,loc="lower right",framealpha=.95)

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.6,6.9),dpi=150)
draw(ax,1/phi**2,"① d = 1/φ²（我们一直用的）\n36°点与双临界点【分离】",True,(0.5356874,0.1537214),
     "36° 点在 |λ1|=1 上\n但不在 |λ0|=1 上\n→ 两点不是同一个")
d2=2/(s5*phi)
draw(ax2,d2,"② d = 2/(√5·φ) ≈ 0.5528\n36°点与双临界点【重合】",True,None,
     "三个条件同时成立：\n|λ0|=1 ∧ |λ1|=1 ∧ arg=36°\n→ 三线共点")
ax2.text(0.36,0.60,"★ 三线共点\n(a,b)=(φ/√5, 1/(√5φ²))\n且 b/a = 1/φ³（手性）",
         fontsize=9.8,color="#c0392b",weight="bold",
         bbox=dict(boxstyle="round,pad=0.35",fc="#fffdf0",ec="#c9a227",lw=1.3))
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/line36_vs_bicrit.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/line36_vs_bicrit.png")
