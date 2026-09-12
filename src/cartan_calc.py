# -*- coding: utf-8 -*-
"""
验证「五行 ↔ 仿射型广义 Cartan 矩阵 A_4^(1)」的各项性质
文献：古立翠《中医五行学说的数学模型与仿射型广义Cartan矩阵》(黑龙江医药, 2010)
"""
import numpy as np
import math
from numpy.linalg import det, matrix_rank, eigvalsh, eig

np.set_printoptions(precision=6, suppress=True)

# ============ 0. 文献给出的矩阵 ============
A = np.array([
    [ 2, -1,  0,  0, -1],
    [-1,  2, -1,  0,  0],
    [ 0, -1,  2, -1,  0],
    [ 0,  0, -1,  2, -1],
    [-1,  0,  0, -1,  2],
], dtype=float)

print("=" * 60)
print("0. 输入矩阵 A（五行 Cartan 矩阵）")
print(A)
print("   节点顺序：木(x1) 火(x2) 土(x3) 金(x4) 水(x5)")

# ============ 1. 对称性 / 可对称化 ============
print("\n" + "=" * 60)
print("1. 对称性 & 可对称化")
print("   A 是否对称：", bool(np.allclose(A, A.T)), " -> 对称矩阵天然可对称化")

# ============ 2. 行列式 ============
print("\n" + "=" * 60)
print("2. 行列式")
print("   det(A) =", round(float(det(A)), 8))

# ============ 3. 秩 ============
n = A.shape[0]
r = matrix_rank(A)
print("\n" + "=" * 60)
print("3. 秩")
print("   rank(A) =", r, " ; n =", n, " ; 零度(n-rank) =", n - r)

# ============ 4. 特征值 ============
ev = np.sort(eigvalsh(A))
print("\n" + "=" * 60)
print("4. 特征值（对称阵，eigvalsh）")
print("   特征值 =", ev)
print("   全部 >= 0（半正定）：", bool(np.all(ev > -1e-9)))
print("   正特征值个数 =", int(np.sum(ev > 1e-9)), " ; 零特征值个数 =", int(np.sum(np.abs(ev) < 1e-9)))

# ============ 5. 零特征向量 & 零根方向 ============
w, V = eig(A)
idx = int(np.argmin(np.abs(w)))
null = V[:, idx].real
null = null / np.linalg.norm(null)
print("\n" + "=" * 60)
print("5. 零特征向量（零根 / null root 方向）")
print("   零特征向量 ≈", null)
print("   归一化后 ≈ (1,1,1,1,1)/sqrt(5) =", np.ones(5)/math.sqrt(5))
print("   验证 A·ones =", A @ np.ones(5))

# ============ 6. 结构分解：A = 2I - Adj(C5) ============
Adj = np.zeros((5, 5))
for i in range(5):
    Adj[i, (i + 1) % 5] = 1
    Adj[(i + 1) % 5, i] = 1
print("\n" + "=" * 60)
print("6. 结构分解：A = 2I - Adj(C5)  （C5 = 五节点环/五边形）")
print("   2I - Adj(C5) 是否等于 A：", bool(np.allclose(2 * np.eye(5) - Adj, A)))
evAdj = np.sort(eigvalsh(Adj))
print("   Adj(C5) 特征值 =", evAdj, " (= 2cos(2πk/5))")
print("   故 A 特征值 = 2 - Adj特征值 =", np.sort(2 - evAdj))

# ============ 7. 与黄金比的关系 ============
phi = (1 + math.sqrt(5)) / 2
print("\n" + "=" * 60)
print("7. 与黄金比 phi 的关系（五边形几何的印记）")
print("   phi = %.6f" % phi)
print("   2cos(72°) = 1/phi = %.6f  -> A 的较小非零特征根 2 - 1/phi = %.6f (二重)" % (1/phi, 2 - 1/phi))
print("   2cos(144°) = -phi = %.6f -> A 的较大非零特征根 2 + phi = %.6f (二重)" % (-phi, 2 + phi))

# ============ 8. 对照：有限型 A_4（链状，非环） ============
A4 = np.array([
    [ 2, -1,  0,  0],
    [-1,  2, -1,  0],
    [ 0, -1,  2, -1],
    [ 0,  0, -1,  2],
], dtype=float)
print("\n" + "=" * 60)
print("8. 对照：有限型 A_4（4 节点链，正定）")
print("   det(A_4) =", round(float(det(A4)), 6))
print("   A_4 特征值 =", np.sort(eigvalsh(A4)), " 全部 > 0：", bool(np.all(eigvalsh(A4) > 0)))

# ============ 9. 结论汇总 ============
print("\n" + "=" * 60)
print("9. 结论汇总")
print("   - 对称、半正定（特征值 0 与 4 个正值）")
print("   - det = 0，秩 = n-1 = 4  -> 典型的『仿射型』特征")
print("   - 唯一零特征向量 ~ (1,1,1,1,1)  -> 零根/null root 方向")
print("   - A = 2I - Adj(C5)，底层图就是『五节点环』，与文献一致")
print("   - 与有限型 A_4（det=5，正定）形成鲜明对照")
