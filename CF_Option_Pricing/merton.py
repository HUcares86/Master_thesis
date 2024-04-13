from scipy.stats import norm
from scipy.optimize import minimize_scalar
N = norm.cdf
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)


def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)


def merton_jump_call(S, K, T, r, sigma, m, v, lam):
    p = 0
    for k in range(40):
        r_k = r - lam * (m - 1) + (k * np.log(m)) / T
        sigma_k = np.sqrt(sigma ** 2 + (k * v ** 2) / T)
        k_fact = np.math.factorial(k)
        p += (np.exp(-m * lam * T) * (m * lam * T) ** k / (k_fact)) * BS_CALL(S, K, T, r_k, sigma_k)

    return p


def merton_jump_put(S, K, T, r, sigma, m, v, lam):
    p = 0  # price of option
    for k in range(40):
        r_k = r - lam * (m - 1) + (k * np.log(m)) / T
        sigma_k = np.sqrt(sigma ** 2 + (k * v ** 2) / T)
        k_fact = np.math.factorial(k)  #
        p += (np.exp(-m * lam * T) * (m * lam * T) ** k / (k_fact)) \
             * BS_PUT(S, K, T, r_k, sigma_k)
    return p


def merton_jump_paths(S, T, r, sigma, lam, m, v, steps, Npaths):
    size = (steps, Npaths)
    dt = T / steps
    poi_rv = np.multiply(np.random.poisson(lam * dt, size=size),np.random.normal(m, v, size=size)).cumsum(axis=0)
    geo = np.cumsum(((r - sigma ** 2 / 2 - lam * (m + v ** 2 * 0.5)) * dt +
                     sigma * np.sqrt(dt) * np.random.normal(size=size)), axis=0)

    return np.exp(geo + poi_rv) * S