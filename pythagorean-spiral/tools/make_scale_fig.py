#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""标度不变性示意：离散标度不变（DSI）及其对数周期签名"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2
fig=plt.figure(figsize=(13.2,6.4),dpi=155)

# --- 左：极坐标螺旋 + 72° 辐条（离散层）---
ax=fig.add_subplot(1,2,1,projection="polar")
th=np.linspace(0,4*np.pi,2000)
r=q**(th/np.radians(72))
ax.plot(th,r,color="#c0392b",lw=2.0)
for k in range(11):
    a=np.radians(72*k)
    rk=q**(k)
    ax.plot([a],[rk],"o",color="#2c5f8a",ms=6,zorder=5)
ax.set_rmax(1.05); ax.set_rticks([0.25,0.5,0.75,1.0])
ax.set_title("离散层：每 72° 半径 ×q\n（q = 1/φ² ≈ 0.382）",fontsize=12.5,weight="bold",pad=18)
ax.grid(alpha=.3)

# --- 右：ln r 对 θ 是直线（等步长 → 对数周期）---
ax2=fig.add_subplot(1,2,2)
sp=np.arange(0,11)
thd=72*sp; lnr=sp*np.log(q)
ax2.plot(thd,lnr,"-o",color="#c0392b",lw=2.0,ms=6,label=r"$\ln r$（本结构：等步长）")
for k in sp:
    ax2.axvline(72*k,color="#d5d8dd",lw=.8,zorder=0)
ax2.axhline(0,color="#aaa",lw=.8)
ax2.set_xlabel("累计转角 θ（度）",fontsize=11)
ax2.set_ylabel("ln r",fontsize=11)
ax2.set_title("对数周期签名：Δln r 每 72° 恒为 ln q\n→ 幂律 + 对数周期（DSI）",fontsize=12.5,weight="bold",pad=14)
ax2.annotate("",xy=(72,np.log(q)),xytext=(0,0),
             arrowprops=dict(arrowstyle="<->",color="#2c5f8a",lw=1.6))
ax2.text(40,-0.35,"Δ = ln q\n(常数)",color="#2c5f8a",fontsize=10.5)
ax2.text(72*5,lnr[5]-2.2,"若为【连续】标度不变：\n任意 λ 都保持结构（无此周期）",
         fontsize=10,color="#555")
ax2.legend(fontsize=10,loc="lower left")
ax2.grid(alpha=.25)

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/wuxing_scale_invariance.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/wuxing_scale_invariance.png")
