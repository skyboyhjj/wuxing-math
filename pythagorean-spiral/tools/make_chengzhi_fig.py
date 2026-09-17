#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""θ=0（承制平衡）vs 五角星点（但生无克）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; d=1/phi**2; w=np.exp(2j*np.pi/5); w2=w**2
def spec(a,b):
    return [(1-d)+a*w**k-b*w**(2*k) for k in range(5)]

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.6,6.8),dpi=150,gridspec_kw={"width_ratios":[1,1.05]})

th=np.linspace(0,2*np.pi,400); ax.plot(np.cos(th),np.sin(th),color="#95a5a6",lw=1.5,ls="--")
l0=spec(1/phi**3,1/phi**2); l1=spec(1/phi,0.0)
mk=["o","o","o","o","o"]
for i,(z,c) in enumerate(zip(l0,["#c0392b"]+["#27865a"]*4)):
    ax.plot(z.real,z.imag,"o",color=c,ms=12,mec="white",mew=1.6,zorder=6)
for i,(z,c) in enumerate(zip(l1,["#e67e22"]+["#8e44ad"]*4)):
    ax.plot(z.real,z.imag,"^",color=c,ms=12,mec="white",mew=1.6,zorder=5,alpha=.75)
ax.annotate("λ0 = 2/φ = 1.236\n（无承制 → 过载）",(l1[0].real,0),textcoords="offset points",
            xytext=(20,26),fontsize=10,color="#e67e22",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#e67e22"))
ax.annotate("λ0 = 2/φ³ = 0.472\n（有承制 → 稳）",(l0[0].real,0),textcoords="offset points",
            xytext=(-30,-46),fontsize=10,color="#c0392b",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#c0392b"))
ax.annotate("λ1 = λ4 = 1 ∠0°\n实、正、不转\n（生克相抵）",(1,0),textcoords="offset points",
            xytext=(34,-56),fontsize=10,color="#27865a",weight="bold",ha="center",
            arrowprops=dict(arrowstyle="->",color="#27865a"))
ax.text(-1.32,1.18,"● θ=0（承制平衡）   ▲ 五角星点（但生无克）",fontsize=9.8,color="#333",
        bbox=dict(boxstyle="round,pad=0.35",fc="#fbfcfd",ec="#aab",lw=1.2))
ax.set_aspect("equal"); ax.set_xlim(-1.42,1.48); ax.set_ylim(-1.32,1.38)
ax.set_xlabel("Re",fontsize=11); ax.set_ylabel("Im",fontsize=11)
ax.set_title("θ=0：承制平衡　vs　五角星点：但生无克",fontsize=12.4,weight="bold",pad=10)
ax.grid(alpha=.2)

aa=np.linspace(0.08,0.40,600); b=d
ARI=np.rad2deg(np.angle((1-d)+aa*w-b*w2)); MOD=np.abs((1-d)+aa*w-b*w2)
ax2.plot(aa/d,ARI,color="#27865a",lw=3,label="arg λ1（相位）")
ax2.axhline(0,color="#7f8c8d",ls=":",lw=1.4); ax2.axvline(phi,color="#c0392b",ls="-.",lw=2)
ax2.plot(phi,0,"*",color="#f1c40f",ms=26,mec="#7d6608",mew=1.6,zorder=6)
ax2.annotate("承/亢 = φ\n相位归零（承制到位）",(phi,0),textcoords="offset points",
             xytext=(26,44),fontsize=10.4,color="#7d6608",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#7d6608"),
             bbox=dict(boxstyle="round,pad=0.42",fc="#fffdf0",ec="#c9a227",lw=1.4))
ax2.set_xlabel("承 / 亢 之比  b/a（固定 b = d）",fontsize=11); ax2.set_ylabel("arg λ1（度）",fontsize=11)
ax2.set_title("承制不足则偏转，承制过头则反偏",fontsize=12.4,weight="bold",pad=10)
ax2.grid(alpha=.22)
ax2.text(0.72,-6.5,"← 承不足：负相位",fontsize=10,color="#2c5f8a",weight="bold")
ax2.text(1.75,3.0,"承过度：正相位 →",fontsize=10,color="#8e44ad",weight="bold")
ax2.set_ylim(-9.5,9.5); ax2.set_xlim(0.15,2.6)
ax2.legend(fontsize=10.2,loc="upper left")
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/chengzhi_pingren.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/chengzhi_pingren.png")
