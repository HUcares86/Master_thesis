import numpy as np

class Config:
    def __init__(self):
        self.eta = 0.25
        self.alpha = 1.5 # alpha大於0算Call，小於0算Put -> 原因：阿中論文p23
        # ==========================================================================SVJ series 參數
        # Parameters for put
        # 先用moneyess == 1
        # k = math.log(K)
        self.S0 = 50
        self.K = 50
        self.n = 12
        self.N = 2**self.n
        self.model = 'SVJ_Series'
        self.r = 0.0319
        self.q = 0
        # 天數用Year為單位
        self.T = 17/365
        # var往平均收斂速度
        self.kappa = 3.99
        # 平均variance
        self.theta = 0.014
        # variance的variance
        self.sig = 0.27
        # var的dW和lnS的dW的相關性
        self.rho = -0.79
        # 起始的var
        self.v0 = 0.094 ** 2

        # Jump
        self.lda_y = 0
        self.lda_v = 0
        self.lda_v = 0
        self.lda_c = 0
        self.lda_bar = self.lda_y + self.lda_v + self.lda_c

        # mu_bar =
        self.mu_y = 0
        self.var_y = 0
        self.mu_v = 0
        self.var_v = 0
        self.mu_cy = 0
        self.var_cy = 0
        self.mu_cv = 0
        self.rho_j = 0
        self.ktSAMPLE_NUM = 25

        # strike and time
        # 做很多strike_prices並對應Moneyness
        self.strike_prices = np.linspace(35, 75, num=self.ktSAMPLE_NUM)
        self.times = np.linspace(17/365, 2, num=self.ktSAMPLE_NUM)
        self.log_Moneyness = np.log(self.strike_prices) / self.S0
        self.PARAM_NUM = 5

        self.pen_weight_cale = 0.8
        self.pen_weight_butt = 0



