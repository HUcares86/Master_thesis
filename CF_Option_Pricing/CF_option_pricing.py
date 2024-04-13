import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import warnings
from mpmath import nsum, exp, inf
warnings.filterwarnings('ignore')
# from IVParamOptim import *
from tqdm import tqdm, trange
from decimal import Decimal
from plot3d import *


class CfOptionPricing():
    def __init__(self, S0, K, r, q, T, sigma, model, option_type, num, n, eta, alpha, K_array, S_array, params):
        self.S0 = S0
        self.r = r
        self.q = q
        self.T = T
        self.K = K
        self.s = np.log(self.S0)
        self.k = np.log(self.K)
        self.sigma = sigma
        self.model = model
        self.option_type = option_type
        self.num = num

        # parameters for fft
        self.n = n
        self.N = 2 ** self.n

        # step - size
        self.eta = eta
        # damping factor
        self.alpha = alpha

        # step -sixe in log strike space
        self.lamda = (2 * math.pi / self.N) / self.eta

        # choice. of beta
        # beta = np.log(S0) - N*lamda/2
        self.beta = np.log(K)

        # evaluate many strikes
        self.K_array = K_array
        self.S_array = S_array
        self.params = params
        self.call_array = []
        self.call_matrix = pd.DataFrame()

        if model == 'GBM':
            pass
        elif model == 'VG':
            sig = 0.3
            nu = 0.5
            theta = -0.4
            self.params.append(sig)
            self.params.append(nu)
            self.params.append(theta)

        elif model == 'Heston':
            kappa = 2.0
            theta = -0.4
            sig = 0.3
            rho = 0.5
            v0 = 0.04

            self.params.append(kappa)
            self.params.append(theta)
            self.params.append(sig)
            self.params.append(rho)
            self.params.append(v0)

        elif model == 'Merton_Normal':
            if num == -2:
                poi_lamda = params[0]
                mu_normal = params[1]
                sig_normal = params[2]
                k_m_n = math.exp(mu_normal + 0.5*sig_normal**2) - 1

                self.params.append(k_m_n)

            if num == 1:
                poi_lamda = 0.5
                mu_normal = 0.8
                sig_normal = 0.2
                k_m_n = np.exp(mu_normal + 0.5*sig_normal**2) - 1

                self.params.append(poi_lamda)
                self.params.append(mu_normal)
                self.params.append(sig_normal)
                self.params.append(k_m_n)


        elif model == "Merton_Double_Normal":
            # mu_normal_1 > 0 , mu_normal_2 < 0
            if num == 1:
                prob = 0.9
                poi_lamda = 0.5
                mu_normal_1 = 2
                sig_normal_1 = 0.1
                mu_normal_2 = -2
                sig_normal_2 = 0.2
                k_m_n = prob*(np.exp(mu_normal_1 + 0.5*sig_normal_1**2)) + (1-prob)*(np.exp(mu_normal_2 + 0.5*sig_normal_2**2)) - 1
                self.params.append(prob)
                self.params.append(poi_lamda)
                self.params.append(mu_normal_1)
                self.params.append(sig_normal_1)
                self.params.append(mu_normal_2)
                self.params.append(sig_normal_2)
                self.params.append(k_m_n)

        elif model == 'Merton_Double_exp':
            if num == -2:
                prob = params[0]
                poi_lamda = params[1]
                e_alpha_1 = params[2]
                e_alpha_2 = params[3]
                k_m_exp = prob * (e_alpha_1 / (e_alpha_1 - 1)) + (1 - prob) * (e_alpha_2 / (e_alpha_2 + 1)) - 1
                self.params.append(k_m_exp)
            if num == -1:
                prob = 0.5
                poi_lamda = 3
                e_alpha_1 = 30
                e_alpha_2 = 30
                k_m_exp = prob*(e_alpha_1 / (e_alpha_1 - 1)) + (1 - prob)*(e_alpha_2 / (e_alpha_2 + 1)) - 1

                self.params.append(prob)
                self.params.append(poi_lamda)
                self.params.append(e_alpha_1)
                self.params.append(e_alpha_2)
                self.params.append(k_m_exp)
            if num == 0:
                prob = 0.5
                poi_lamda = 1
                e_alpha_1 = 2
                e_alpha_2 = 2
                k_m_exp = prob*(e_alpha_1 / (e_alpha_1 - 1)) + (1 - prob)*(e_alpha_2 / (e_alpha_2 + 1)) - 1

                self.params.append(prob)
                self.params.append(poi_lamda)
                self.params.append(e_alpha_1)
                self.params.append(e_alpha_2)
                self.params.append(k_m_exp)
            # alpha > 1

        elif model == 'Merton_Double_gamma':
            # g_beta_1 & g_beta_2 > 1
            if num == -2:
                prob = params[0]
                poi_lamda = params[1]
                g_beta_1 = params[2]
                g_alpha_1 = params[3]
                g_beta_2 = params[4]
                g_alpha_2 = params[5]
                k_m_g = prob*(1 - 1 / g_beta_1)**(-g_alpha_1) + (1 - prob)*(1 + 1/g_beta_2)**(-g_alpha_2) - 1
                self.params.append(k_m_g)
            # if num == 0:
            #     prob = 0.5
            #     poi_lamda = 1
            #     g_beta_1 = 2
            #     g_alpha_1 = 1
            #     g_beta_2 = 2
            #     g_alpha_2 = 1
            #     k_m_g = prob*(1 - 1 /g_beta_1)**(-g_alpha_1) + (1 - prob)*(1 + 1/g_beta_2)**(-g_alpha_2) - 1
            #
            #     self.params.append(prob)
            #     self.params.append(poi_lamda)
            #     self.params.append(g_beta_1)
            #     self.params.append(g_alpha_1)
            #     self.params.append(g_beta_2)
            #     self.params.append(g_alpha_2)
            #     self.params.append(k_m_g)
            # # num 1 - 5 change in alpha
            # if num == 1:
            #     prob = 0.5
            #     poi_lamda = 1
            #     g_beta_1 = 1.5
            #     g_alpha_1 = 0.0
            #     g_beta_2 = 1.5
            #     g_alpha_2 = 0.0
            #     k_m_g = prob*(1 - 1 /g_beta_1)**(-g_alpha_1) + (1 - prob)*(1 + 1/g_beta_2)**(-g_alpha_2) - 1
            #
            #     self.params.append(prob)
            #     self.params.append(poi_lamda)
            #     self.params.append(g_beta_1)
            #     self.params.append(g_alpha_1)
            #     self.params.append(g_beta_2)
            #     self.params.append(g_alpha_2)
            #     self.params.append(k_m_g)

        elif model == 'weibull':
            # k_w1  >= 1, k_w2  >= 1
            if num == -2:
                prob = params[0]
                poi_lamda = params[1]
                k_w1 = params[2]
                lamda_w1 = params[3]
                k_w2 = params[4]
                lamda_w2 = params[5]
                total1 = 0
                total2 = 0
                for n in trange(0, 200):
                    # total += exp(-n ** 2)
                    a1 = Decimal(np.math.gamma(1 + n / k_w1))
                    # a = Decimal(np.math.factorial(n / k_w1))
                    b1 = Decimal(lamda_w1 ** n)
                    c1 = Decimal(np.math.factorial(n))
                    total1 += (a1 * b1) / c1

                    a2 = Decimal(((-1) ** n) * math.gamma(1 + n / k_w2))
                    # a = Decimal(np.math.factorial(n / k_w1))
                    b2 = Decimal(lamda_w2 ** n)
                    c2 = Decimal(np.math.factorial(n))
                    total2 += (a2 * b2) / c2

                    n += 1
                k_m_w = prob*total1 + (1 - prob)*total2  - 1
                self.params.append(k_m_w)

    def generic_cf(self, u, s):
        if self.model == "GBM":
            sig = self.sigma

            ln_phi = 1j * (np.log(s) + (self.r - self.q - sig ** 2 / 2) * self.T) * u - \
                     ((sig * np.sqrt(self.T) * u) ** 2) / 2
            cf = np.exp(ln_phi)
            return cf

        if self.model == "Heston":
            kappa = self.params[0]
            theta = self.params[1]
            sig = self.params[2]
            rho = self.params[3]
            v0 = self.params[4]

            temp1 = kappa - 1j * rho * sig * u
            gamma = np.sqrt((sig ** 2) * (u ** 2 + 1j * u) + temp1 ** 2)

            pow1 = 2 * kappa * theta / (sig ** 2)

            # number 1
            ele1 = (kappa * theta * self.T * temp1) / (sig ** 2)
            ele2 = 1j * u * self.r * self.T
            ele3 = 1j * u * np.log(s)
            numer1 = ele1 + ele2 + ele3

            # log_denum1
            dele1 = np.cosh(gamma * self.T / 2)
            dele2 = (temp1 / gamma) * np.sinh(gamma * self.T / 2)
            dele3 = (u ** 2 + 1j * u) * v0
            dele3 = gamma / np.tanh(gamma * self.T / 2)
            dele4 = temp1

            log_denum1 = pow1 * np.log(dele1) + dele2
            temp2 = dele3 / (dele3 + dele4)
            log_phi = numer1 - log_denum1 - temp2
            cf = np.exp(log_phi)
            return cf

        if self.model == "Merton_Normal":
            sig = self.sigma
            poi_lamda = self.params[0]
            mu_normal = self.params[1]
            sig_normal = self.params[2]
            k_m_n = self.params[3]

            ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_n - sig ** 2 / 2) * self.T) * u - \
                     ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                     poi_lamda * self.T * (np.exp(1j * u * mu_normal - ((sig_normal * u) ** 2) / 2) - 1)
            cf = np.exp(ln_phi)

            return cf

        if self.model == "Merton_Double_Normal":
            sig = self.sigma
            prob = self.params[0]
            poi_lamda = self.params[1]
            mu_normal_1 = self.params[2]
            sig_normal_1 = self.params[3]
            mu_normal_2 = self.params[4]
            sig_normal_2 = self.params[5]
            k_m_n = self.params[6]


            ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_n - sig ** 2 / 2) * self.T) * u - \
                     ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                     poi_lamda * self.T * (prob * np.exp(1j * u * mu_normal_1 - ((sig_normal_1 * u) ** 2) / 2) + (1-prob)*np.exp(1j * u * mu_normal_2 - ((sig_normal_2 * u) ** 2) / 2) - 1)
            cf = np.exp(ln_phi)
            return cf

        if self.model == "Merton_Double_exp":
            sig= self.sigma
            prob= self.params[0]
            poi_lamda= self.params[1]
            e_alpha_1= self.params[2]
            e_alpha_2= self.params[3]
            k_m_exp= self.params[4]

            ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_exp- sig ** 2 / 2) * self.T) * u - \
                     ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                     poi_lamda * self.T * (prob * (e_alpha_1/(e_alpha_1-1j*u)) + (1-prob) * (e_alpha_2/(e_alpha_2+1j*u)) - 1)

            # a = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_exp- sig ** 2 / 2) * self.T) * u
            # b = ((sig * np.sqrt(self.T) * u) ** 2) / 2
            # c = poi_lamda * self.T * (prob * (e_alpha_1/(e_alpha_1-1j*u)) + (1-prob) * (e_alpha_2/(e_alpha_2+1j*u)) - 1)
            # d = (e_alpha_1/(e_alpha_1-1j*u))
            # e =  (e_alpha_2/(e_alpha_2+1j*u))
            # print("a,b,c",a, b, c, d ,e)
            cf = np.exp(ln_phi)

            # print(k_m_exp)
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
            # print(k_m_g)

            ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_g- sig ** 2 / 2) * self.T) * u - \
                     ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                     poi_lamda * self.T * (prob * (1 - (1j * u / g_beta_1)) ** (-g_alpha_1) + (1 - prob) * (1 + (1j * u / g_beta_2)) ** (-g_alpha_2) - 1)
            # a = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_g- sig ** 2 / 2) * self.T) * u
            # b = ((sig * np.sqrt(self.T) * u) ** 2) / 2
            # c = poi_lamda * self.T * (prob * (1 - (1j * u / g_beta_1)) ** (-g_alpha_1) + (1 - prob) * (1 + (1j * u / g_beta_2)) ** (-g_alpha_2) - 1)
            # d = (1 - (1j * u / g_beta_1) ** (-g_alpha_1))
            # e =(1 - (1j * u / g_beta_1) ** (-g_alpha_1))
            # print("a,b,c",a, b, c, d, e)
            cf = np.exp(ln_phi)
            # print(cf)
            return cf

        # if self.model == 'weibull':
        #     sig= self.sigma
        #     prob = self.params[0]
        #     poi_lamda = self.params[1]
        #     k_w1 = self.params[2]
        #     lamda_w1 = self.params[3]
        #     k_w2 = self.params[4]
        #     lamda_w2 = self.params[5]
        #     k_m_w = self.params[6]
        #     total1 = 0
        #     total2 = 0
        #
        #     ln_phi = 1j * (np.log(s) + (self.r - self.q - poi_lamda*k_m_w - sig ** 2 / 2) * self.T) * u - \
        #              ((sig * np.sqrt(self.T) * u) ** 2) / 2 + \
        #              poi_lamda * self.T \
        #              * ()
        #     cf = np.exp(ln_phi)
        #
        #
        #     for n in trange(0, 200):
        #         # total += exp(-n ** 2)
        #         a1 = Decimal(np.math.gamma(1 + n / k_w1))
        #         # a = Decimal(np.math.factorial(n / k_w1))
        #         b1 = Decimal(lamda_w1 ** n)
        #         c1 = Decimal(np.math.factorial(n))
        #         total1 += (a1 * b1) / c1
        #
        #         a2 = Decimal(((-1) ** n) * math.gamma(1 + n / k_w2))
        #         # a = Decimal(np.math.factorial(n / k_w1))
        #         b2 = Decimal(lamda_w2 ** n)
        #         c2 = Decimal(np.math.factorial(n))
        #         total2 += (a2 * b2) / c2
        #
        #         n += 1
        #     k_m_w = prob * total1 + (1 - prob) * total2 - 1
        #     self.params.append(k_m_w)
        #
        #
        #     return cf

    def evaluate_integral_one_strike(self):
        df = np.exp(-self.r*self.T)
        beta = np.log(self.K)
        if self.option_type == "call":
            sum1 = 0
            for j in range(self.N):#
                nuj = j * self.eta
                tmp1 = self.alpha + 1j * nuj
                psi_nuJ = df * self.generic_cf(nuj - (self.alpha + 1) * 1j, self.S0) / (tmp1 * (tmp1 + 1))
                # print(psi_nuJ, j)
                if j == 0:
                    wj = self.eta / 2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj) * psi_nuJ * wj

            CT_k = (np.exp(-self.alpha * self.k) / math.pi) * sum1

            return np.real(CT_k)
        if self.option_type == "put":
            sum1 = 0
            for j in range(self.N):
                nuj = j * self.eta
                tmp1 = self.alpha - 1j * nuj
                psi_nuJ = df*self.generic_cf(nuj - (-self.alpha + 1) * 1j, self.S0)/(tmp1 * (tmp1 - 1))
                if j == 0:
                    wj = self.eta/2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj )* psi_nuJ*wj
            CT_k = (np.exp(self.alpha * self.k) / math.pi)*sum1

            return np.real(CT_k)

    def evaluate_integral_many_strikes(self):
        self.call_array = []
        df = np.exp(-self.r*self.T)
        if self.option_type == "call":
            for k in tqdm(self.K_array):
                beta = np.log(k)
                sum1 = 0
                for j in range(self.N):
                    nuj = j * self.eta
                    tmp1 = self.alpha + 1j * nuj
                    psi_nuJ = df*self.generic_cf(nuj - (self.alpha + 1) * 1j, self.S0)/(tmp1 * (tmp1 + 1))
                    if j == 0:
                        wj = self.eta/2
                    else:
                        wj = self.eta
                    sum1 += np.exp(-1j * beta * nuj) * psi_nuJ*wj
                CT_k = (np.exp(-self.alpha * beta) / math.pi)*sum1
                self.call_array.append(np.real(CT_k))

            return self.call_array  #self.K_array,

        if self.option_type == "put":
            for k in tqdm(self.K_array):
                beta = np.log(k)
                sum1 = 0
                for j in range(self.N):
                    nuj = j * self.eta
                    tmp1 = self.alpha - 1j * nuj
                    psi_nuJ = df*self.generic_cf(nuj - (-self.alpha + 1) * 1j, self.S0)/(tmp1 * (tmp1 - 1))
                    if j == 0:
                        wj = self.eta/2
                    else:
                        wj = self.eta
                    sum1 += np.exp(-1j * beta * nuj) * psi_nuJ*wj
                CT_k = (np.exp(self.alpha * beta) / math.pi)*sum1
                self.call_array.append(np.real(CT_k))

            return self.call_array  #self.K_array,

    def evaluate_integral_many_S0(self):
        call_array_2 = []
        df = np.exp(-self.r*self.T)
        beta = np.log(self.K)

        if self.option_type == "call":
            for s in tqdm(self.S_array):
                sum1 = 0
                for j in range(self.N):
                    nuj = j * self.eta
                    tmp1 = self.alpha + 1j * nuj
                    psi_nuJ = df*self.generic_cf(nuj - (self.alpha + 1) * 1j, s)/(tmp1 * (tmp1 + 1))
                    if j == 0:
                        wj = self.eta/2
                    else:
                        wj = self.eta
                    sum1 += np.exp(-1j * beta * nuj) * psi_nuJ*wj
                CT_k = (np.exp(-self.alpha * beta) / math.pi)*sum1
                call_array_2.append(np.real(CT_k))
            return call_array_2

        if self.option_type == "put":
            for s in tqdm(self.S_array):
                sum1 = 0
                for j in range(self.N):
                    nuj = j * self.eta
                    tmp1 = self.alpha - 1j * nuj
                    psi_nuJ = df * self.generic_cf(nuj - (-self.alpha + 1) * 1j, s) / (tmp1 * (tmp1 - 1))
                    if j == 0:
                        wj = self.eta / 2
                    else:
                        wj = self.eta
                    sum1 += np.exp(-1j * beta * nuj) * psi_nuJ * wj
                CT_k = (np.exp(self.alpha * beta) / math.pi) * sum1
                call_array_2.append(np.real(CT_k))

            return call_array_2

    def evaluate_integral_one_S0(self, S1):
        df = np.exp(-self.r*self.T)
        beta = np.log(self.K)
        if self.option_type == "call":
            sum1 = 0
            for j in range(self.N):#self.N
                nuj = j * self.eta
                tmp1 = self.alpha + 1j * nuj
                psi_nuJ = df * self.generic_cf(nuj - (self.alpha + 1) * 1j, S1) / (tmp1 * (tmp1 + 1))
                # print(nuj, tmp1, psi_nuJ, j)
                if j == 0:
                    wj = self.eta / 2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj) * psi_nuJ * wj

            CT_k = (np.exp(-self.alpha * self.k) / math.pi) * sum1

            return np.real(CT_k)
        if self.option_type == "put":
            sum1 = 0
            for j in range(self.N):
                nuj = j * self.eta
                tmp1 = self.alpha - 1j * nuj
                psi_nuJ = df*self.generic_cf(nuj - (-self.alpha + 1) * 1j, S1)/(tmp1 * (tmp1 - 1))
                if j == 0:
                    wj = self.eta/2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj )* psi_nuJ*wj
            CT_k = (np.exp(self.alpha * self.k) / math.pi)*sum1

            return np.real(CT_k)

