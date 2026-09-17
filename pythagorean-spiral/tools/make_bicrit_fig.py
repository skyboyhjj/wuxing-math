#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""双临界点：准周期（24.78°） vs 五角星点：10 步闭合（36°）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; d=q; w=np.exp(2j*np.pi/5); w2=w**2
# c=0 双临界点精确解
c2=3-phi; c1=5**0.5/phi**2; c0=-5**0.5/phi**2
aD=(-c1+np.sqrt(c1**2-4*c2*c0))/(2*c2); bD=aD-q; thD=np.rad2deg(np.angle((1-d)+aD*w-bD*w2))

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.6,6.9),dpi=150,gridspec_kw={"width_ratios":[1.1,1]})

# ---- 左：|λ1|=1 曲线上两个点 ----
A,B=np.meshgrid(np.linspace(-0.15,1.0,600),np.linspace(-0.4,0.75,600))
L1=np.abs((1-d)+A*w-B*w2); L0=np.abs((1-d)+A-B)
ax.contour(A,B,L1,levels=[1.0],colors="#c0392b",linewidths=2.6)
ax.contour(A,B,L0,levels=[1.0],colors="#2c5f8a",linewidths=2.0,linestyles="--")
ax.plot(aD,bD,"o",color="#8e44ad",ms=13,mec="white",mew=1.8,zorder=8)
ax.annotate("c=0 双临界点\n(0.5357, 0.1537)\n两模都临界，但 θ=24.78°\n→ 准周期（无周期）",
            (aD,bD),textcoords="offset points",xytext=(-6,-86),fontsize=10,color="#8e44ad",weight="bold",ha="center",
            arrowprops=dict(arrowstyle="->",color="#8e44ad"),
            bbox=dict(boxstyle="round,pad=0.42",fc="#faf5ff",ec="#8e44ad",lw=1.4))
ax.plot(1/phi,0,"*",color="#27865a",ms=26,mec="white",mew=1.8,zorder=9)
ax.annotate("补 c=a−d 后 → 五角星点\n(1/φ, 0)，θ=36°\n→ 10 步闭合（节律正常）",
            (1/phi,0),textcoords="offset points",xytext=(24,40),fontsize=10,color="#27865a",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#27865a"),
            bbox=dict(boxstyle="round,pad=0.42",fc="#f2faf6",ec="#27865a",lw=1.4))
from matplotlib.lines import Line2D
h=[Line2D([0],[0],color="#c0392b",lw=2.6,label="相生临界 |λ1|=1"),
   Line2D([0],[0],color="#2c5f8a",lw=2.0,ls="--",label="c=0 时的均匀临界 |λ0|=1")]
ax.legend(handles=h,fontsize=9.8,loc="upper left",framealpha=.95)
ax.set_xlim(-0.15,1.0); ax.set_ylim(-0.4,0.75); ax.grid(alpha=.2)
ax.set_xlabel("相生 a",fontsize=11); ax.set_ylabel("相克 b",fontsize=11)
ax.set_title("同一个“以平为期”，两个不同的相位",fontsize=12.4,weight="bold",pad=10)

# ---- 右：单位圆步进 ----
th_c=np.linspace(0,2*np.pi,400); ax2.plot(np.cos(th_c),np.sin(th_c),color="#ccc",lw=1.3,ls="--")
for name,t,c,m in [("θ=36°（五角星，10 步闭合）",36,"#27865a","o"),("θ=24.78°（双临界点，准周期）",thD,"#8e44ad","s")]:
    ks=range(0,15); pts=[np.exp(1j*np.deg2rad(t*k)) for k in ks]
    ax2.plot([p.real for p in pts],[p.imag for p in pts],color=c,lw=1.2,alpha=.55)
    ax2.plot([p.real for p in pts],[p.imag for p in pts],m,color=c,ms=8,mec="white",mew=1.1,alpha=.9,mfc=c)
ax2.plot([1],[0],"*",color="#f1c40f",ms=24,mec="#7d6608",mew=1.6,zorder=9)
ax2.annotate("10 步回到原点（闭合）",(1,0),textcoords="offset points",xytext=(-10,-34),fontsize=10,
             color="#27865a",weight="bold",ha="center",arrowprops=dict(arrowstyle="->",color="#27865a"))
ax2.annotate("14.5 步还没回来，\n也永远不会回来",(-1,0.05),textcoords="offset points",xytext=(30,30),fontsize=10,
             color="#8e44ad",weight="bold",arrowprops=dict(arrowstyle="->",color="#8e44ad"),
             bbox=dict(boxstyle="round,pad=0.35",fc="#faf5ff",ec="#8e44ad",lw=1.2))
ax2.text(0,1.22,"● 36°（绿）　■ 24.78°（紫）",fontsize=9.8,color="#333",ha="center",
         bbox=dict(boxstyle="round,pad=0.32",fc="#fbfcfd",ec="#aab",lw=1.1))
ax2.set_aspect("equal"); ax2.set_xlim(-1.35,1.35); ax2.set_ylim(-1.35,1.4)
ax2.set_xlabel("Re",fontsize=11); ax2.set_ylabel("Im",fontsize=11)
ax2.set_title("节律：闭合 vs 准周期",fontsize=12.4,weight="bold",pad=10)
ax2.grid(alpha=.18)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/bicritical_tcm.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/bicritical_tcm.png")
