#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""两全面 c=a−d 套上相图：均匀模临界线塌缩成 b=0"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; w=np.exp(2j*np.pi/5); d=q
def lam1(a,b): return (1-d)+a*w-b*w**2

fig,axes=plt.subplots(1,3,figsize=(17.2,6.2),dpi=150)
ax,ax2,ax3=axes

A,B=np.meshgrid(np.linspace(-0.15,1.35,600), np.linspace(-0.35,1.05,600))
# ---------- panel 1: c = 0 ----------
L0a=np.abs((1-d)+A-B); L1a=np.abs(lam1(A,B))
ax.contourf(A,B,np.minimum(L0a,L1a),levels=[0,0.6,1.0,1.6,2.6],
            colors=["#e8eef5","#f3f7fa","#fdf0ec","#f9dcd4"],alpha=.7)
ax.contour(A,B,L0a,levels=[1.0],colors="#2c5f8a",linewidths=2.4)
ax.contour(A,B,L1a,levels=[1.0],colors="#c0392b",linewidths=2.4)
ax.plot(0.535,0.153,"o",color="#e67e22",ms=11,zorder=7)
ax.annotate("双临界点",(0.535,0.153),textcoords="offset points",xytext=(24,-24),fontsize=9.6,
            color="#e67e22",weight="bold",arrowprops=dict(arrowstyle="->",color="#e67e22"))
ax.plot(1/phi,0,"*",color="#27865a",ms=22,zorder=8)
ax.annotate("五角星点\n|λ0|=2/φ（过载，不在蓝线上）",(1/phi,0),textcoords="offset points",
            xytext=(-14,-58),fontsize=9.4,color="#27865a",ha="center",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#27865a"))
ax.set_title("① 原来（c = 0）\n均匀模临界是斜线，两全点离五角星点很远",fontsize=11.6,weight="bold",pad=9)
ax.set_xlim(-0.15,1.35); ax.set_ylim(-0.35,1.05); ax.grid(alpha=.2)
ax.set_xlabel("相生 a",fontsize=11); ax.set_ylabel("相克 b",fontsize=11)

# ---------- panel 2: c = a − d ----------
ax2.contourf(A,B,A*0+np.abs(1-B),levels=[0,0.999,1.001,3],colors=["#f9dcd4","#d6f0e0"],alpha=.55)
ax2.axhline(0,color="#2c5f8a",lw=3)
ax2.contour(A,B,L1a,levels=[1.0],colors="#c0392b",linewidths=2.4)
ax2.plot(1/phi,0,"*",color="#27865a",ms=26,zorder=8)
ax2.annotate("五角星点 (1/φ, 0)\n= 两全点（唯一正交点）",(1/phi,0),textcoords="offset points",
             xytext=(6,-64),fontsize=9.6,color="#27865a",ha="center",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#27865a"))
ax2.text(1.28,0.62,"b > 0\n|λ0|=1−b < 1\n稳定",fontsize=10,color="#27865a",ha="right",weight="bold",
         bbox=dict(boxstyle="round,pad=0.4",fc="#f2faf6",ec="#27865a",lw=1.3))
ax2.text(1.28,-0.26,"b < 0\n|λ0|=1−b > 1\n过载",fontsize=10,color="#c0392b",ha="right",weight="bold",
         bbox=dict(boxstyle="round,pad=0.4",fc="#fdeceb",ec="#c0392b",lw=1.3))
ax2.set_title("② 补上 c = a − d\n均匀模临界塌缩成 b = 0（一条水平线）",fontsize=11.6,weight="bold",pad=9)
ax2.set_xlim(-0.15,1.35); ax2.set_ylim(-0.35,1.05); ax2.grid(alpha=.2)
ax2.set_xlabel("相生 a",fontsize=11); ax2.set_ylabel("相克 b",fontsize=11)
h=[Line2D([0],[0],color="#2c5f8a",lw=3,label="均匀模临界 |λ0|=1"),
   Line2D([0],[0],color="#c0392b",lw=2.4,label="相生模临界 |λ1|=1（c 不动它）")]
ax2.legend(handles=h,fontsize=9.4,loc="upper left",framealpha=.95)

# ---------- panel 3: λ0 = 1 − b ----------
bb=np.linspace(-0.35,1.05,300)
ax3.plot(bb,1-bb,color="#2c5f8a",lw=3.2)
ax3.axhline(1,color="#7f8c8d",ls=":",lw=1.5); ax3.axvline(0,color="#7f8c8d",ls=":",lw=1.5)
ax3.fill_between(bb,0,1,where=(1-bb<=1),color="#d6f0e0",alpha=.5)
ax3.fill_between(bb,1,3,where=(1-bb>=1),color="#f9dcd4",alpha=.5)
ax3.plot(0,1,"*",color="#27865a",ms=24,zorder=6)
ax3.annotate("b=0 ⟹ λ0=1\n（五角星点）",(0,1),textcoords="offset points",xytext=(30,34),
             fontsize=10,color="#27865a",weight="bold",arrowprops=dict(arrowstyle="->",color="#27865a"))
ax3.set_title("③ λ0 = 1 − b\n（与 a、d 完全无关）",fontsize=11.6,weight="bold",pad=9)
ax3.set_xlabel("相克 b",fontsize=11); ax3.set_ylabel("λ0",fontsize=11)
ax3.set_xlim(-0.35,1.05); ax3.set_ylim(0,1.65); ax3.grid(alpha=.22)
ax3.text(0.6,1.35,"相克 b 成了\n唯一的『过载旋钮』",fontsize=10.2,color="#333",weight="bold",
         bbox=dict(boxstyle="round,pad=0.4",fc="#fbfcfd",ec="#aab",lw=1.2))

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/cface_phase.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/cface_phase.png")
