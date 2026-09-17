#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三维：两全面 ⊗ 均匀临界面 ⊗ 相生柱面，三面共点 = 五角星点"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; d=1/phi**2; w=np.exp(2j*np.pi/5); w2=w**2
Minv=np.linalg.inv(np.array([[w.real,-w2.real],[w.imag,-w2.imag]]))
def ab(th):
    c=np.exp(1j*th)-(1-d); return Minv@np.array([c.real,c.imag])

fig=plt.figure(figsize=(16.4,7.2),dpi=150)
ax=fig.add_subplot(121,projection="3d"); ax2=fig.add_subplot(122)
CLIP=(0,0.78)
def clip(C): return np.where((C>=CLIP[0])&(C<=CLIP[1]),C,np.nan)

A2,B2=np.meshgrid(np.linspace(-0.05,1.15,90),np.linspace(-0.40,0.90,90))
ax.plot_surface(A2,B2,clip(A2-d),color="#27865a",alpha=.30,linewidth=0,shade=False)
ax.plot_surface(A2,B2,clip(A2-B2-d),color="#2c5f8a",alpha=.28,linewidth=0,shade=False)

th=np.linspace(np.deg2rad(-110),np.deg2rad(115),220)
P=np.array([ab(t) for t in th]); Cax=np.linspace(CLIP[0],CLIP[1],30)
AA,CC=np.meshgrid(P[:,0],Cax); BB,_=np.meshgrid(P[:,1],Cax)
ax.plot_surface(AA,BB,CC,color="#c0392b",alpha=.24,linewidth=0,shade=False)

# ①∩② 直线 b=0, c=a−d
al=np.linspace(d,1.15,50); ax.plot(al,np.zeros_like(al),al-d,color="#111",lw=3.4,zorder=9)

a0,b0,c0=1/phi,0.0,1/phi**3
ax.scatter([a0],[b0],[c0],color="#f1c40f",s=260,edgecolor="#7d6608",lw=2,depthshade=False,zorder=20)
ax.text(a0+0.05,b0-0.02,c0+0.14,"三面共点\n(1/φ, 0, 1/φ³)",fontsize=10.5,weight="bold",color="#7d6608")
ax.set_xlabel("相生 a",fontsize=11); ax.set_ylabel("相克 b",fontsize=11); ax.set_zlabel("饱和 c",fontsize=11)
ax.set_title("三维：三张面只在一个点上碰头",fontsize=12.6,weight="bold",pad=6)
ax.view_init(elev=22,azim=-58)
h=[Line2D([0],[0],color="#27865a",lw=8,alpha=.5,label="两全面  c = a − d"),
   Line2D([0],[0],color="#2c5f8a",lw=8,alpha=.5,label="均匀临界面  c = a − b − d"),
   Line2D([0],[0],color="#c0392b",lw=8,alpha=.5,label="相生柱面  |λ1| = 1（沿 c 挤出）"),
   Line2D([0],[0],color="#111",lw=3.4,label="①∩② 交线：b = 0, c = a − d")]
ax.legend(handles=h,fontsize=9.2,loc="upper left",framealpha=.95)

# 右：沿交线扫 a
al2=np.linspace(0.30,1.05,400); L=np.abs((1-d)+al2*w); AR=np.rad2deg(np.angle((1-d)+al2*w))
ax2.plot(al2,L,color="#c0392b",lw=3,label="|λ1| 沿交线")
ax2.axhline(1,color="#7f8c8d",ls=":",lw=1.5)
ax2.axvline(1/phi,color="#27865a",ls="-.",lw=2)
ax2.plot(1/phi,1,"*",color="#f1c40f",ms=24,mec="#7d6608",mew=1.6,zorder=6)
ax2.annotate("a = 1/φ ：|λ1| = 1、arg = 36°\n（交线上唯一的一点）",(1/phi,1),textcoords="offset points",
             xytext=(20,-52),fontsize=10.2,color="#7d6608",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#7d6608"),
             bbox=dict(boxstyle="round,pad=0.4",fc="#fffdf0",ec="#c9a227",lw=1.4))
ax2b=ax2.twinx(); ax2b.plot(al2,AR,color="#8e44ad",lw=2,ls="--",label="arg λ1")
ax2b.set_ylabel("arg λ1（度）",fontsize=10.5,color="#8e44ad"); ax2b.tick_params(axis="y",colors="#8e44ad")
ax2b.axhline(36,color="#8e44ad",ls=":",lw=1.2)
ax2.set_xlabel("沿交线的相生强度 a",fontsize=11); ax2.set_ylabel("|λ1|",fontsize=11,color="#c0392b")
ax2.set_title("沿交线 b=0, c=a−d 扫 a：唯一穿越点",fontsize=12.6,weight="bold",pad=10)
ax2.grid(alpha=.22); ax2.set_ylim(0.75,1.30)
ax2.text(0.34,1.22,"a<1/φ：λ1 缩进圆内\na>1/φ：λ1 冲出圆外",fontsize=9.8,color="#333",
         bbox=dict(boxstyle="round,pad=0.4",fc="#fbfcfd",ec="#aab",lw=1.2))
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/three_surfaces.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/three_surfaces.png")
