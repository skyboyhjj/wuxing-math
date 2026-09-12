# -*- coding: utf-8 -*-
import os as _os
"""
非线性化「乘侮」——观察临界线是否折叠（fold / 相变）
有效模型：dx/dt = D + x - mu * x^3
  D = a - b  为净驱动（相生 a 减去 相克 b）
  +x         为自身正反馈（自生/亢进）
  -mu x^3    为乘侮的【非线性】压制（亢盛时克制急剧增强，容量/饱和项）
平衡：D = mu x^3 - x   —— S 形曲线
折点：x = ±1/sqrt(3 mu) ，  |D| = (2/3)/sqrt(3 mu)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans SC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def D_of_x(x, mu): return mu * x**3 - x
def fold_D(mu):    return (2/3) / np.sqrt(3 * mu)

fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.2))

# ---------- (a) S 形分支图 ----------
ax = axes[0]
mu = 0.5
x = np.linspace(-2.4, 2.4, 800)
D = D_of_x(x, mu)
fp = 1 - 3 * mu * x**2
stable = fp < 0
ax.plot(D[stable], x[stable], 'b-', lw=2.2, label='稳定分支')
ax.plot(D[~stable], x[~stable], 'r--', lw=2.0, label='不稳定分支')
xf = 1 / np.sqrt(3 * mu); Df = fold_D(mu)
for s in (1, -1):
    ax.plot(s * Df, s * xf, 'ko', ms=8, zorder=5)
    ax.annotate('fold', (s * Df, s * xf), textcoords='offset points', xytext=(8, -4), fontsize=10)
ax.axvline(0, color='k', lw=0.5); ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel('净驱动 D = a − b'); ax.set_ylabel('平衡振幅 x')
ax.set_title(f'(a) 非线性乘侮下的 S 形分支（μ={mu}）')
ax.legend(fontsize=9)

# ---------- (b) 相变边界 (D, mu) ----------
ax = axes[1]
mu = np.linspace(0.12, 2.0, 400)
Df = fold_D(mu)
ax.plot(Df, mu, 'r-', lw=2.2)
ax.plot(-Df, mu, 'r-', lw=2.2, label='折叠线（相变边界）')
ax.fill_betweenx(mu, -Df, Df, color='#f7dc6f', alpha=0.55, label='双稳区（滞后 / 相变带）')
for m in (0.25, 0.5, 1.0):
    ax.axvline(0, color='gray', lw=0.0)
    ax.plot([fold_D(m), -fold_D(m)], [m, m], 'k:', lw=1)
    ax.annotate(f'μ={m}: |D|<{fold_D(m):.3f}', (fold_D(m), m), textcoords='offset points',
                xytext=(6, 4), fontsize=8.5)
ax.set_xlabel('净驱动 D = a − b'); ax.set_ylabel('乘侮非线性强度 μ')
ax.set_title('(b) 相变边界：折叠线夹出「双稳带」')
ax.legend(fontsize=9, loc='lower right')

# ---------- (c) 滞后回线 ----------
ax = axes[2]
mu = 0.5
def sweep(Ds):
    x = 1.5 if Ds[0] > Ds[-1] else -1.5
    out = []
    dt, relax = 0.05, 300
    for D in Ds:
        for _ in range(relax):
            x += dt * (D + x - mu * x**3)
        out.append(x)
    return np.array(out)
Ds_down = np.linspace(1.3, -1.3, 500)
Ds_up = np.linspace(-1.3, 1.3, 500)
xd, xu = sweep(Ds_down), sweep(Ds_up)
ax.plot(Ds_down, xd, 'b-', lw=2, label='D 从大到小')
ax.plot(Ds_up, xu, 'r-', lw=2, label='D 从小到大')
ax.axvline(0, color='k', lw=0.5)
ax.set_xlabel('净驱动 D = a − b'); ax.set_ylabel('平衡振幅 x')
ax.set_title('(c) 滞后回线（相变的直接证据）')
ax.legend(fontsize=9)
print("D=0 时：下降支 x = %.3f，上升支 x = %.3f  -> 两者不同即有滞后" %
      (np.interp(0, Ds_down[::-1], xd[::-1]), np.interp(0, Ds_up, xu)))
print("μ=0.5 折点： x=±%.4f, |D|=±%.4f" % (1/np.sqrt(3*0.5), fold_D(0.5)))
print("μ=0.25 双稳带宽 |D|<%.4f ; μ=1.0 时 |D|<%.4f （乘侮越强，带越窄）" % (fold_D(0.25), fold_D(1.0)))

plt.tight_layout()
plt.savefig(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'figures', 'fig_fold.png'), dpi=160, bbox_inches='tight')
print("saved: figures/fig_fold.png")
