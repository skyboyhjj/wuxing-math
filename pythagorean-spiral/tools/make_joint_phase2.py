#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""联合相图（加强版）：5 个模式的临界面 + R^n 尺度阶梯"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; w=np.exp(2j*np.pi/5); d=q
def lam(a,b,k): return (1-d)+a*w**k-b*w**(2*k)

fig,(ax,ax2)=plt.subplots(1,2,figsize=(16.0,7.8),dpi=150,gridspec_kw={"width_ratios":[1.45,1]})

A,B=np.meshgrid(np.linspace(-0.15,1.55,700), np.linspace(-0.32,1.05,700))
L={k:np.abs(lam(A,B,k)) for k in range(5)}
ax.contourf(A,B,np.minimum.reduce([L[0],L[1],L[2]]),levels=[0,0.6,1.0,1.6,2.6],
            colors=["#e8eef5","#f3f7fa","#fdf0ec","#f9dcd4"],alpha=.75)
ax.contour(A,B,L[0],levels=[1.0],colors="#2c5f8a",linewidths=2.4)
ax.contour(A,B,L[1],levels=[1.0],colors="#c0392b",linewidths=2.4)
ax.contour(A,B,L[2],levels=[1.0],colors="#8e44ad",linewidths=2.4,linestyles="--")

ax.plot(1/phi**2,0,"s",color="#2c5f8a",ms=8,zorder=7)
ax.annotate("a=1/φ²\n(均匀模临界)",(1/phi**2,0),textcoords="offset points",xytext=(-52,-16),
            fontsize=9.5,color="#2c5f8a",ha="center",arrowprops=dict(arrowstyle="->",color="#2c5f8a"))
ax.plot(1/phi,0,"*",color="#27865a",ms=24,zorder=9)
ax.annotate("五角星点 a=1/φ\nλ1=e^(i36°)（相生临界）",(1/phi,0),textcoords="offset points",
            xytext=(2,-68),fontsize=9.8,color="#27865a",ha="center",
            arrowprops=dict(arrowstyle="->",color="#27865a"),zorder=9)
ax.plot(0.535,0.153,"o",color="#e67e22",ms=11,zorder=8)
ax.annotate("双临界点 (0.535,0.153)\n= 均匀模 ∩ 相生模",(0.535,0.153),textcoords="offset points",
            xytext=(34,20),fontsize=9.8,color="#e67e22",
            arrowprops=dict(arrowstyle="->",color="#e67e22"))

h=[Line2D([0],[0],color="#2c5f8a",lw=2.4,label="k=0  均匀模  |λ0|=1"),
   Line2D([0],[0],color="#c0392b",lw=2.4,label="k=1/4  相生 · 子病及母  |λ1|=|λ4|=1"),
   Line2D([0],[0],color="#8e44ad",lw=2.4,ls="--",label="k=2/3  相克 · 相侮  |λ2|=|λ3|=1")]
ax.legend(handles=h,fontsize=10,ncol=3,loc="upper center",bbox_to_anchor=(0.5,-0.13),framealpha=.95)
ax.set_xlabel("相生强度 a",fontsize=11.5); ax.set_ylabel("相克强度 b",fontsize=11.5)
ax.set_title("联合相图（5 个不可约表示）　固定 d = 1/φ² ≈ 0.382",fontsize=12.5,weight="bold",pad=10)
ax.grid(alpha=.2); ax.set_xlim(-0.15,1.55); ax.set_ylim(-0.32,1.05)
ax.text(0.03,0.99,"五角星点上：\n|λ0| = 2/φ = 1.236（过载）\n|λ1| = |λ4| = 1（临界）\n|λ2| = |λ3| = 1/φ² = 0.382（衰减）",
        transform=ax.transAxes,fontsize=9.8,ha="left",va="top",
        bbox=dict(boxstyle="round,pad=0.45",fc="#fffdf5",ec="#c9a227",lw=1.4))

ns=np.arange(1,6); sc=1/phi**(4*ns)
names=["相生
R1","相克
R2","相侮
R3","子病及母
R4","复原
R5"]
ax2.bar(range(1,6),sc,color=["#27865a","#8e44ad","#8e44ad","#c0392b","#95a5a6"],alpha=.9,width=.62)
ax2.set_yscale("log")
for n,s in zip(ns,sc):
    ax2.text(n,s*1.6,f"1/φ^{4*n}\n= {s:.2e}",ha="center",fontsize=9.6,weight="bold")
ax2.set_xticks(range(1,6)); ax2.set_xticklabels(names,fontsize=10.5)
ax2.set_ylim(1.5e-5,3.0)
ax2.set_ylabel("五行链第 n 步的振幅   |T^(2n)| = 1/φ^(4n)",fontsize=11)
ax2.set_title("R^n 的尺度：每走一步五行关系，振幅 × 1/φ^4",fontsize=12.5,weight="bold",pad=10)
ax2.grid(alpha=.25,axis="y",which="both")
ax2.text(3.0,2.2e-5,"⇒ 相克 / 相侮 / 子病及母 相对相生\n    是 1/φ^4、1/φ^8、1/φ^12 级的深层微扰",
         ha="center",fontsize=10.2,color="#8e44ad",
         bbox=dict(boxstyle="round,pad=0.45",fc="#faf5ff",ec="#8e44ad",lw=1.2))

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/joint_phase_rscale.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/joint_phase_rscale.png")
