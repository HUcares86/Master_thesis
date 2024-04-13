from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import vega
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from IPython.display import HTML, Image # For GIF
from matplotlib import rc
rc('animation', html='jshtml')

def implied_vol(S0, K, T, r, market_price, flag='c', tol=0.00001):
    """Compute the implied volatility of a European Option
        S0: initial stock price
        K:  strike price
        T:  maturity
        r:  risk-free rate
        market_price: market observed price
        tol: user choosen tolerance
    """
    max_iter = 200 #max number of iterations
    vol_old = 0.30 #initial guess

    for k in range(max_iter):
        bs_price = bs(flag, S0, K, T, r, vol_old)
        Cprime =  vega(flag, S0, K, T, r, vol_old)*100
        C = bs_price - market_price
        vol_new = vol_old - C/Cprime
        bs_new = bs(flag, S0, K, T, r, vol_new)

        if (abs(vol_old - vol_new) < tol or abs(bs_new - market_price) < tol):
            break
        vol_old = vol_new

    implied_vol = vol_old
    return implied_vol

S0, K, T, r = 100, 91, 1, 0.05
market_price = 10.41
implied_vol_est = implied_vol(S0, K, T, r, market_price, flag='c')
print("Implied Volatility is : ", round(implied_vol_est,2)*100, "%")

# S0 = 100     # Initial price of the underlying asset
# r = 0.05     # Risk-free interest rate
# q = 0
# T = 1        # Time to maturity of the option
# K_min = 90   # Minimum strike price of the option
# K_max = 110  # Maximum strike price of the option
# N_K = 21     # Number of strike prices
# K = np.linspace(K_min, K_max, N_K)  # Array of strike prices
# V_market = np.array([10.41, 7.45, 4.91, 2.98, 1.65, 0.81, 0.35, 0.14, 0.05, 0.02, 0.01, 0.01, 0.01, 0.02, 0.04, 0.07, 0.12, 0.20, 0.33, 0.51, 0.77])  # Array of market option prices
