# wuxing-math · 五行数学之旅

**A mathematical journey of the Chinese Five Elements (Wu Xing): from the 5-cycle / affine Cartan matrix A₄⁽¹⁾ to fold phase transitions.**

把中医「五行」从"五种物质的清单"重新讲成"一张五节点环的关系网"，并一路推到"相变"。

---

## 核心结论链

> **结构**（$`C_5`$、$`R^5=I`$）→ **动力**（$`e^{At}`$）→ **稳定**（有界稳定域）
> → **代数**（仿射 Cartan $`A_4^{(1)}`$）→ **生克兼编码**（$`a+b=1`$）
> → **乘侮微扰**（平移/弯折/手性）→ **相变**（fold / 双稳 / 滞后）
> → **系统科学**（正负反馈 · 自稳网络）

- 相生矩阵 $`R`$ 是循环置换矩阵，$`R^5=I`$。

  $`\{I,R,R^2,R^3,R^4\}`$ 构成 5 阶循环群，且都是正交矩阵；生、克、侮、母子四种关系**全是 $`R`$ 的幂**。
- 五行图 = 仿射 Dynkin 图 $`\tilde A_4`$，Cartan 矩阵 $`A=2I-\mathrm{Adj}(C_5)`$：$`\det(A)=0`$、秩 4、半正定（**仿射型**）。

  零根 $`=(1,1,1,1,1)`$；非零特征根 $`=2+\varphi`$ 与 $`2-\tfrac1\varphi`$（黄金比 $`\varphi`$ 自动出现）。
- 生克加权 $`M(a,b)=2I-a\,\mathrm{Adj}(生)-b\,\mathrm{Adj}(克)`$：$`a+b<1`$ 有限型 / $`=1`$ **仿射型（动态平衡）** / $`>1`$ 不定型。

  **"生克总强度 = 1" ＝ "以平为期"。**
- 非线性化乘侮（$`dx/dt=D+x-\mu x^3`$）→ **S 形折叠、双稳带与滞后**——**五行的病，是一场 fold 相变。**

## 图（figures/）

| 图 | 内容 |
|---|---|
| `fig_cartan.png` | $A_4^{(1)}$ 核算：五节点环 $C_5$ 与特征值谱 |
| `fig_phase.png` | 生克耦合相图：有限型 / 仿射型 / 不定型 |
| `fig_pert.png` | 乘侮微扰：临界线的平移与弯折、手性复模态 |
| `fig_fold.png` | 非线性乘侮：S 形分支 + 相变带 + 滞后回线 |

## 目录

```
wuxing-math/
├── docs/        structure_note.md        研究笔记（主文档）
├── src/         cartan_calc.py            Cartan 矩阵核算
│                cartan_plot.py            五节点环 + 特征值谱
│                shengke_phase.py          生克兼编码相图
│                chengwu_perturb.py        乘侮微扰
│                fold_transition.py        非线性相变（fold）
├── figures/     fig_cartan / fig_phase / fig_pert / fig_fold
└── references/  README.md（仅引用信息，不含 PDF）
```

## 复现

```bash
pip install -r requirements.txt
python src/cartan_calc.py       # 打印核算结果
python src/cartan_plot.py       # 生成 figures/fig_cartan.png
python src/shengke_phase.py     # 生成 figures/fig_phase.png
python src/chengwu_perturb.py   # 生成 figures/fig_pert.png
python src/fold_transition.py   # 生成 figures/fig_fold.png
```

> 脚本输出目录为其所在目录的 `../figures/`，故从仓库任意位置运行均可。

## 引用

见 [`references/README.md`](references/README.md)。本项目为**独立的探索性重构**，非任何原文的官方发布；如引用，请同时引用对应文献。

## License

- 代码：**MIT**（见 `LICENSE`）
- 文档与图：**CC-BY-4.0**（署名传播）
