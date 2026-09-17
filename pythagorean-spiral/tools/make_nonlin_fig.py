#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对照：立方饱和（会混合各模） vs 总量饱和（只作用于均匀模）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; a=1/phi; d=q
S=np.zeros((5,5))
for i in range(5): S[i,(i-1)%5]=1
I=np.eye(5); J1=np.ones((5,5))

cA=0.5
m=np.sqrt((a-d)/(5*cA)); x=np.ones(5)*m
JA=(1-d)*I+a*S-cA*(np.dot(x,x)*I+2*np.outer(x,x))
cB=0.5
JB=(1-d)*I+a*S-(cB/5)*J1

fig,ax=plt.subplots(1,2,figsize=(13.2,6.0),dpi=155)
t=np.linspace(0,2*np.pi,300)
for k,(A,ttl) in enumerate([(JA,"候选A：立方饱和  N = −c|x|²x\n（混合各模 → λ1 被推离 36°）"),
                            (JB,"候选B：总量饱和  N = −c·mean(x)·1\n（只作用于均匀模 → λ1 保持 36°）")]):
    ax[k].plot(np.cos(t),np.sin(t),"--",color="#9aa0a6",lw=1.5,label="单位圆 |λ|=1")
    ax[k].axhline(0,color="#e6e6e6",lw=1); ax[k].axvline(0,color="#e6e6e6",lw=1)
    ev=np.linalg.eigvals(A)
    for z in ev:
        col="#c0392b" if abs(abs(z)-1)<1e-6 else ("#27865a" if abs(z)<1 else "#8e44ad")
        ax[k].plot([0,z.real],[0,z.imag],"-",color=col,lw=1.6,alpha=.75)
        ax[k].plot([z.real],[z.imag],"o",color=col,ms=10,zorder=5)
    ang=np.radians(36)
    ax[k].plot([0,1.2*np.cos(ang)],[0,1.2*np.sin(ang)],":",color="#2c5f8a",lw=1.6,label="36°（五角星步）")
    ax[k].set_xlim(-1.6,1.8); ax[k].set_ylim(-1.3,1.3); ax[k].set_aspect("equal")
    ax[k].set_title(ttl,fontsize=12,weight="bold",pad=12)
    ax[k].set_xlabel("Re λ",fontsize=10.5); ax[k].set_ylabel("Im λ",fontsize=10.5)
    ax[k].legend(fontsize=9.5,loc="lower left"); ax[k].grid(alpha=.2)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/wuxing_nonlinear_choice.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/wuxing_nonlinear_choice.png")
