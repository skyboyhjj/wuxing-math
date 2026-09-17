#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""相生临界线 |λ1|=1 上：相位 θ 与 均匀模 |λ0| 的取舍"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; w=np.exp(2j*np.pi/5); w2=w**2; base=1-q
M=np.array([[w.real,-w2.real],[w.imag,-w2.imag]]); Minv=np.linalg.inv(M)
def ab(th):
    c=np.exp(1j*th)-base; return Minv@np.array([c.real,c.imag])
def L0(th):
    a,b=ab(th); return abs(base+a-b)

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.4,7.0),dpi=150,gridspec_kw={"width_ratios":[1.18,1]})

th=np.linspace(np.deg2rad(-120),np.deg2rad(110),900)
P=np.array([ab(t) for t in th]); V=np.array([L0(t) for t in th])
pts=np.stack([P[:,0],P[:,1]],axis=1).reshape(-1,1,2)
segs=np.concatenate([pts[:-1],pts[1:]],axis=1)
lc=LineCollection(segs,cmap="coolwarm",lw=4.2); lc.set_array(V[:-1]); lc.set_clim(0.3,2.1)
ax.add_collection(lc)
cb=fig.colorbar(lc,ax=ax,fraction=.046,pad=.02); cb.set_label("均匀模 |λ0|",fontsize=11)

for i,(T,c) in enumerate([(0,"#1f7a4d"),(24.778655,"#e67e22"),(36,"#c0392b")],1):
    p=ab(np.deg2rad(T))
    ax.text(p[0],p[1],str(i),ha="center",va="center",fontsize=11,weight="bold",color=c,zorder=9,
            bbox=dict(boxstyle="circle,pad=0.34",fc="white",ec=c,lw=2.0))
ax.text(0.98,0.03,"1  θ=0°      (a,b)=(1/φ³, 1/φ²)   |λ0|=2/φ³=0.472\n"
                  "2  θ=24.78°  (a,b)=(0.536, 0.154)  |λ0|=1（不过载）\n"
                  "3  θ=36°     (a,b)=(1/φ, 0)        |λ0|=2/φ=1.236（过载）",
        transform=ax.transAxes,ha="right",va="bottom",fontsize=9.5,color="#333",
        bbox=dict(boxstyle="round,pad=0.45",fc="#fbfcfd",ec="#aab",lw=1.2))
ax.set_xlim(-0.30,0.82); ax.set_ylim(-0.62,0.70)
ax.set_xlabel("相生强度 a",fontsize=11.5); ax.set_ylabel("相克强度 b",fontsize=11.5)
ax.set_title("相生临界线 |λ1|=1 上的取舍\n（颜色 = 均匀模 |λ0|）",fontsize=12.6,weight="bold",pad=10)
ax.grid(alpha=.2)

tt=np.rad2deg(th); vv=V
ax2.plot(tt,vv,color="#2c5f8a",lw=3)
ax2.axhline(1.0,color="#7f8c8d",ls="--",lw=1.6)
ax2.axvline(36,color="#c0392b",ls=":",lw=1.8)
ax2.axvline(24.778655,color="#e67e22",ls=":",lw=1.8)
ax2.fill_between(tt,0,1,where=(vv<=1),color="#d6f0e0",alpha=.75)
ax2.plot(36,2/phi,"o",color="#c0392b",ms=11,mec="white",mew=1.5,zorder=6)
ax2.annotate("θ=36°：|λ0|=2/φ=1.236\n（必然过载）",(36,2/phi),textcoords="offset points",
             xytext=(-128,10),fontsize=10,color="#c0392b",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#c0392b"))
ax2.plot(24.778655,1.0,"o",color="#e67e22",ms=11,mec="white",mew=1.5,zorder=6)
ax2.annotate("θ=24.78°：|λ0|=1\n（双临界点）",(24.778655,1.0),textcoords="offset points",
             xytext=(18,-46),fontsize=10,color="#e67e22",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#e67e22"))
ax2.plot(0,2/phi**3,"o",color="#1f7a4d",ms=9,mec="white",mew=1.4,zorder=6)
ax2.annotate("θ=0°：|λ0|=2/φ³=0.472",(0,2/phi**3),textcoords="offset points",
             xytext=(40,12),fontsize=10,color="#1f7a4d",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#1f7a4d"))
ax2.text(60,0.62,"绿色带 = 不过载区\n须 θ ≲ 24.78°",fontsize=10.2,color="#1f7a4d",weight="bold",
         bbox=dict(boxstyle="round,pad=0.4",fc="#f2faf6",ec="#1f7a4d",lw=1.3))
ax2.set_xlim(-20,95); ax2.set_ylim(0.35,2.15)
ax2.set_xlabel("相生模的相位 arg λ1（度）",fontsize=11.5); ax2.set_ylabel("均匀模 |λ0|",fontsize=11.5)
ax2.set_title("要压住过载，就必须离开 36°",fontsize=12.6,weight="bold",pad=10)
ax2.grid(alpha=.22)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/line36_tradeoff.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/line36_tradeoff.png")
