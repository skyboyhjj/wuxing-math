#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""黄金配比：a+d=1 ⟹ χ=a−d=1/φ³（差=积）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2
a=1/phi; d=1/phi**2; chi=1/phi**3
fig,ax=plt.subplots(figsize=(11.4,6.4),dpi=160)
ax.set_xlim(-0.06,1.16); ax.set_ylim(0,1.0); ax.axis("off")

# 总长 1 的横条
ax.add_patch(Rectangle((0,0.60),a,0.16,fc="#c0392b",ec="none"))
ax.add_patch(Rectangle((a,0.60),d,0.16,fc="#2c5f8a",ec="none"))
ax.text(a/2,0.68,f"a = 1/φ = {a:.4f}\n（相生）",ha="center",va="center",color="white",fontsize=11.5,weight="bold")
ax.text(a+d/2,0.68,f"d = 1/φ² = {d:.4f}\n（衰减）",ha="center",va="center",color="white",fontsize=11.5,weight="bold")
ax.text(0.5,0.845,"a + d = 1.000000   ← 黄金分割方程  x² + x = 1",ha="center",fontsize=12,weight="bold",color="#333")

# 差值区间 a-d
ax.plot([d,d],[0.44,0.60],color="#27865a",lw=1.6)
ax.plot([a,a],[0.44,0.60],color="#27865a",lw=1.6)
arr=FancyArrowPatch((d,0.50),(a,0.50),arrowstyle="<->",color="#27865a",lw=2.2,mutation_scale=16)
ax.add_patch(arr)
ax.text((a+d)/2,0.40,f"a − d = χ = 1/φ³ = {chi:.6f}",ha="center",fontsize=12.5,color="#27865a",weight="bold")

# 乘积说明
ax.text(0.5,0.20,"并且   (1/φ)·(1/φ²) = 1/φ³     —— 【差】与【积】是同一个数！",
        ha="center",fontsize=12,color="#444",
        bbox=dict(boxstyle="round,pad=0.5",fc="#f7f8fa",ec="#d0d4da"))

# 标题
ax.text(0.5,0.94,"χ = 1/φ³ 的物理读法：手性 = 生 − 衰",
        ha="center",fontsize=14.5,weight="bold")
ax.text(0.5,0.075,"只要『生衰配比金』(a+d=1)，手性 χ 就【自动】= 1/φ³ —— 不必外部给定",
        ha="center",fontsize=11.5,color="#c0392b")
plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/chi_golden_ratio.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/chi_golden_ratio.png")
