import matplotlib.pyplot as plt
import warnings
from mpmath import nsum, exp, inf
warnings.filterwarnings('ignore')
# from IVParamOptim import *
from tqdm import tqdm, trange
from decimal import Decimal
from plot3d import *
import numpy as np
import math

prob = 0.5
poi_lamda = 0.1
k_w1 = 2
lamda_w1 =1
k_w2 = 2
lamda_w2 = 1
nn = 12
N = 2 ** nn
eta =  0.01
alpha =  0.5
for j in range(N):
    nuj = j * eta
    tmp1 = alpha + 1j * nuj

    # reset
    local_total1 = 0
    local_total2 = 0
    local_k_m_w = 0
    d1, e1, f1, g1, d2, e2, f2, g2 = 0, 0, 0, 0, 0, 0, 0, 0
    u = nuj - (alpha + 1) * 1j
    for n in trange(0, 100):
        # print(j, n)
        # total += exp(-n ** 2)
        d1 = Decimal(np.math.gamma(1 + n / k_w1))
        e1 = Decimal(lamda_w1 ** n)
        g1 = (1j * u) ** n
        f1 = Decimal(np.math.factorial(n))

        # print(d1)
        # print(e1)
        # print(g1)
        # print(f1)
        # print(float(d1))
        # print(float(e1))
        # print(g1)
        # print(float(f1))
        local_total1 += (float(d1) * float(e1) * g1) / float(f1)
        # print(local_total1)


        d2 = Decimal(((-1) ** n) * math.gamma(1 + n / k_w2))
        e2 = Decimal(lamda_w2 ** n)
        g2 = (-1j * u) ** n
        f2 = Decimal(np.math.factorial(n))
        local_total2 += (float(d2) * float(e2) * g2) / float(f2)
        # print(local_total2)
        n += 1
    local_k_m_w = prob * local_total1 + (1 - prob) * local_total2 - 1
    print(local_k_m_w, j)



