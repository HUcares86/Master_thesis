import numpy as np
from scipy.stats import norm
import math


def d1(S, K, T, q, r, sigma):
    return (np.log(S / K) + (r - q + sigma ** 2 / 2) * T) / sigma * np.sqrt(T)


def d2(S, K, T, q, r, sigma):
    return d1(S, K, T, q, r, sigma) - sigma * np.sqrt(T)


def black_scholes_call(S, K, T, q, r, sigma):
    call_price = S * math.exp(-q * T) * norm.cdf(d1(S, K, T, q, r, sigma)) -\
                 K * math.exp(-r * T) * norm.cdf(d2(S, K, T, q, r, sigma))
    return call_price


def black_scholes_put(S, K, T, q, r, sigma):
    put_price = - S * math.exp(-q * T) * norm.cdf(-d1(S, K, T, q, r, sigma)) +\
                K * math.exp(-r * T) * norm.cdf(-d2(S, K, T, q, r, sigma))
    return put_price

# ------ Greeks -----------------------------------------------------------------------------------------------------
"delta"
def delta_call(S, K, T, q, r, sigma):
    # analytic formula
    N = norm.cdf
    return math.exp(-q * T) *N(d1(S, K, T, q, r, sigma))


def delta_fdm_call(S, K, T, q, r, sigma, ds=1e-8, method='central'):
    # finite difference method
    method = method.lower()
    if method == 'central':
        return (black_scholes_call(S + ds, K, T, q, r, sigma) - black_scholes_call(S - ds, K, T, q, r, sigma)) / \
               (2 * ds)
    elif method == 'forward':
        return (black_scholes_call(S + ds, K, T, q, r, sigma) - black_scholes_call(S, K, T, q, r, sigma)) / ds
    elif method == 'backward':
        return (black_scholes_call(S, K, T, q, r, sigma) - black_scholes_call(S - ds, K, T, q, r, sigma)) / ds


def delta_put(S, K, T, q, r, sigma):
    # analytic formula
    N = norm.cdf
    return - math.exp(-q * T) * N(-d1(S, K, T, q, r, sigma))


def delta_fdm_put(S, K, T, q, r, sigma, ds=1e-8, method='central'):
    # finite difference method
    method = method.lower()
    if method == 'central':
        return (black_scholes_put(S + ds, K, T, q, r, sigma) - black_scholes_put(S - ds, K, T, q, r, sigma)) / \
               (2 * ds)
    elif method == 'forward':
        return (black_scholes_put(S + ds, K, T, q, r, sigma) - black_scholes_put(S, K, T, q, r, sigma)) / ds
    elif method == 'backward':
        return (black_scholes_put(S, K, T, q, r, sigma) - black_scholes_put(S - ds, K, T, q, r, sigma)) / ds

"gamma"

def gamma(S, K, T, q, r, sigma):
    # The formula for gamma is the same for both calls and puts
    N_prime = norm.pdf
    return N_prime(d1(S, K, T, q, r, sigma))/(S*sigma*np.sqrt(T))


def gamma_fdm(S, K, T, q, r, sigma, ds=1e-5, method='central'):
    method = method.lower()
    if method =='central':
        return (black_scholes_call(S + ds, K, T, q, r, sigma) -2*black_scholes_call(S, K, T, q, r, sigma) +
                black_scholes_call(S - ds, K, T, q, r, sigma))/ (ds)**2
    elif method == 'forward':
        return (black_scholes_call(S + 2*ds, K, T, q, r, sigma) - 2*black_scholes_call(S + ds, K, T, q, r, sigma)+
                black_scholes_call(S, K, T, q, r, sigma))/ (ds**2)
    elif method == 'backward':
        return (black_scholes_call(S, K, T, q, r, sigma) - 2*black_scholes_call(S - ds, K, T, q, r, sigma) +
                black_scholes_call(S - 2*ds, K, T, q, r, sigma)) / (ds**2)


"------- Vega --------------------------------------------------------------------------------------------"

def vega_no_q(S, K, T, r, sigma):
    N_prime = norm.pdf
    return S*np.sqrt(T)*N_prime(d1(S,K,T,0,r,sigma))


def black_scholes_vega(S, K, T, q, r, sigma):
    bs_vega = S * math.sqrt(T) * math.exp(-q * T) * norm.pdf(d1(S, K, T, q, r, sigma))
    return bs_vega


