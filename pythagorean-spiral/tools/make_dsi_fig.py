#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""闭环：五角星层级步（缩放 q + 旋转 36°）⇒ 周期 5 的对数周期调制"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; lnq=abs(np.log(q)); th=np.radians(36.0)
N=60; n=np.arange(N)

u=q**n*np.cos(n*th);      res=np.log(np.abs(u)+1e-300)-np.polyval(np.polyfit(n,np.log(np.abs(u)+1e-300),1),n)
u0=q**n;                  res0=np.log(u0)-np.polyval(np.polyfit(n,np.log(u0),1),n)

fig,ax=plt.subplots(1,2,figsize=(13.4,5.8),dpi=155)

ax[0].plot(n,res,"-o",color="#c0392b",lw=1.8,ms=5,label="有旋转 36°（五角星步）")
ax[0].plot(n,res0,"-s",color="#9aa0a6",lw=1.6,ms=6,label="无旋转（只缩放）")
for k in range(0,N,5): ax[0].axvline(k,color="#d5d8dd",lw=.9,zorder=0)
ax[0].set_xlabel("层级序号 n",fontsize=11); ax[0].set_ylabel("去趋势后的 ln|u|",fontsize=11)
ax[0].set_title("五角星层级步 ⇒ 【周期 5】的对数周期调制\n（灰线：去掉旋转即完全消失）",fontsize=12.5,weight="bold",pad=12)
ax[0].legend(fontsize=10); ax[0].grid(alpha=.25)

fs=np.linspace(0.005,0.5,3000)
P =np.array([abs((res *np.exp(-2j*np.pi*f*n)).sum())**2 for f in fs]); P/=P.max()
P0=np.array([abs((res0*np.exp(-2j*np.pi*f*n)).sum())**2 for f in fs]); P0/=max(P0.max(),1e-30)
ax[1].plot(fs,P,color="#c0392b",lw=1.9,label="有旋转 36°")
ax[1].plot(fs,P0,color="#9aa0a6",lw=1.6,label="无旋转")
ax[1].axvline(1/5,color="#2c5f8a",ls="--",lw=1.8,label="f = 1/5（周期 5）")
ax[1].set_xlabel("频率（1/n）",fontsize=11); ax[1].set_ylabel("归一化谱强度",fontsize=11)
ax[1].set_title("谱：旋转把主峰钉在 f = 1/5\n（灰线无峰）",fontsize=12.5,weight="bold",pad=12)
ax[1].legend(fontsize=10); ax[1].grid(alpha=.25)

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/pentagon_hierarchy_dsi.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/pentagon_hierarchy_dsi.png")
