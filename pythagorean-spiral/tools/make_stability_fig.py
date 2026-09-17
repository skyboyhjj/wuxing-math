#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""稳定性判据修正：d>a 只在 d≤1 成立；d>1 有上界"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; w=np.exp(2j*np.pi/5)
A,D=np.meshgrid(np.linspace(0,1.1,700),np.linspace(0,2.4,700))
R=np.maximum.reduce([np.abs((1-D)+A*w**k) for k in range(5)])
STABLE=R<1.0                       # 真实稳定域
NAIVE=(D>A)                        # 原（错误）判据

fig,ax=plt.subplots(figsize=(9.6,7.4),dpi=160)
# 真实稳定域（绿）
ax.contourf(A,D,STABLE.astype(float),levels=[0.5,1.5],colors=["#d6f0e0"])
# 假阳性区：d>a 但实际不稳（红）
FP=NAIVE&(~STABLE)
ax.contourf(A,D,FP.astype(float),levels=[0.5,1.5],colors=["#f9d7d2"])
ax.contour(A,D,R,levels=[1.0],colors="#1f7a4d",linewidths=2.6)
ax.plot([0,1.1],[0,1.1],color="#c0392b",lw=2.6,ls="--")     # d = a
ax.axhline(1.0,color="#2c5f8a",lw=2.0,ls=":")

# u(a) 上界
aa=np.linspace(0,0.999,300); uu=(np.sqrt(4-(3-phi)*aa**2)-phi*aa)/2
ax.plot(aa,1+uu,color="#1f7a4d",lw=2.4)

ax.plot(1/phi,1/phi**2,"*",color="#f1c40f",ms=24,mec="#7d6608",mew=1.8,zorder=8)
ax.annotate("黄金点 (1/φ, 1/φ²)\n在过载侧（λ0=2/φ>1）\n—— 正由 §4 的 c 项救回",
            (1/phi,1/phi**2),textcoords="offset points",xytext=(34,44),fontsize=10,color="#7d6608",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#7d6608"),
            bbox=dict(boxstyle="round,pad=0.4",fc="#fffdf0",ec="#c9a227",lw=1.4))
ax.annotate("原判据 d > a\n（红虚线）",(0.95,0.98),textcoords="offset points",xytext=(14,16),
            fontsize=10.4,color="#c0392b",weight="bold")
ax.annotate("新上界 d = 1 + u(a)",(0.42,1.62),textcoords="offset points",xytext=(18,10),
            fontsize=10.4,color="#1f7a4d",weight="bold",arrowprops=dict(arrowstyle="->",color="#1f7a4d"))
ax.text(0.06,0.62,"绿色 = 真实稳定域 ρ<1\n红色 = 假阳性（d>a 却 ρ>1）\n蓝虚线 d=1：k=0 不再取最大的分界",
        fontsize=10,color="#333",bbox=dict(boxstyle="round,pad=0.45",fc="#fbfcfd",ec="#aab",lw=1.2))
ax.set_xlim(0,1.1); ax.set_ylim(0,2.4)
ax.set_xlabel("相生强度 a",fontsize=11.5); ax.set_ylabel("衰减系数 d",fontsize=11.5)
ax.set_title("稳定性判据修正：d>a 仅在 d≤1 成立；d>1 时 d 有上界",fontsize=13,weight="bold",pad=12)
ax.grid(alpha=.2)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/stability_region_ad.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/stability_region_ad.png")
