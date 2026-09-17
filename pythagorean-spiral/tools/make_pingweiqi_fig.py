#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""以平为期：不转射线 × 中性点 × 稳定域"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; d=q; w=np.exp(2j*np.pi/5)
fig,(ax,ax2)=plt.subplots(1,2,figsize=(15.8,6.9),dpi=150,gridspec_kw={"width_ratios":[1.1,1]})

# ---- 左：稳定域 + 不转射线 ----
A,B=np.meshgrid(np.linspace(-0.1,1.2,700),np.linspace(-0.5,1.0,700))
M=np.full_like(A,True,dtype=bool)
for k in range(5): M &= (np.abs((1-d)+A*w**k-B*w**(2*k))<=1+1e-7)
ax.contourf(A,B,M.astype(float),levels=[0.5,1.5],colors=["#e6f4ec"],alpha=.95)
aa=np.linspace(0,0.75,300); ax.plot(aa,phi*aa,color="#c0392b",lw=3,label="不转射线  b = φa（相位恒 0）")
ax.plot(1/phi**3,1/phi**2,"*",color="#f1c40f",ms=26,mec="#7d6608",mew=1.8,zorder=8)
ax.annotate("（平）\n(1/φ³, 1/φ²)\n不转 且 不增不衰",(1/phi**3,1/phi**2),textcoords="offset points",
            xytext=(42,-30),fontsize=10.2,color="#7d6608",weight="bold",
            arrowprops=dict(arrowstyle="->",color="#7d6608"),
            bbox=dict(boxstyle="round,pad=0.4",fc="#fffdf0",ec="#c9a227",lw=1.4))
ax.plot(1/phi,0,"^",color="#8e44ad",ms=14,mec="white",mew=1.6,zorder=7)
ax.annotate("五角星点（不稳，|λ0|=2/φ）",(1/phi,0),textcoords="offset points",xytext=(14,30),
            fontsize=9.8,color="#8e44ad",weight="bold",arrowprops=dict(arrowstyle="->",color="#8e44ad"))
ax.text(0.60,0.30,"灰色 = 稳定域 |λk| ≤ 1（∀k）",fontsize=10,color="#1f7a4d",weight="bold",
        bbox=dict(boxstyle="round,pad=0.35",fc="white",ec="#1f7a4d",lw=1.2))
ax.text(0.30,0.60,"射线在\n（平）处穿出\n稳定域",fontsize=9.6,color="#c0392b",weight="bold")
ax.set_xlim(-0.1,1.05); ax.set_ylim(-0.45,0.95); ax.grid(alpha=.2)
ax.set_xlabel("相生 a（亢）",fontsize=11); ax.set_ylabel("相克 b（承）",fontsize=11)
ax.set_title("“以平为期”：不转射线与稳定域只交于一点",fontsize=12.4,weight="bold",pad=10)
ax.legend(fontsize=10,loc="upper left")

# ---- 右：沿射线扫 a ----
aa=np.linspace(0.02,0.45,500); bb=phi*aa
L1=np.array([(1-d)+a*w-b*w**2 for a,b in zip(aa,bb)]).real
L0=np.abs((1-d)+aa-bb); L2=np.abs((1-d)+aa*w**2-bb*w**4)
ax2.plot(aa,L1,color="#c0392b",lw=3,label="λ1（实数）")
ax2.plot(aa,L0,color="#2c5f8a",lw=2,ls="--",label="|λ0|")
ax2.plot(aa,L2,color="#8e44ad",lw=2,ls=":",label="|λ2|")
ax2.axhline(1,color="#7f8c8d",ls=":",lw=1.5)
ax2.axvline(1/phi**3,color="#f1c40f",ls="-.",lw=2.4)
ax2.plot(1/phi**3,1,"*",color="#f1c40f",ms=24,mec="#7d6608",mew=1.6,zorder=7)
ax2.annotate("a = d/φ = 1/φ³\nλ1 恰好 = 1（平）",(1/phi**3,1),textcoords="offset points",
             xytext=(22,-52),fontsize=10.2,color="#7d6608",weight="bold",
             arrowprops=dict(arrowstyle="->",color="#7d6608"),
             bbox=dict(boxstyle="round,pad=0.4",fc="#fffdf0",ec="#c9a227",lw=1.4))
ax2.fill_between(aa,0,1.6,where=(aa<1/phi**3),color="#e8f1fb",alpha=.7)
ax2.fill_between(aa,0,1.6,where=(aa>1/phi**3),color="#fdeceb",alpha=.7)
ax2.text(0.09,1.42,"不及（λ1<1，衰减）",fontsize=10,color="#2c5f8a",weight="bold")
ax2.text(0.28,1.42,"太过（λ1>1，增长）",fontsize=10,color="#c0392b",weight="bold")
ax2.set_xlim(0.02,0.45); ax2.set_ylim(0.25,1.6); ax2.grid(alpha=.22)
ax2.set_xlabel("沿不转射线的相生 a（此时 b = φa）",fontsize=11); ax2.set_ylabel("特征值",fontsize=11)
ax2.set_title("沿射线：不及 → 平 → 太过",fontsize=12.4,weight="bold",pad=10)
ax2.legend(fontsize=10,loc="lower right")
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/pingweiqi.png",bbox_inches="tight",facecolor="white",pad_inches=0.25)
print("已生成 output/pingweiqi.png")
