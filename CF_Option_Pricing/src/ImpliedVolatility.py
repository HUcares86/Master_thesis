# import numpy as np
# from scipy.stats import norm
#
#
# class ImpliedVolatility:
#     def __init__(self, S, K, r, q, T, option='call'):
#         self.S = S
#         self.K = K
#         self.r = r
#         self.q = q
#         self.T = T
#         self.option = option
#
#     def black_scholes(self, sigma):
#         d1 = (np.log(self.S / self.K) + (self.r + sigma ** 2 / 2) * self.T) / (sigma * np.sqrt(self.T))
#         d2 = d1 - sigma * np.sqrt(self.T)
#         if self.option == 'call':
#             return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
#         elif self.option == 'put':
#             return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
#         else:
#             raise ValueError("Invalid option type. Must be 'call' or 'put'.")
#
#     def implied_volatility(self, market_price, init_vol=0.4, tol=1e-6, max_iter=10000):
#         vol = init_vol
#         for i in range(max_iter):
#             price = self.black_scholes(vol)
#             vega = self.S * np.sqrt(self.T) * norm.pdf(
#                 (np.log(self.S / self.K) + (self.r + vol ** 2 / 2) * self.T) / (vol * np.sqrt(self.T)))
#             diff = price - market_price
#             if abs(diff) < tol:
#                 return vol
#             vol = vol - diff / vega
#         raise ValueError("Newton method failed to converge.")

# market_price = 4.5
# S = 100
# K = 130
# r = 0.0319
# T = 136/365
# implyVol = ImpliedVolatility(S, K, r, T)
# vol = implyVol.implied_volatility(market_price)
# print(vol)
# price = implyVol.black_scholes(vol)
# print(price)

# ======================================================================

from scipy.stats import norm
import math

class ImpliedVolatility:
    def __init__(self, S0, K, T, r, q):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.MAX_ITERATIONS = 100
        self.PRECISION = 1.0e-6
        self.sigma = 0.2

    def black_scholes(self, sigma):
        d1 = (math.log(self.S0 / self.K) + (self.r - self.q + sigma ** 2 / 2) * self.T) / (sigma * math.sqrt(self.T))
        d2 = d1 - sigma * math.sqrt(self.T)
        call_price = self.S0 * math.exp(-self.q * self.T) * norm.cdf(d1) - self.K * math.exp(-self.r * self.T) * norm.cdf(d2)
        return call_price

    def implied_volatility(self, market_price):
        for i in range(0, self.MAX_ITERATIONS):
            price = self.black_scholes(self.sigma)
            d1 = (math.log(self.S0 / self.K) + (self.r - self.q + self.sigma ** 2 / 2) * self.T) / (self.sigma * math.sqrt(self.T))
            vega = self.S0 * math.sqrt(self.T) * math.exp(-self.q * self.T) * norm.pdf(d1)
            diff = market_price - price
            if abs(diff) < self.PRECISION:
                return self.sigma
            self.sigma = self.sigma + diff/vega
        return self.sigma
        # raise Exception("The Newton Raphson method does not converge")

# bs = ImpliedVolatility(100, 110, 1, 0.05, 0.03)
# market_price = 10.0
# imply_vol = bs.implied_volatility(market_price)
# # imply_vol = bs.sigma
# print("Implied volatility:", bs.sigma)
# price = bs.black_scholes(imply_vol)
# print(price)