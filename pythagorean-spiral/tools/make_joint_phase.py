#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""联合相图：均匀模临界面 vs 图案模临界面（d = 1/φ²）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; w=np.exp(2j*np.pi/5); d=q
def lam(a,b,k): return (1-d)+a*w**k-b*w**(2*k)

A,B=np.meshgrid(np.linspace(-0.25,1.35,600), np.linspace(-0.25,1.35,600))
L0=np.abs((1-d)+A-B); L1=np.abs((1-d)+A*w-B*w**2)

fig,ax=plt.subplots(figsize=(8.6,7.4),dpi=160)
cs=ax.contourf(A,B,np.minimum(L0,L1),levels=[0,0.6,1.0,1.5,2.5],
               colors=["#dce9f5","#eef4f9","#fdece9","#f8d7d1"],alpha=.85)
ax.contour(A,B,L0,levels=[1.0],colors="#2c5f8a",linewidths=2.4)
ax.contour(A,B,L1,levels=[1.0],colors="#c0392b",linewidths=2.4)

ax.plot(1/phi,0,"*",color="#27865a",ms=20,zorder=6)
ax.annotate("五角星点\n(a=1/φ, b=0)\nλ1=e^(i36°)",(1/phi,0),textcoords="offset points",
            xytext=(14,-42),fontsize=10,color="#27865a",
            arrowprops=dict(arrowstyle="->",color="#27865a"))
ax.plot(0.538,0.156,"o",color="#8e44ad",ms=11,zorder=6)
ax.annotate("双临界交点\n(a≈0.54, b≈0.16)",(0.538,0.156),textcoords="offset points",
            xytext=(-120,18),fontsize=10,color="#8e44ad",
            arrowprops=dict(arrowstyle="->",color="#8e44ad"))

from matplotlib.lines import Line2D
h=[Line2D([0],[0],color="#2c5f8a",lw=2.4,label="均匀模临界 |λ0|=1（k=0）"),
   Line2D([0],[0],color="#c0392b",lw=2.4,label="图案模临界 |λ1|=1（k=1）")]
ax.legend(handles=h,fontsize=10.5,loc="lower right")
ax.set_xlabel("相生强度 a",fontsize=11.5); ax.set_ylabel("相克强度 b",fontsize=11.5)
ax.set_title("联合相图：两个临界（不同不可约表示）\n固定 d = 1/φ² ≈ 0.382",fontsize=13,weight="bold",pad=13)
ax.grid(alpha=.22)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/joint_phase_diagram.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/joint_phase_diagram.png")
