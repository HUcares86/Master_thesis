# %%
import numpy as np
import math
import matplotlib.pyplot as plt
from ImpliedVolatility import *
from implyVolBrent import *
# from numpy import coth
import warnings

warnings.filterwarnings('ignore')
from IVParamOptim import *
from tqdm import tqdm

from plot3D import *


# %%


class CfOptionPricing:

    def __init__(self, config):  # sig在SV系列表Variance的sig，其他時候表真實sig
        self.S0 = config.S0
        self.r = config.r
        self.q = config.q
        self.T = config.T
        self.K = config.K
        self.model = config.model
        self.config = config

        if self.model == "GBM":
            # 真sig
            self.sig = config.sig

        if self.model == "Heston":
            self.kappa = config.kappa
            self.theta = config.theta
            # 變異數的sig
            self.sig = config.sig
            self.rho = config.rho
            self.v0 = config.v0

        if self.model == "VG":
            self.sig = config.sig
            self.nu = config.nu
            self.theta = config.theta

        # 令t==0，T = τ
        if self.model == "SV2":
            self.kappa = config.kappa
            self.theta = config.theta
            self.sig = config.sig
            self.rho = config.rho
            self.v0 = config.v0

        if self.model == "SVJ_Series":
            self.kappa = config.kappa
            self.theta = config.theta
            self.sig = config.sig
            self.rho = config.rho
            self.v0 = config.v0
            self.lda_y = config.lda_y
            self.lda_v = config.lda_v
            self.lda_c = config.lda_c
            self.lda_bar = config.lda_y + config.lda_v + config.lda_c
            self.mu_y = config.mu_y
            self.var_y = config.var_y
            self.mu_v = config.mu_v
            self.var_v = config.var_v
            self.mu_cy = config.mu_cy
            self.var_cy = config.var_cy
            self.mu_cv = config.mu_cv
            self.rho_j = config.rho_j

    def theta_y(self, c):
        return np.exp(self.mu_y * c + 0.5 * self.var_y * (c ** 2))

    def theta_v(self, c):
        return 1 / (1 - self.mu_v * c)

    def theta_c(self, c1, c2):
        part_1 = np.exp(self.mu_cy * c1 + 0.5 * self.var_y * (c1 ** 2))
        part_2 = 1 - self.mu_cy * c2 - self.rho_j * self.mu_cv * c1
        return part_1 / part_2

    def theta_all(self, c1, c2):
        # print("y")
        # print(self.theta_y(c1))
        # print("v")
        # print(self.theta_v(c2))
        # print("c")
        # print(self.theta_c(c1,c2))
        return (self.lda_y * self.theta_y(c1) + self.lda_v * self.theta_v(c2)
                + self.lda_c * self.theta_c(c1, c2)) / self.lda_bar

    def f_y(self, u, tau):
        return tau * np.exp(self.mu_y * u + 0.5 * self.var_y * (u ** 2))

    def f_v(self, tau, gamma, a, b, exp_e):
        part_1 = ((gamma - b) * tau) / ((gamma - b) + self.mu_v * a)
        part_2 = (2 * self.mu_v * a) / (gamma ** 2 - (b - self.mu_v * a) ** 2)
        part_3 = np.log(1 - ((gamma + b) - self.mu_v * a) * exp_e / (2 * gamma))

        return part_1 + part_2 * part_3

    def f_c(self, u, tau, gamma, a, b, exp_e, c):
        part_1 = tau * np.exp(self.mu_cy * u + 0.5 * self.var_cy * (u ** 2))
        d_1 = ((gamma - b) * tau) / ((gamma - b) * c + self.mu_cv * a)
        d_2 = (2 * self.mu_cv * a) / ((gamma * c) ** 2 - (b * c - self.mu_cv * a) ** 2)
        d_3 = np.log(1 - ((gamma + b) * c - self.mu_cv * a) * exp_e / (2 * gamma * c))
        d = d_1 - d_2 * d_3

        return part_1 * d

    def cf(self, u):
        if self.model == "GBM":
            logCf = 1j * (np.log(self.S0) + (self.r - self.q - self.sig ** 2 / 2) * self.T) * u - \
                    ((self.sig * np.sqrt(self.T)) ** 2 * u ** 2) / 2
            cf = np.exp(logCf)

            return cf

        if self.model == "Heston":
            temp1 = self.kappa - 1j * self.rho * self.sig * u
            gamma = np.sqrt(self.sig ** 2 * (u ** 2 + 1j * u) + temp1 ** 2)

            ele1 = 1j * u * np.log(self.S0)
            ele2 = 1j * u * self.r * self.T
            ele3 = self.kappa * self.theta * self.T * temp1 / self.sig ** 2
            ele4 = -(u ** 2 + 1j * u) * self.v0

            dele1 = np.cosh(gamma * self.T / 2)
            dele2 = (temp1 / gamma) * np.sinh(gamma * self.T / 2)
            pow1 = 2 * self.kappa * self.theta / self.sig ** 2
            # 沒有coth，用coth = 1/tanh
            dele3 = gamma * (1 / np.tanh(gamma * self.T / 2))
            dele4 = temp1

            numer1 = np.exp(ele1 + ele2 + ele3)
            denumer1 = (dele1 + dele2) ** pow1
            finalTerm = np.exp(ele4 / (dele3 + dele4))
            cf = (numer1 / denumer1) * finalTerm
            return cf

        if self.model == "VG":
            # 欠 修!!! if nu == 0

            mu = np.log(self.S0) + (self.r - self.q) * self.T
            denumer1 = 1 - 1j * u * self.theta * self.nu + ((self.sig * u) ** 2 * self.nu) / 2
            pow1 = self.T / self.nu
            cf = np.exp(1j * u * mu) * (1 / denumer1) ** pow1

            return cf

        if self.model == "SV2":
            # tau = T - t = T - 0 = T
            u = 1j * u
            # self.T = -self.T
            b = self.sig * self.rho * u - self.kappa
            a = u * (1 - u)
            gamma = np.sqrt(b ** 2 + a * (self.sig ** 2))

            # beta_bar
            exp_e = 1 - np.exp(-gamma * self.T)
            beta_bar = -(a * exp_e) / (2 * gamma - (gamma + b) * exp_e)

            # alpha
            # 省略-rt!!!
            inter_1 = ((gamma + b) / self.sig ** 2) * self.T
            inter_2 = (2 / self.sig ** 2) * np.log(1 - (gamma + b) * exp_e / (2 * gamma))
            alpha_0 = (self.r - self.q) * u * self.T - self.kappa * self.theta * (inter_1 + inter_2)
            # 沒折現的CF
            cf = np.exp(alpha_0 + u * np.log(self.S0) + beta_bar * self.v0)
            # print(cf)
            return cf
            # lambda項稍後補

        if self.model == "SVJ_Series":
            u = 1j * u
            # self.T = -self.T
            b = self.sig * self.rho * u - self.kappa
            a = u * (1 - u)
            gamma = np.sqrt(b ** 2 + a * (self.sig ** 2))

            # beta_bar
            exp_e = 1 - np.exp(-gamma * self.T)
            beta_bar = -(a * exp_e) / (2 * gamma - (gamma + b) * exp_e)

            # alpha
            # 省略-rt!!!
            inter_1 = ((gamma + b) / self.sig ** 2) * self.T
            inter_2 = (2 / self.sig ** 2) * np.log(1 - (gamma + b) * exp_e / (2 * gamma))
            alpha_0 = (self.r - self.q) * u * self.T - self.kappa * self.theta * (
                        inter_1 + inter_2)  # 省略折現後面計算option price會折

            # 跳動項
            # 問! 用mu_y而不用mu_cy是正確的???
            # 或是要按情況調整mu_bar
            if self.lda_bar != 0:
                c = 1 - self.rho_j * self.mu_cv * u
                mu_bar = self.theta_all(1, 0) - 1
                jump_1 = self.lda_bar * self.T * (1 + mu_bar * u)
                integral = (self.lda_y * self.f_y(u, self.T) + self.lda_v * self.f_v(self.T, gamma, a, b, exp_e)
                            + self.lda_c * self.f_c(u, self.T, gamma, a, b, exp_e, c)) / self.lda_bar
                jump_2 = self.lda_bar * integral
                # 沒折現的CF
                alpha = alpha_0 - jump_1 + jump_2
                cf = np.exp(alpha + u * np.log(self.S0) + beta_bar * self.v0)
            else:
                cf = np.exp(alpha_0 + u * np.log(self.S0) + beta_bar * self.v0)

            return cf
            # lambda項稍後補

    def psi(self, nu, alpha):

        df = math.exp(- self.r * self.T)
        tmp1 = alpha + 1j * nu
        psi = (df / (tmp1 * (tmp1 + 1))) * self.cf(nu - (alpha + 1) * 1j)

        return psi

    def integrateCFOneK(self, alpha, N, eta):

        # no fft
        sumC0T = 0

        for j in range(1, N + 1):

            nuj = (j - 1) * eta
            # print(nuj)
            psij = self.psi(nuj, alpha)

            if j == 1:
                wj = 1 / 2 * eta
            else:
                wj = eta

            # put eta跟N只需決定1個且P0T計算公式會變
            sumC0T += np.exp(-1j * nuj * np.log(self.K)) * psij * wj

        mulTerm = np.exp(-alpha * np.log(self.K)) / np.pi
        C0T = mulTerm * sumC0T
        return np.real(C0T)

    def integrateCFPackFFT(self, alpha, N, eta):

        sumC0T = 0
        lda = 2 * np.pi / (N * eta)
        k = np.log(self.K)
        # 設定法一： 使km在S0兩側
        # beta = np.log(S0) - (N / 2)
        # 設定法二：使km從特定K開始向上加
        beta = np.log(self.K)
        # k 改 km
        # km = beta + (m - 1) * lda

        xjArr = np.zeros(N)
        # ymArr = np.zeros(N)

        # 可向量化
        for j in range(1, N + 1):

            nuj = (j - 1) * eta
            psij = self.psi(nuj, alpha)
            xjExpP = np.exp(-1j * beta * nuj)

            if j == 1:
                wj = 1 / 2 * eta
            else:
                wj = eta

            xj = xjExpP * psij * wj
            xjArr[j - 1] = xj

            # sumExpP = np.exp(-1j * lda * eta * (j - 1) * (m - 1))
            # sumC0T += sumExpP * xj

        ymArr = np.fft.fft(xjArr)
        C0TArr = np.zeros(N)
        for m in range(1, N + 1):
            km = beta + (m - 1) * lda
            mulTerm = np.exp(-alpha * km) / np.pi
            C0T = mulTerm * ymArr[m - 1]
            C0TArr[m - 1] = C0T

        return np.real(C0TArr)

    def IVSurface(self):
        imply_volMat = np.zeros([self.config.ktSAMPLE_NUM, self.config.ktSAMPLE_NUM])
        pbar = tqdm(enumerate(self.config.times), total=self.config.ktSAMPLE_NUM, desc="Pricing")
        for timNum, t in pbar:
            market_prices = []
            for i, K in enumerate(self.config.strike_prices):
                self.K = K
                C0TPack = self.integrateCFPackFFT(self.config.alpha, self.config.N, self.config.eta)
                market_price = C0TPack[0]
                market_prices.append(market_price)  # 把做好的option price存起來準備做IV曲線

            implied_volatilities = []
            # pbar.set_postfix("iii")
            for market_price, K in zip(market_prices, self.config.strike_prices):
                imvol = ImpliedVolatilityCalculator(self.S0, K, t, self.r, self.q)  # 用K=100做IV 問!為何可以固定K???
                implied_volatilitie = imvol.implied_volatility(market_price)
                if np.isnan(implied_volatilitie):
                    if len(implied_volatilities) > 1:
                        implied_volatilities.append(implied_volatilities[len(implied_volatilities) - 2])  # 欠修!
                else:
                    implied_volatilities.append(implied_volatilitie)
                # implied_volatilities.append(round(imvol.implied_volatility(market_price), 4)) # 做IV曲線
            implied_vol = np.array(implied_volatilities)
            imply_volMat[timNum] = implied_vol
        return imply_volMat