#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1/φ^k 的奇偶分工：嵌套五边形 对角线(偶) vs 边长(奇)"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2
def pent(R,rot=90):
    return np.array([(R*np.cos(np.deg2rad(rot+72*k)), R*np.sin(np.deg2rad(rot+72*k))) for k in range(5)])

fig,ax=plt.subplots(figsize=(11.2,8.6),dpi=150)
R=1.0
# 两层五边形 + 星
for lvl,c in [(0,"#c0392b"),(1,"#2c5f8a")]:
    Rl=R/phi**(2*lvl)
    V=pent(Rl); Vs=np.array([V[(i*2)%5] for i in range(5)])
    ax.plot(list(V[:,0])+[V[0,0]],list(V[:,1])+[V[0,1]],color=c,lw=2.6,zorder=4)
    ax.plot(list(Vs[:,0])+[Vs[0,0]],list(Vs[:,1])+[Vs[0,1]],color=c,lw=1.1,ls=(0,(5,4)),zorder=3)

V=pent(1.0); Vi=pent(1/phi**2)
def ann(V0,V1,tx,ty,txt,c):
    m=(V0+V1)/2
    ax.annotate(txt,xy=m,xytext=(tx,ty),fontsize=12,weight="bold",color=c,
                ha="center",va="center",zorder=8,
                bbox=dict(boxstyle="round,pad=0.32",fc="white",ec=c,lw=1.4),
                arrowprops=dict(arrowstyle="-",color=c,lw=1.3,shrinkA=2,shrinkB=2))
ann(V[0],V[1],-1.95,1.15,"外·边长  1/φ\n（奇数幂）","#c0392b")
ann(V[0],V[2],-1.95,0.05,"外·对角线 1\n（偶数幂）","#c0392b")
ann(Vi[0],Vi[1],2.15,0.95,"内·边长  1/φ^3\n（奇数幂）","#2c5f8a")
ann(Vi[0],Vi[2],2.15,-0.15,"内·对角线 1/φ^2\n（偶数幂）","#2c5f8a")

ax.text(0,-1.62,"再内一层：对角线 1/φ^4（偶）　边长 1/φ^5（奇）　—— 层与层只差一个 q = 1/φ^2",
        ha="center",fontsize=12,color="#1f7a4d",weight="bold",
        bbox=dict(boxstyle="round,pad=0.45",fc="#f2faf6",ec="#1f7a4d",lw=1.4))
ax.set_xlim(-3.1,3.3); ax.set_ylim(-1.95,1.5); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("1/φ^k 的奇偶分工：偶数幂 = 对角线/层级尺度　奇数幂 = 边长/比例",
             fontsize=14,weight="bold",pad=8)
ax.text(0,1.32,"同一层：对角线 ÷ 边长 = φ　　层与层：× q = 1/φ^2",
        ha="center",fontsize=12,color="#333")
ax.text(0,-1.30,"⇒ 偶数幂 = 『整数步 / 闭合』　　奇数幂 = 『半整数步 / 旋量』",
        ha="center",fontsize=12.2,color="#c0392b",weight="bold")
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/phi_powers_parity.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("ok")
