# -*- coding: utf-8 -*-
import os as _os
"""
把「乘 / 侮」作为非对称微扰加入五行 Cartan 模型，观察临界线 a+b=1 的变化
乘 = 克得太过（沿克方向的增强）
侮 = 反克（克的反方向）
"""
import numpy as np, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans SC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
from numpy.linalg import eigvalsh, eig

n = 5
def directed(step):
    D = np.zeros((n, n))
    for i in range(n):
        D[i, (i + step) % n] = 1
    return D

P = directed(1)          # 相生：i -> i+1
C = directed(2)          # 相克：i -> i+2
AdjS = P + P.T           # 相生（无向）
AdjK = C + C.T           # 相克（无向）

def Msym(a, b):
    return 2 * np.eye(n) - a * AdjS - b * AdjK

# ============ 实验 A：全局（均匀）乘/侮 ============
# 乘(前向 +mu)、侮(反向 +nu) 与克同边 -> 等效克强度 b_eff = b + (mu+nu)/2，另加反对称手性 chi=(mu-nu)/2
print("=" * 64)
print("实验 A：全局乘/侮 ≡ 等效克强度平移 + 手性")
print("  对称部分：2I - a*Adj(生) - (b+(mu+nu)/2)*Adj(克)  -> 临界线 a+b+(mu+nu)/2 = 1（整体平移）")
print("  反对称部分：(mu-nu)/2 * (C - C^T)  -> 手性（不改对称部分，故不移动稳定边界）")

# 验证：不同 (mu+nu) 的临界 b 截距（a=0 时）
for g in [0.0, 0.2, 0.4]:
    print(f"   mu+nu={g:.1f} -> 临界线 a+b={1-g:.1f}（b 截距 {1-g:.1f}）")

# ============ 实验 B：局部乘（仅在一条克边 木→土 上） ============
E = np.zeros((n, n)); E[0, 2] = 1; E[2, 0] = 1   # 木-土 那条克边
print("\n" + "=" * 64)
print("实验 B：局部乘（仅加在『木克土』一条边上）")

a = np.linspace(0, 1.5, 260)
b = np.linspace(0, 1.5, 260)
A, B = np.meshgrid(a, b)

def lmin_grid(mu):
    L = np.empty_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            L[i, j] = eigvalsh(2*np.eye(n) - A[i, j]*AdjS - B[i, j]*AdjK - mu*E)[0]
    return L

def b0_at_a0(mu):
    """在 a=0 上求 λmin=0 的临界 b（先粗扫定区间，再二分精算）"""
    bs = np.linspace(0, 1.2, 2401)
    v = np.array([eigvalsh(2*np.eye(n) - 0.0*AdjS - bb*AdjK - mu*E)[0] for bb in bs])
    idx = np.where(np.diff(np.sign(v)))[0]
    if not len(idx):
        return float('nan')
    lo, hi = bs[idx[0]], bs[idx[0] + 1]
    for _ in range(100):
        mid = (lo + hi) / 2
        f_lo = eigvalsh(2*np.eye(n) - 0.0*AdjS - lo*AdjK - mu*E)[0]
        f_mid = eigvalsh(2*np.eye(n) - 0.0*AdjS - mid*AdjK - mu*E)[0]
        if f_lo * f_mid <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

for mu in [0.0, 0.5, 1.0]:
    L = lmin_grid(mu)
    b0 = b0_at_a0(mu)
    print(f"   mu={mu:.1f}: a=0 处临界 b = {b0:.4f} (基线=1.000)")

# ============ 图 ============
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# 面板 1：临界线 —— 平移 vs 弯折
ax = axes[0]
ax.plot(a, 1 - a, 'g--', lw=1.8, label='基线 a+b=1（纯生+克，仿射）')
ax.plot(a, 0.6 - a, 'b--', lw=1.8, label='全局乘侮(mu+nu=0.8)：整体平移')
ax.plot(a, 0.6 - a, 'b--', lw=1.8)
# 局部乘曲线
L = lmin_grid(0.8)
cs = ax.contour(A, B, L, levels=[0], colors='#e74c3c', linewidths=2.2)
ax.clabel(cs, fmt='局部乘 mu=0.8', fontsize=9)
ax.set_xlabel('相生强度 a'); ax.set_ylabel('相克强度 b')
ax.set_title('临界线：全局乘侮「平移」 vs 局部乘「弯折」')
ax.legend(loc='upper right', fontsize=9)
ax.set_xlim(0, 1.5); ax.set_ylim(0, 1.5)

# 面板 2：手性 —— 零模分裂为旋转复模态
ax = axes[1]
M0 = Msym(0.5, 0.5)
Skew = C - C.T
for chi in [0.0, 0.3, 0.6, 1.0]:
    M = M0 + chi * Skew
    ev = eig(M)[0]
    ev = ev[np.argsort(np.abs(ev))]  # 按 |λ| 排序
    ax.plot(ev.real, ev.imag, 'o', ms=7, label=f'手性 χ={chi:.1f}')
ax.axhline(0, color='k', lw=0.6); ax.axvline(0, color='k', lw=0.6)
ax.set_xlabel('Re λ'); ax.set_ylabel('Im λ')
ax.set_title('乘侮的手性效应：临界点上零模 → 旋转复模态')
ax.legend(fontsize=9); ax.set_aspect('equal', 'box')

plt.tight_layout()
plt.savefig(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'figures', 'fig_pert.png'), dpi=160, bbox_inches='tight')
print("\nsaved: figures/fig_pert.png")
