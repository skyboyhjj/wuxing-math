# -*- coding: utf-8 -*-
import os as _os
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans SC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4))

# ---------- 左：五节点环 C5（实线相生，虚线相克） ----------
ax = axes[0]
labels = ['木', '火', '土', '金', '水']
pts = [(math.cos(math.radians(90 - 72 * i)), math.sin(math.radians(90 - 72 * i))) for i in range(5)]
for i in range(5):                      # 相生：环边
    x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 5]
    ax.plot([x1, x2], [y1, y2], color='#27ae60', lw=2.4, zorder=1)
for i in range(5):                      # 相克：隔一节点的弦
    x1, y1 = pts[i]; x2, y2 = pts[(i + 2) % 5]
    ax.plot([x1, x2], [y1, y2], color='#e67e22', lw=1.4, ls='--', zorder=1)
for i, (x, y) in enumerate(pts):
    ax.scatter([x], [y], s=950, color='#2c3e50', zorder=3)
    ax.text(x, y, labels[i], ha='center', va='center', fontsize=15, color='white', zorder=4)
ax.set_title('五行 = 五节点环 C5\n（实线：相生 / 虚线：相克）', fontsize=13)
ax.axis('equal'); ax.axis('off')

# ---------- 右：特征值谱 ----------
ax = axes[1]
ev = [0.0, 1.381966, 1.381966, 3.618034, 3.618034]
colors = ['#c0392b', '#2980b9', '#2980b9', '#8e44ad', '#8e44ad']
ax.bar(range(1, 6), ev, color=colors, width=0.6)
for i, v in enumerate(ev):
    ax.text(i + 1, v + 0.07, '%.4f' % v, ha='center', fontsize=10)
ax.axhline(0, color='k', lw=0.8)
ax.set_title('Cartan 矩阵 A 的特征值谱\n（半正定：1 个零根 + 4 个正根）', fontsize=13)
ax.set_xlabel('模态序号', fontsize=11)
ax.set_ylabel('特征根 λ', fontsize=11)
ax.set_ylim(0, 4.3)
ax.text(1.35, 4.15, 'λ = 2 + φ 与 2 − 1/φ   (φ = 黄金比 1.6180)\n2 + φ   = 3.6180 (二重)\n2 − 1/φ = 1.3820 (二重)',
        fontsize=9.5, va='top')
ax.annotate('零根 δ（仿射型标志）', xy=(1, 0), xytext=(1.55, 0.6), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='#c0392b'))

plt.tight_layout()
plt.savefig(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'figures', 'fig_cartan.png'), dpi=160, bbox_inches='tight')
print('saved')
