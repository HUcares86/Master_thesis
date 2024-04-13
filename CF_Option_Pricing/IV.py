import numpy as np
from scipy.stats import norm
import math
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
# from functions.Parameters import Option_param
# from functions.Processes import Diffusion_process, Merton_process, VG_process, Heston_process
# from functions.BS_pricer import BS_pricer
# from functions.Merton_pricer import Merton_pricer
# from functions.VG_pricer import VG_pricer
# from functions.Heston_pricer import Heston_pricer
from BS import*
from CF_option_pricing import*

import pandas as pd
import scipy as scp
import scipy.stats as ss
import scipy.optimize as scpo
from functools import partial
from itertools import compress
import os
import warnings
warnings.filterwarnings("ignore")

S, K, T, q, r, sigma = 100, 100, 0.25, 0.01, 0.05, 0.1

# call_value = CfOptionPricing(S, K, r, q, T, sigma, "GBM", "call", -2, 12, 0.01, 0.5, [], [], []).evaluate_integral_one_strike()
# print(call_value)

def implied_volatility_bisec(price, S0, K, T, q, r, payoff="call", method="fsolve", disp=True):
    """ Returns Implied volatility
        methods:  fsolve (default) or brent
    """
    def obj_fun(vol):
        return (price - CfOptionPricing(S0, K, r, q, T, vol, "GBM", "call", -2, 12, 0.01, 0.5, [], [], []).evaluate_integral_one_strike())

    if method == "brent":
        x, r = scpo.brentq(obj_fun, a=1e-15, b=500, full_output=True)
        if r.converged == True:
            return x
    if method == "fsolve":
        X0 = [0.1, 0.5, 1, 3]  # set of initial guess points
        for x0 in X0:
            x, _, solved, _ = scpo.fsolve(obj_fun, x0, full_output=True, xtol=1e-8)
            if solved == 1:
                return x[0]

    if disp == True:
        print("Strike", K)
    return -1

# a = implied_volatility_bisec(call_value, S, K, T, q, r)
# print(a)


def implied_volatility_minimize(price, S0, K, T, q, r, payoff="call", disp=True):
    """ Returns Implied volatility by minimization"""

    n = 2  # must be even

    def obj_fun(vol):
        return (CfOptionPricing(S0, K, r, q, T, vol, "GBM", "call", -2, 12, 0.01, 0.5, [], [], []).evaluate_integral_one_strike() - price) ** n

    res = scpo.minimize_scalar(obj_fun, bounds=(1e-15, 8), method='bounded')
    if res.success == True:
        return res.x
    if disp == True:
        print("Strike", K)
    return -1

# a = implied_volatility_minimize(call_value, S, K, T, q, r)
# print(a)



class ImpliedVolatility:
    def __init__(self, S0, K, T, q, r):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.MAX_ITERATIONS = 100
        self.PRECISION = 1.0e-6
        self.sigma = 0.1

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


# a = ImpliedVolatility(S, K, T, q, r)
# print(a.implied_volatility(call_value))



def plot_vol(implied_vol_list, implied_vol_given_list, strike_prices):
    x = strike_prices
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    y = implied_vol_list
    z = implied_vol_given_list
    ax.plot(x, y, label="Implied volatilities (computed)")
    ax.plot(x, z, label="Implied volatilities (given)")
    ax.set_xlabel('Strike price')
    ax.set_ylabel('Implied volatility')
    ax.set_title('Volatility smile')

    strike_labels = strike_prices[::10]
    min_vol = min(implied_vol_list)
    max_vol = max(implied_vol_list)
    vol_labels = np.linspace(min_vol, max_vol, num=5, endpoint=False)

    plt.legend(loc="best")

    ax.set_xticklabels(strike_labels)
    ax.set_yticks(vol_labels)
    plt.show()




