#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""36° 临界线：a = 1/φ² + d/φ, b = d − 1/φ²（等价 a+b = φ·d）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; w=np.exp(2j*np.pi/5)
d=np.linspace(0,1,400)
a=1/phi**2+d/phi; b=d-1/phi**2

fig,ax=plt.subplots(figsize=(9.0,7.0),dpi=160)
ax.plot(a,b,color="#c0392b",lw=2.6,label="36° 临界线  (|λ1|=1, arg λ1=36°)")

# 特殊点：b=0（我们的五角星点）
d0=1/phi**2; a0=1/phi**2+d0/phi
ax.plot(a0,0,"*",color="#27865a",ms=22,zorder=6)
ax.annotate(f"五角星点\nb = 0, d = 1/φ²\na = 1/φ = {a0:.4f}\nλ1 = e^(i36°)",
            (a0,0),textcoords="offset points",xytext=(18,26),fontsize=10.5,color="#27865a",
            arrowprops=dict(arrowstyle="->",color="#27865a",lw=1.4))

# 采样几个 d
for dv in [0.2,0.65,0.9]:
    av=1/phi**2+dv/phi; bv=dv-1/phi**2
    ax.plot(av,bv,"o",color="#2c5f8a",ms=7,zorder=5)
    ax.text(av+0.012,bv-0.045,f"d={dv}",fontsize=9.5,color="#2c5f8a")

ax.axhline(0,color="#ccc",lw=1); ax.axvline(0,color="#ccc",lw=1)
ax.set_xlabel("相生强度 a",fontsize=12); ax.set_ylabel("相克强度 b",fontsize=12)
ax.set_title("“36° 临界线”：一整族参数都能让 λ1 落在五角星步上\n"
             "a = 1/φ² + d/φ ,  b = d − 1/φ²   （等价 a+b = φ·d）",
             fontsize=13,weight="bold",pad=14)
ax.legend(fontsize=11,loc="upper left"); ax.grid(alpha=.25)

# 角标：1/φ 的幂
ax.text(0.02,0.03,"1/φ 的三个幂：\n  相生 a = 1/φ\n  衰减 d = 1/φ²\n  手性 χ = 1/φ³",
        transform=ax.transAxes,fontsize=10.5,color="#444",
        bbox=dict(boxstyle="round,pad=0.4",fc="#f7f8fa",ec="#d0d4da"))
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/line36_critical.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/line36_critical.png")
