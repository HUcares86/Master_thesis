from mpmath import nsum, exp, inf
import math
from tqdm import tqdm, trange
from decimal import Decimal
from scipy.special import gamma, factorial
import numpy as np
eta,alpha =  0.01, 0.5
N = 2* 10**12
S = 100
K = 100
T = 0.25
q = 0.01
r = 0.05  #0.04  0.05  , 0.065
sigma = 0.3

df = np.exp(-r*T)
beta = np.log(K)

sum1 = 0
def generic_cf(self, u, s):
    if self.model == "Merton_Double_exp":
        sig = self.sigma
        prob = self.params[0]
        poi_lamda = self.params[1]
        e_alpha_1 = self.params[2]
        e_alpha_2 = self.params[3]
        k_m_exp = self.params[4]

        ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda * k_m_exp - sig ** 2 / 2) * self.T) * u - \
                 ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                 poi_lamda * self.T * (prob * (e_alpha_1 / (e_alpha_1 - 1j * u)) + (1 - prob) * (
                    e_alpha_2 / (e_alpha_2 + 1j * u)) - 1)
        cf = np.exp(ln_phi)
        # print(cf)
        return cf

    if self.model == "Merton_Double_gamma":
        sig = self.sigma
        prob = self.params[0]
        poi_lamda = self.params[1]
        g_beta_1 = self.params[2]
        g_alpha_1 = self.params[3]
        g_beta_2 = self.params[4]
        g_alpha_2 = self.params[5]
        k_m_g = self.params[6]

        ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda * k_m_g - sig ** 2 / 2) * self.T) * u - \
                 ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                 poi_lamda * self.T * (prob * (1 - (1j * u / g_beta_1) ** (-g_alpha_1)) + (1 - prob) * (
                    1 + (1j * u / g_beta_2) ** (-g_alpha_2)) - 1)
        cf = np.exp(ln_phi)
        # print(cf)
        return cf


for j in range(N):
    nuj = j * eta
    tmp1 = alpha + 1j * nuj
    psi_nuJ = df * generic_cf(nuj - (self.alpha + 1) * 1j, self.S0) / (tmp1 * (tmp1 + 1))
    if j == 0:
        wj = self.eta / 2
    else:
        wj = self.eta
    sum1 += np.exp(-1j * beta * nuj) * psi_nuJ * wj

CT_k = (np.exp(-self.alpha * self.k) / math.pi) * sum1

return np.real(CT_k)

