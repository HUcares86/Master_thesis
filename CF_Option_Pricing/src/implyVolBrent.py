import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm


class ImpliedVolatilityCalculator:
    def __init__(self, S0, K, T, Q, R):
        self.S0 = S0
        self.K = K
        self.T = T
        self.Q = Q
        self.R = R


    def black_scholes(self, sigma):
        d1 = (np.log(self.S0 / self.K) + (self.R - self.Q + 0.5 * sigma ** 2) * self.T) / (sigma * np.sqrt(self.T))
        # print(f"d1: {d1}")
        d2 = d1 - sigma * np.sqrt(self.T)
        # print(f"d2: {d2}")
        C = self.S0 * np.exp(-self.Q * self.T) * norm.cdf(d1) - self.K * np.exp(-self.R * self.T) * norm.cdf(d2)
        return C


    def implied_volatility(self, option_price):
        def f(sigma):
            # print(sigma)
            price = self.black_scholes(sigma)
            # print(f"price: {price}")
            return price - option_price
        # print(f"f(a){f(0.01)}")
        # print(f"f(b){f(0.99)}")
        try:
            sigma = brentq(f, 0.01, 5)
        except ValueError:
            sigma = np.nan
        return sigma


# example usage
# calculator = ImpliedVolatilityCalculator(100, 1, 0.05, 0.05)
# implied_vol = calculator.implied_volatility(95, 10)
# print("Implied volatility: ", implied_vol)