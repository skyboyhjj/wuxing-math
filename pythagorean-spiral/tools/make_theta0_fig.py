#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""θ=0° 点：虚部相消（实性）+ b=d（临界）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; d=1/phi**2; w=np.exp(2j*np.pi/5); w2=w**2
a=1/phi**3; b=1/phi**2

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.6,6.8),dpi=150,gridspec_kw={"width_ratios":[1,1.12]})

# ---- 左：复平面矢量三角形 ----
P0=0j; P1=a*w; P2=a*w-b*w2
ax.annotate("",xy=(P1.real,P1.imag),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",color="#c0392b",lw=3.0,mutation_scale=20))
ax.annotate("",xy=(P2.real,P2.imag),xytext=(P1.real,P1.imag),arrowprops=dict(arrowstyle="-|>",color="#2c5f8a",lw=3.0,mutation_scale=20))
ax.annotate("",xy=(P2.real,P2.imag),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",color="#27865a",lw=2.6,ls="--",mutation_scale=20))
ax.plot([-0.05,0.46],[0,0],color="#ccc",lw=1.4)
ax.plot([P2.real],[0],"o",color="#27865a",ms=11,zorder=6)
ax.text(P1.real/2-0.02,P1.imag/2+0.03,f"aω\n|aω|=1/φ³={a:.4f}",fontsize=10.5,color="#c0392b",weight="bold",ha="center")
ax.text((P1.real+P2.real)/2+0.05,(P1.imag+P2.imag)/2-0.05,f"−bω²\n|bω²|=1/φ²={b:.4f}",fontsize=10.5,color="#2c5f8a",weight="bold",ha="left")
ax.text(0.40,-0.055,f"和 = d = {d:.4f}\n（落在实轴上）",fontsize=11,color="#27865a",weight="bold",ha="right",va="top")
ax.text(0.02,0.30,"虚部恰好相消：\na·sin72° = b·sin144°\n→ 生/克 = 1/φ",fontsize=10.6,color="#333",weight="bold",
        bbox=dict(boxstyle="round,pad=0.42",fc="#fbfcfd",ec="#aab",lw=1.3))
ax.set_xlim(-0.05,0.47); ax.set_ylim(-0.16,0.34); ax.set_aspect("equal")
ax.set_xlabel("Re",fontsize=11); ax.set_ylabel("Im",fontsize=11)
ax.set_title("θ=0° 的矢量图：两条边虚部相消，落在实轴上",fontsize=12.3,weight="bold",pad=10)
ax.grid(alpha=.22)

# ---- 右：在 b=d 直线上扫 a ----
aa=np.linspace(0.10,0.40,500)
L1=(1-d)+aa*w-b*w2
ax2.plot(aa,L1.real,color="#2c5f8a",lw=3,label="Re λ1")
ax2.plot(aa,L1.imag,color="#c0392b",lw=3,label="Im λ1")
ax2.axhline(0,color="#999",lw=1.2); ax2.axhline(1,color="#999",lw=1.2,ls=":")
ax2.axvline(a,color="#27865a",ls="-.",lw=2)
ax2.plot(a,0,"o",color="#c0392b",ms=11,mec="white",mew=1.8,zorder=6)
ax2.plot(a,1,"o",color="#2c5f8a",ms=11,mec="white",mew=1.8,zorder=6)
ax2.annotate(f"a = d/φ = 1/φ³ = {a:.6f}\nIm 归零 且 Re = 1（同一处）",(a,0),textcoords="offset points",
             xytext=(24,-56),fontsize=10.4,color="#27865a",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#27865a"),
             bbox=dict(boxstyle="round,pad=0.42",fc="#f2faf6",ec="#27865a",lw=1.4))
ax2.text(0.115,1.55,"b 固定 = d = 1/φ²",fontsize=10,color="#333",
         bbox=dict(boxstyle="round,pad=0.32",fc="#fbfcfd",ec="#aab",lw=1.1))
ax2.legend(fontsize=10.5,loc="center right")
ax2.set_xlabel("相生强度 a（固定 b = d = 1/φ²）",fontsize=11); ax2.set_ylabel("λ1 的分量",fontsize=11)
ax2.set_title("两条曲线在同一 a 处同时命中",fontsize=12.3,weight="bold",pad=10)
ax2.set_ylim(-0.55,1.85); ax2.set_xlim(0.10,0.40); ax2.grid(alpha=.22)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/theta0_meaning.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/theta0_meaning.png")