def vega_fdm(S, K, T, q, r, sigma, dv=1e-4, method='central'):
    method = method.lower()
    if method == 'central':
        return (black_scholes_call(S, K, T, q, r, sigma+dv) - black_scholes_call(S, K, T, q, r, sigma-dv))/(2*dv)
    elif method == 'forward':
        return (black_scholes_call(S, K, T, q, r, sigma+dv) - black_scholes_call(S, K, T, q, r, sigma))/dv
    elif method == 'backward':
        return (black_scholes_call(S, K, T, q, r, sigma) - black_scholes_call(S, K, T, q, r, sigma-dv))/dv


"------ theta ---------------------------------------------------------------------------------------------"


def theta_call_no_q(S, K, T, r, sigma):
    N_prime = norm.pdf
    N = norm.cdf
    p1 = - S * N_prime(d1(S, K, T, 0, r, sigma)) * sigma / (2 * np.sqrt(T))
    p2 = r * K * np.exp(-r * T) * N(d2(S, K, T, 0, r, sigma))
    return p1 - p2


def theta_put_no_q(S, K, T, r, sigma):
    N_prime = norm.pdf
    N = norm.cdf
    p1 = - S * N_prime(d1(S, K, T, 0, r, sigma)) * sigma / (2 * np.sqrt(T))
    p2 = r * K * np.exp(-r * T) * N(-d2(S, K, T, 0, r, sigma))
    return p1 + p2


def theta_call_fdm(S, K, T, q, r, sigma, dt, method='forward'):
    if method == 'central':
        return -(black_scholes_call(S, K, T+dt, q, r, sigma) - black_scholes_call(S, K, T-dt, q, r, sigma)) / (2 * dt)
    elif method == 'forward':
        return -(black_scholes_call(S, K, T+dt, q, r, sigma) - black_scholes_call(S, K, T, q, r, sigma)) / dt
    elif method == 'backward':
        return -(black_scholes_call(S, K, T, q, r, sigma) - black_scholes_call(S, K, T-dt, q, r, sigma)) / dt


def theta_put_fdm(S, K, T, q, r, sigma, dt, method='forwardl'):
    if method == 'central':
        return -(black_scholes_put(S, K, T+dt, q, r, sigma) - black_scholes_put(S, K, T-dt, q, r, sigma)) / (2 * dt)
    elif method == 'forward':
        return -(black_scholes_put(S, K, T+dt, q, r, sigma) - black_scholes_put(S, K, T, q, r, sigma)) / dt
    elif method == 'backward':
        return -(black_scholes_put(S, K, T, q, r, sigma) - black_scholes_put(S, K, T-dt, q, r, sigma)) / dt


"------ rho ---------------------------------------------------------------------------------------------"


def rho_call_no_q(S, K, T, r, sigma):
    N = norm.cdf
    return K * T * np.exp(-r * T) * N(d2(S, K, T, 0, r, sigma))


def rho_put_no_q(S, K, T, r, sigma):
    N = norm.cdf
    return -K * T * np.exp(-r * T) * N(-d2(S, K, T, 0, r, sigma))


def rho_call_fdm(S, K, T, q, r, sigma, dr, method='central'):
    method = method.lower()
    if method == 'central':
        return (black_scholes_call(S, K, T, q, r+dr, sigma) - black_scholes_call(S, K, T, q, r-dr, sigma)) / (2 * dr)
    elif method == 'forward':
        return (black_scholes_call(S, K, T, q, r+dr, sigma) - black_scholes_call(S, K, T, q, r, sigma)) / dr
    elif method == 'backward':
        return (black_scholes_call(S, K, T, q, r, sigma) - black_scholes_call(S, K, T, q, r-dr, sigma)) / dr


def rho_put_fdm(S, K, T, q, r, sigma, dr, method='central'):
    method = method.lower()
    if method == 'central':
        return (black_scholes_put(S, K, T, q, r+dr, sigma) - black_scholes_put(S, K, T, q, r-dr, sigma)) / (2 * dr)
    elif method == 'forward':
        return (black_scholes_put(S, K, T, q, r+dr, sigma) - black_scholes_put(S, K, T, q, r, sigma)) / dr
    elif method == 'backward':
        return (black_scholes_put(S, K, T, q, r, sigma) - black_scholes_put(S, K, T, q, r-dr, sigma)) / dr