class CfOptionPricing_weibull():
    def __init__(self, S0, K, r, q, T, sigma, option_type, num, n, eta, alpha, K_array, S_array, params):
        self.S0 = S0
        self.r = r
        self.q = q
        self.T = T
        self.K = K
        self.s = np.log(self.S0)
        self.k = np.log(self.K)
        self.sigma = sigma
        # self.model = model
        self.option_type = option_type
        self.num = num

        # parameters for fft
        self.n = n
        self.N = 2 ** self.n

        # step - size
        self.eta = eta
        # damping factor
        self.alpha = alpha

        # step -sixe in log strike space
        self.lamda = (2 * math.pi / self.N) / self.eta

        # choice. of beta
        # beta = np.log(S0) - N*lamda/2
        self.beta = np.log(K)

        # evaluate many strikes
        self.K_array = K_array
        self.S_array = S_array
        self.params = params
        self.call_array = []
        self.call_matrix = pd.DataFrame()

        self.sig = self.sigma
        self.prob = self.params[0]
        self.poi_lamda = self.params[1]
        self.k_w1 = self.params[2]
        self.lamda_w1 = self.params[3]
        self.k_w2 = self.params[4]
        self.lamda_w2 = self.params[5]
        self.total1 = 0
        self.total2 = 0
        self.k_m_w = 0

    def evaluate_integral_one_strike(self):

        self.total1 = 0
        self.total2 = 0
        self.k_m_w = 0
        a1, b1, c1, a2, b2, c2 = 0, 0, 0, 0, 0, 0
        for n in trange(0, 50):
            # total += exp(-n ** 2)
            a1 = Decimal(np.math.gamma(1 + n / self.k_w1))
            # a = Decimal(np.math.factorial(n / k_w1))
            b1 = Decimal(self.lamda_w1 ** n)
            c1 = Decimal(np.math.factorial(n))
            self.total1 += (float(a1) * float(b1)) / float(c1)
            a2 = Decimal(((-1) ** n) * math.gamma(1 + n / self.k_w2))
            # a = Decimal(np.math.factorial(n / k_w1))
            b2 = Decimal(self.lamda_w2 ** n)
            c2 = Decimal(np.math.factorial(n))
            self.total2 += (a2 * b2) / c2
            n += 1
        self.k_m_w = self.prob * self.total1 + (1 - self.prob) * self.total2 - 1
        print(self.k_m_w)

        df = np.exp(-self.r*self.T)
        beta = np.log(self.K)

        if self.option_type == "call":
            sum1 = 0
            for j in range(self.N):
                nuj = j * self.eta
                tmp1 = self.alpha + 1j * nuj

                # reset
                local_total1 = 0
                local_total2 = 0
                local_k_m_w = 0
                d1, e1, f1, g1, d2, e2, f2, g2 = 0, 0, 0, 0, 0, 0, 0, 0
                u = nuj - (self.alpha + 1) * 1j
                for n in trange(0, 100):
                    # total += exp(-n ** 2)
                    d1 = Decimal(np.math.gamma(1 + n / self.k_w1))
                    e1 = Decimal(self.lamda_w1 ** n)
                    g1 = Decimal((1j * u) ** n)
                    f1 = Decimal(np.math.factorial(n))
                    local_total1 += (d1 * e1 * g1) / f1

                    d2 = Decimal(((-1) ** n) * math.gamma(1 + n / self.k_w2))
                    e2 = Decimal(self.lamda_w2 ** n)
                    g2 = Decimal((-1j * u) ** n)
                    f2 = Decimal(np.math.factorial(n))
                    local_total2 += (d2 * e2 * g2) / f2
                    n += 1
                local_k_m_w = self.prob * local_total1 + (1 - self.prob) * local_total2 - 1


                local_ln_phi = 1j * (np.log(self.S0) + (self.r - self.q - self.poi_lamda * self.k_m_w - self.sig ** 2 / 2) * self.T) * u - \
                         ((self.sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                         self.poi_lamda * self.T * (local_k_m_w)
                local_cf = np.exp(local_ln_phi)

                psi_nuJ = df * local_cf / (tmp1 * (tmp1 + 1))
                if j == 0:
                    wj = self.eta / 2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj) * psi_nuJ * wj

            CT_k = (np.exp(-self.alpha * self.k) / math.pi) * sum1

            return np.real(CT_k)
        if self.option_type == "put":
            sum1 = 0
            for j in range(self.N):
                nuj = j * self.eta
                tmp1 = self.alpha - 1j * nuj
                # reset
                local_total1 = 0
                local_total2 = 0
                local_k_m_w = 0
                d1, e1, f1, g1, d2, e2, f2, g2 = 0, 0, 0, 0, 0, 0, 0, 0
                u = nuj - (self.alpha + 1) * 1j
                for n in trange(0, 200):
                    # total += exp(-n ** 2)
                    d1 = Decimal(np.math.gamma(1 + n / self.k_w1))
                    e1 = Decimal(self.lamda_w1 ** n)
                    g1 = Decimal((1j * u) ** n)
                    f1 = Decimal(np.math.factorial(n))
                    local_total1 += (d1 * e1 * g1) / f1

                    d2 = Decimal(((-1) ** n) * math.gamma(1 + n / self.k_w2))
                    e2 = Decimal(self.lamda_w2 ** n)
                    g2 = Decimal((-1j * u) ** n)
                    f2 = Decimal(np.math.factorial(n))
                    local_total2 += (d2 * e2 * g2) / f2
                    n += 1
                local_k_m_w = self.prob * local_total1 + (1 - self.prob) * local_total2 - 1


                local_ln_phi = 1j * (np.log(self.S0) + (self.r - self.q - self.poi_lamda * self.k_m_w - self.sig ** 2 / 2) * self.T) * u - \
                         ((self.sig * np.sqrt(self.T) * u) ** 2) / 2 + \
                         self.poi_lamda * self.T * (local_k_m_w)
                local_cf = np.exp(local_ln_phi)

                psi_nuJ = df * local_cf / (tmp1 * (tmp1 + 1))
                if j == 0:
                    wj = self.eta/2
                else:
                    wj = self.eta
                sum1 += np.exp(-1j * beta * nuj )* psi_nuJ*wj
            CT_k = (np.exp(self.alpha * self.k) / math.pi)*sum1

            return np.real(CT_k)