#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""负结果 + 正对照：C5 非线性模型不含对数周期（必须显式装入离散标度）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["Noto Sans SC"]; plt.rcParams["axes.unicode_minus"]=False

phi=(1+5**0.5)/2; q=1/phi**2; per=abs(np.log(q)); f_t=1/per
S=np.zeros((5,5))
for i in range(5): S[i,(i-1)%5]=1
def sim(d,a,c,T=4000,seed=7):
    rng=np.random.default_rng(seed); x=0.3*rng.standard_normal(5)
    tr=[]
    for _ in range(T):
        x=(1-d)*x+a*(S@x)-c*x**3; tr.append(x.copy())
    return np.array(tr)
def spec(res,lt):
    lt=lt-lt.mean(); fs=np.linspace(0.05,6,1500)
    P=np.array([abs((res*np.exp(-2j*np.pi*f*lt)).sum())**2 for f in fs]); return fs,P/P.max()

d,c=0.30,0.6
tr=sim(d,0.2999,c); A=np.abs(tr).max(axis=1)
t=np.arange(1,len(A)+1); m=(A>1e-13)&(t<=1200); t=t[m];A=A[m]; lt=np.log(t)
b=np.polyfit(lt,np.log(A),1); res=np.log(A)-np.polyval(b,lt)
fs,P=spec(res,lt)

# 对照
tc=np.exp(np.linspace(0,6*per,1500)); Ac=tc**-1*(1+0.15*np.cos(2*np.pi*np.log(tc)/per))
ltc=np.log(tc); bc=np.polyfit(ltc,np.log(Ac),1); resc=np.log(Ac)-np.polyval(bc,ltc)
fsc,Pc=spec(resc,ltc)

fig,ax=plt.subplots(1,2,figsize=(13.4,5.6),dpi=155)
ax[0].plot(fs,P,color="#2c5f8a",lw=1.8,label="C5 非线性模型")
ax[0].axvline(f_t,color="#c0392b",ls="--",lw=2,label=f"目标频率 1/|ln q|={f_t:.3f}")
ax[0].set_xlabel("频率（1/ln t）",fontsize=11); ax[0].set_ylabel("归一化谱强度",fontsize=11)
ax[0].set_title("C5 非线性模型：目标频率处【无峰】\n（最强峰在别处）",fontsize=12.5,weight="bold",pad=12)
ax[0].legend(fontsize=10); ax[0].grid(alpha=.25)
k=np.argmin(abs(fs-f_t))
ax[0].annotate(f"此处仅 {P[k]:.2f}",xy=(f_t,P[k]),xytext=(f_t+0.9,0.45),
               arrowprops=dict(arrowstyle="->",color="#c0392b"),color="#c0392b",fontsize=10.5)

ax[1].plot(fsc,Pc,color="#27865a",lw=1.8,label="注入的对数周期信号")
ax[1].axvline(f_t,color="#c0392b",ls="--",lw=2,label="同一目标频率")
ax[1].set_xlabel("频率（1/ln t）",fontsize=11); ax[1].set_ylabel("归一化谱强度",fontsize=11)
ax[1].set_title("正对照：注入后【出现尖峰】\n（证明检测器有效）",fontsize=12.5,weight="bold",pad=12)
ax[1].legend(fontsize=10); ax[1].grid(alpha=.25)
kc=np.argmin(abs(fsc-f_t))
ax[1].annotate(f"峰强度 {Pc[kc]:.2f}",xy=(f_t,Pc[kc]),xytext=(f_t+1.0,0.6),
               arrowprops=dict(arrowstyle="->",color="#27865a"),color="#27865a",fontsize=10.5)

plt.tight_layout()
import os
os.makedirs("/sandbox/workspace/output",exist_ok=True)
fig.savefig("/sandbox/workspace/output/logperiodic_negative_test.png",bbox_inches="tight",facecolor="white",pad_inches=0.2)
print("已生成 output/logperiodic_negative_test.png")
