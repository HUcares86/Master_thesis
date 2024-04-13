import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt
fig = plt.figure()
# Define the parameters of the Black-Scholes model
S0 = 100     # Initial price of the underlying asset
r = 0.05     # Risk-free interest rate
q = 0
T = 1        # Time to maturity of the option
K_min = 90   # Minimum strike price of the option
K_max = 110  # Maximum strike price of the option
N_K = 21     # Number of strike prices
K = np.linspace(K_min, K_max, N_K)  # Array of strike prices
V_market = np.array([10.41, 7.45, 4.91, 2.98, 1.65, 0.81, 0.35, 0.14, 0.05, 0.02, 0.01, 0.01, 0.01, 0.02, 0.04, 0.07, 0.12, 0.20, 0.33, 0.51, 0.77])  # Array of market option prices

class ImpliedVolatility:
    def __init__(self, S0, K, T, q, r):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.q = q
        self.MAX_ITERATIONS = 200
        self.PRECISION = 1.0e-4
        self.sigma = 0.3

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

# Calculate the implied volatility smile for the Black-Scholes model
IV = np.zeros(N_K)
for i in range(N_K):
    # IV[i] = implied_volatility(S0, K[i], r, T, V_market[i])
    iv = ImpliedVolatility(S0,  K[i], T, q, r)
    IV[i] = iv.implied_volatility(V_market[i])
print("Implied volatility smile:", IV)
plt.plot(IV)
