# -*- coding: utf-8 -*-
import os as _os
"""
尝试把「相生 + 相克」同时编码进 Cartan 框架
古立翠 A_4^(1) 只编码了相生环；本脚本探索加入相克后的结果。
"""
import numpy as np, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
plt.rcParams['font.sans-serif'] = ['Noto Sans SC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
from numpy.linalg import det, matrix_rank, eigvalsh

n = 5
phi = (1 + math.sqrt(5)) / 2

# 相生环 C5 的邻接矩阵（相邻相连）
S = np.zeros((n, n))
for i in range(n):
    S[i, (i + 1) % n] = 1; S[(i + 1) % n, i] = 1
# 相克：相距 2 的对角，即 C5 的补图
K = np.zeros((n, n))
for i in range(n):
    K[i, (i + 2) % n] = 1; K[(i + 2) % n, i] = 1

print("=" * 64)
print("一、相生环 vs 相克环：C5 是自补图")
print("  相生边数 =", int(S.sum() // 2), "  相克边数 =", int(K.sum() // 2))
print("  相生 + 相克 = 完全图 K5 ? ", bool(np.allclose(S + K, np.ones((n, n)) - np.eye(n))))
print("  相生环谱 =", np.round(np.sort(eigvalsh(S)), 6))
print("  相克环谱 =", np.round(np.sort(eigvalsh(K)), 6))
print("  两者同谱（结构同构）：", bool(np.allclose(np.sort(eigvalsh(S)), np.sort(eigvalsh(K)))))

# 加权 Cartan 族 A(a,b) = 2I - a*Adj(C5) - b*Adj(C5补)
def Aab(a, b):
    return 2 * np.eye(n) - a * S - b * K

def classify(M):
    ev = np.sort(eigvalsh(M)); tol = 1e-9
    if np.any(ev < -tol): return "不定型 (indefinite)", ev
    if np.any(np.abs(ev) < tol): return "仿射型 (affine)", ev
    return "有限型 (finite, 正定)", ev

reps = {
    "纯相生 A(1,0)":  Aab(1, 0),
    "纯相克 A(0,1)":  Aab(0, 1),
    "生克等权 A(.5,.5)": Aab(0.5, 0.5),
    "生克全耦合 A(1,1)=K5": Aab(1, 1),
}
print("\n" + "=" * 64)
print("二、四种编码的判别")
for name, M in reps.items():
    t, ev = classify(M)
    print(f"  {name:20s} det={det(M):9.4f}  rank={matrix_rank(M)}")
    print(f"       谱 = {np.round(ev, 6)}   -> {t}")

print("\n" + "=" * 64)
print("三、加权族的解析特征值（同一 DFT 模态 k 下）")
print("   mu0 = 2 - 2(a+b)                      [k=0 模态]")
print("   mu1 = mu4 = 2 - (1/phi)a + phi*b       [k=1,4]")
print("   mu2 = mu3 = 2 + phi*a - (1/phi)b       [k=2,3]   (phi=%.6f)" % phi)
# 数值验证解析式
for (a, b) in [(1, 0), (0, 1), (0.5, 0.5), (1, 1)]:
    ev = np.sort(eigvalsh(Aab(a, b)))
    mu = np.sort([2 - 2*(a+b), 2-(1/phi)*a+phi*b, 2+phi*a-(1/phi)*b,
                  2+phi*a-(1/phi)*b, 2-(1/phi)*a+phi*b])
    print(f"   a={a}, b={b}: 数值={np.round(ev,6)}  解析={np.round(mu,6)}  一致={bool(np.allclose(ev,mu))}")

print("\n" + "=" * 64)
print("四、相图分区（由 mu0 主导）")
print("   a + b < 1  -> 有限型（正定） —— 刚性")
print("   a + b = 1  -> 仿射型（半正定, 1 零） —— 动态平衡/临界")
print("   a + b > 1  -> 不定型（含负特征值） —— 失稳")
print("   注：等权生克 a=b=0.5 恰在 a+b=1 临界线上 -> 同时含生与克且为仿射型！")

# ---------- 图 ----------
a_line = np.linspace(0, 1.6, 400)
A_, B_ = np.meshgrid(a_line, a_line)
mu0 = 2 - 2 * (A_ + B_)
indef = mu0 < -1e-6
aff = (~indef) & (np.abs(mu0) < 2e-3)
fin = (~indef) & (~aff)
img = np.where(indef, 2, np.where(aff, 1, 0)).astype(float)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.4))
ax = axes[0]
cmap = ListedColormap(['#aed6f1', '#27ae60', '#e74c3c'])
ax.imshow(img, origin='lower', extent=[0, 1.6, 0, 1.6], cmap=cmap, aspect='auto', alpha=0.9)
ax.plot(a_line, 1 - a_line, 'k--', lw=1.6, label='a + b = 1（仿射临界线）')
for name, (x, y) in {'A(1,0) 纯生': (1, 0), 'A(0,1) 纯克': (0, 1),
                     'A(.5,.5) 等权': (0.5, 0.5), 'A(1,1) K5': (1, 1)}.items():
    ax.plot(x, y, 'ko', ms=6)
    ax.annotate(name, (x, y), textcoords='offset points', xytext=(7, 7), fontsize=9)
ax.set_xlabel('相生耦合强度 a'); ax.set_ylabel('相克耦合强度 b')
ax.set_title('五行 Cartan 耦合相图\n蓝=有限型(刚性)  绿=仿射型(动态平衡)  红=不定型(失稳)')
ax.legend(loc='lower right'); ax.set_xlim(0, 1.6); ax.set_ylim(0, 1.6)

ax = axes[1]
labels = list(reps.keys())
for i, (name, M) in enumerate(reps.items()):
    ev = np.sort(eigvalsh(M))
    ax.plot(ev, [i] * len(ev), 'o', ms=9)
    for v in ev:
        ax.text(v, i + 0.10, '%.2f' % v, ha='center', fontsize=8)
ax.axvline(0, color='k', lw=0.8)
ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels, fontsize=9.5)
ax.set_xlabel('特征值 λ'); ax.set_title('四种编码的特征值对比')
ax.set_ylim(-0.5, len(labels) - 0.3)

plt.tight_layout()
plt.savefig(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'figures', 'fig_phase.png'), dpi=160, bbox_inches='tight')
print("\nsaved: figures/fig_phase.png")
