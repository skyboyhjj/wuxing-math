#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五行动力学的临界谱：λ_1 = e^(i36°)（五角星步），λ_0 = 2/φ（过载）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2
a=1/phi; d=q
L=[(1-d)+a*np.exp(2j*np.pi*k/5) for k in range(5)]

fig,ax=plt.subplots(figsize=(8.6,8.0),dpi=160)
t=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(t),np.sin(t),"--",color="#9aa0a6",lw=1.6,label="单位圆 |λ|=1（临界）")
ax.axhline(0,color="#e0e0e0",lw=1); ax.axvline(0,color="#e0e0e0",lw=1)

cols={0:"#c0392b",1:"#27865a",2:"#2c5f8a",3:"#2c5f8a",4:"#27865a"}
labs={0:"λ0 = 2/φ ≈ 1.236（过载，不稳定）",
      1:"λ1 = e^(i36°)（五角星步，临界）",
      2:"λ2 = q·e^(i72°)（收缩）",
      3:"λ3 = q·e^(−i72°)",
      4:"λ4 = e^(−i36°)"}
for k in range(5):
    z=L[k]
    ax.plot([0,z.real],[0,z.imag],"-",color=cols[k],lw=2.0,alpha=.8)
    ax.plot([z.real],[z.imag],"o",color=cols[k],ms=11,zorder=5)
    ax.annotate(labs[k],xy=(z.real,z.imag),xytext=(z.real+(0.10 if z.real>=0 else -0.10), z.imag+0.17),
                fontsize=10,color=cols[k],
                ha="left" if z.real>=0 else "right",
                arrowprops=dict(arrowstyle="-",color=cols[k],lw=.8))

# 36° 角标记
ang=np.radians(36)
ax.plot([0,1.25*np.cos(ang)],[0,1.25*np.sin(ang)],":",color="#27865a",lw=1.2)
ax.text(1.05*np.cos(ang/2),1.05*np.sin(ang/2),"36°",color="#27865a",fontsize=11)

ax.set_xlim(-1.9,2.3); ax.set_ylim(-1.7,1.7); ax.set_aspect("equal")
ax.set_xlabel("Re λ",fontsize=11); ax.set_ylabel("Im λ",fontsize=11)
ax.set_title("五行动力学的临界谱  a=1/φ, d=1/φ²  (a+d=1)\n"
             "k=1 模式恰为五角星步 e^(i36°)；k=0 过载（= 原稿『只有相生会过载』）",
             fontsize=12.5,weight="bold",pad=14)
ax.legend(fontsize=10,loc="lower left"); ax.grid(alpha=.2)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/wuxing_critical_spectrum.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/wuxing_critical_spectrum.png")
