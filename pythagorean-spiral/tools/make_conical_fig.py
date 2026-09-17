#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三维锥形对数螺旋：五行五大元素轨迹（对应图 6/10）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

q=0.8; R0=1.0; H=1.0            # 每层：半径×q，高度+h
names=["火","木","水","金","土"]; cols=["#c0392b","#27865a","#2c5f8a","#c9a227","#a0522d"]

fig=plt.figure(figsize=(9.2,8.2),dpi=160); ax=fig.add_subplot(111,projection="3d")

n=np.linspace(0,5.0,600)
for k in range(5):
    th=np.radians(90+72*n+72*k)          # 每条曲线的方位
    r=R0*q**n
    x=r*np.cos(th); y=r*np.sin(th); z=H*n
    ax.plot(x,y,z,color=cols[k],lw=2.2,label=f"{names[k]}的螺旋轨迹")

# 整数层上的五边形（离散骨架）
for m in range(0,6):
    th=np.radians(90+72*m+72*np.arange(6))
    r=R0*q**m*np.ones(6)
    ax.plot(r*np.cos(th),r*np.sin(th),H*m*np.ones(6),color="#9aa0a6",lw=1.0,alpha=.55)

# 标出 火 在 n=0 与 n=5：同方位、不同半径
for m,c in ((0,"#c0392b"),(5,"#7b241c")):
    th=np.radians(90+72*m); r=R0*q**m
    ax.scatter([r*np.cos(th)],[r*np.sin(th)],[H*m],color=c,s=70,zorder=5)
    ax.text(r*np.cos(th),r*np.sin(th),H*m+0.12,f"火 n={m}",color=c,fontsize=10)

ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z（高度）")
ax.set_title("五行锥形螺旋：每层转 72°、半径 ×q\n（5 层回到同一方位，但半径已缩小 ⇒ 螺旋而非循环）",
             fontsize=13.5,weight="bold",pad=16)
ax.legend(loc="upper left",fontsize=9.5)
ax.view_init(elev=16,azim=-62)
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/wuxing_conical_spiral.png",bbox_inches="tight",facecolor="white",pad_inches=0.15)
print("已生成 output/wuxing_conical_spiral.png")
