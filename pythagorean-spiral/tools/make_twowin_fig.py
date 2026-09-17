#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""总量饱和 c 的两全作用：压住 λ0，不动 λ1"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; d=q; a=1/phi; w=np.exp(2j*np.pi/5)
cs=1/phi**3

fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.4,6.8),dpi=150,gridspec_kw={"width_ratios":[1.1,1]})

# ---- 左：|λ0|、|λ1| vs c ----
C=np.linspace(0,0.55,500); L0=np.abs(1-d+a-C); L1=np.full_like(C,1.0)
ax.plot(C,L0,color="#c0392b",lw=3,label="均匀模 |λ0| = 1−d+a−c")
ax.plot(C,L1,color="#27865a",lw=3,ls="--",label="相生模 |λ1| = 1（纹丝不动）")
ax.axhline(1,color="#7f8c8d",ls=":",lw=1.5)
ax.axvline(cs,color="#8e44ad",ls="-.",lw=2)
ax.plot(cs,1,"o",color="#8e44ad",ms=13,mec="white",mew=2,zorder=6)
ax.annotate(f"c* = 1/φ³ = {cs:.6f}\n两全点：|λ0|=|λ1|=1",(cs,1),textcoords="offset points",
            xytext=(26,-80),fontsize=11,color="#8e44ad",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#8e44ad"),
            bbox=dict(boxstyle="round,pad=0.4",fc="#faf5ff",ec="#8e44ad",lw=1.4))
ax.fill_between(C,0,1,where=(L0<=1),color="#d6f0e0",alpha=.55)
ax.text(0.42,0.72,"稳定区（c>c*）",fontsize=10.5,color="#27865a",weight="bold")
ax.text(0.03,1.19,"过载区（c<c*）",fontsize=10.5,color="#c0392b",weight="bold")
ax.legend(fontsize=10.5,loc="upper right")
ax.set_xlabel("总量饱和强度 c",fontsize=11.5); ax.set_ylabel("模",fontsize=11.5)
ax.set_title("总量饱和 c：只压均匀模，不碰相生模",fontsize=12.6,weight="bold",pad=10)
ax.set_ylim(0.44,1.32); ax.set_xlim(0,0.55); ax.grid(alpha=.22)

# ---- 右：复平面谱 ----
th=np.linspace(0,2*np.pi,400); ax2.plot(np.cos(th),np.sin(th),color="#95a5a6",lw=1.4,ls="--")
L0v=1-d+a
P=[("λ0（c=0，过载）",L0v,"#c0392b","^"),
   ("λ1 = e^(i36°)",np.exp(1j*np.deg2rad(36)),"#27865a","o"),
   ("λ4 = e^(−i36°)",np.exp(-1j*np.deg2rad(36)),"#1f7a4d","o"),
   ("λ2 = (1/φ²)e^(i72°)",q*np.exp(1j*np.deg2rad(72)),"#8e44ad","s"),
   ("λ3 = (1/φ²)e^(−i72°)",q*np.exp(-1j*np.deg2rad(72)),"#8e44ad","s"),
   ("λ0（补 c* 后）",1.0,"#e67e22","*")]
for txt,z,c,m in P:
    ax2.plot(z.real,z.imag,m,color=c,ms=(20 if m=="*" else 11),mec="white",mew=1.6,zorder=5)
for txt,z,dx,dy in [("λ0(c=0)=2/φ",complex(L0v,0),6,12),("λ1=e^(i36°)",np.exp(1j*np.deg2rad(36)),6,-24),
                    ("λ4=e^(−i36°)",np.exp(-1j*np.deg2rad(36)),-16,-30),
                    ("λ2",q*np.exp(1j*np.deg2rad(72)),8,10),
                    ("λ3",q*np.exp(-1j*np.deg2rad(72)),8,-18),
                    ("λ0(c*)",1.0,-4,-34)]:
    ax2.annotate(txt,xy=(z.real,z.imag),textcoords="offset points",xytext=(dx,dy),fontsize=9.6,ha="center",weight="bold")
ax2.plot([0,0],[-1.35,1.35],color="#ddd",lw=1); ax2.plot([-1.35,1.35],[0,0],color="#ddd",lw=1)
ax2.set_aspect("equal"); ax2.set_xlim(-1.62,1.72); ax2.set_ylim(-1.62,1.62)
ax2.set_title("补上 c* 后的谱（a=1/φ, d=1/φ²）",fontsize=12.6,weight="bold",pad=10)
ax2.grid(alpha=.18)
ax2.text(-1.52,1.42,"两个临界（±36°）、两个衰减（1/φ²）、一个归位（1）",
         fontsize=9.8,color="#333",bbox=dict(boxstyle="round,pad=0.35",fc="#fbfcfd",ec="#aab"))
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/nonlinear_twowin.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/nonlinear_twowin.png")
