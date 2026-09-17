#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对数周期幂律（LPPL）：离散标度不变的可观测签名"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; L=np.log(q)
x=np.exp(np.linspace(0,6*abs(L)+0.001,4000))   # ln x 跨 6 个周期
alpha=-1.0
pure=x**alpha
lppl=x**alpha*(1+0.22*np.cos(2*np.pi*np.log(x)/L))

fig,ax=plt.subplots(1,2,figsize=(13.4,5.9),dpi=155)

ax[0].loglog(x,pure,color="#2c5f8a",lw=2.2,label="连续标度不变：纯幂律（α = −1）")
ax[0].loglog(x,lppl*1.0,color="#c0392b",lw=1.8,alpha=.9,label="离散标度不变：幂律 × 对数周期")
ax[0].set_xlabel("尺度 x（对数轴）",fontsize=11)
ax[0].set_ylabel("f(x)（对数轴）",fontsize=11)
ax[0].set_title("连续 SI → 直线；离散 SI → 直线 + 周期振荡",fontsize=12.5,weight="bold",pad=12)
ax[0].legend(fontsize=10); ax[0].grid(alpha=.25,which="both")

t=np.log(x)
ax[1].plot(t/abs(L),lppl/pure,color="#c0392b",lw=2.0)
ax[1].axhline(1,color="#2c5f8a",lw=1.6,ls="--",label="连续 SI：恒为 1（无振荡）")
for k in range(7):
    ax[1].axvline(k,color="#d5d8dd",lw=.8,zorder=0)
ax[1].set_xlabel("ln x / |ln q|   （以 ln q 为周期）",fontsize=11)
ax[1].set_ylabel("f(x) / x^α",fontsize=11)
ax[1].set_title("去掉幂律后：严格以 ln q 为周期的振荡\n（复临界指数 α + 2πik/ln q）",fontsize=12.5,weight="bold",pad=12)
ax[1].legend(fontsize=10); ax[1].grid(alpha=.25)

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/logperiodic_powerlaw.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/logperiodic_powerlaw.png")
