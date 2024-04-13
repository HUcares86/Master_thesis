from scipy.stats import norm
import numpy as np
from BS import *
import matplotlib.pyplot as plt

S = 100
K = 120
T = 1
q = 0.01
r = 0.02
sigma = 0.2

prices = np.arange(1, 250, 1)
# print(black_scholes_call(100, 110, 1, 0.02, 0.05, 0.3))

"----- delta --------------------------------------------------------------------------------------------------------"
# deltas_c = delta_call(prices, K, T, q, r, sigma)
# deltas_p = delta_put(prices, K, T, q, r, sigma)
#
# deltas_central_c = delta_fdm_call(prices, K, T, q, r, sigma, ds=0.01, method='central')
# deltas_forward_c = delta_fdm_call(prices, K, T, q, r, sigma, ds=0.01, method='forward')
# deltas_back_c = delta_fdm_call(prices, K, T, q, r, sigma, ds=0.01, method='backward')
#
# deltas_central_p = delta_fdm_put(prices, K, T, q, r, sigma, ds=0.01, method='central')
# deltas_forward_p = delta_fdm_put(prices, K, T, q, r, sigma, ds=0.01, method='forward')
# deltas_back_p = delta_fdm_put(prices, K, T, q, r, sigma, ds=0.01, method='backward')
#
# plt.plot(prices, deltas_c, label='Delta Call')
# plt.plot(prices, deltas_p, label='Delta Put')
# plt.xlabel('$S_0$')
# plt.ylabel('Delta')
# plt.title('Stock Price Effect on Delta for Calls/Puts')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()


# -- testing errors ---------------------------------------------------------------------------------------
#
# error_back_c = np.array(deltas_c) - np.array(deltas_back_c)
# error_central_c = np.array(deltas_c) - np.array(deltas_central_c)
# error_forward_c = np.array(deltas_c) - np.array(deltas_forward_c)
#
# error_central_p = np.array(deltas_p) - np.array(deltas_central_p)
# error_back_p = np.array(deltas_p) - np.array(deltas_back_p)
# error_forward_p = np.array(deltas_p) - np.array(deltas_forward_p)
#
# plt.plot(prices, error_back_c, label='back')
# plt.plot(prices, error_central_c, label='central')
# plt.plot(prices, error_forward_c, label='forward')
# plt.legend()
# plt.xlabel('$S_0$')
# plt.ylabel('FDM Error')
# plt.show()
#
# plt.plot(prices, error_back_p, label='back')
# plt.plot(prices, error_central_p , label='central')
# plt.plot(prices, error_forward_p, label='forward')
# plt.legend()
# plt.xlabel('$S_0$')
# plt.ylabel('FDM Error')
# plt.show()

"------ gamma ------------------------------------------------------------------------------------------------"
# gammas = gamma(prices, K, T, q, r, sigma)
# gamma_forward = gamma_fdm(prices, K, T, q, r, sigma, ds=0.01, method='forward')
#
# plt.plot(prices, gammas)
# plt.plot(prices, gamma_forward)
# plt.title('Gamma by changing $S_0$')
# plt.xlabel('$S_0$')
# plt.ylabel('Gamma')
# plt.show()

"----- vega -----------------------------------------------------------------------------------------------"

# Ts = [1,0.75,0.5,0.25]
#
# for t in Ts:
#     plt.plot(black_scholes_vega(prices, K, t, q, r, sigma), label=f'T = {t}')
# plt.legend()
# plt.xlabel('$S_0$')
# plt.ylabel('Vega')
# plt.title('Vega Decrease with Time')
# plt.show()
#
# vega_central = vega_fdm(prices, K, T, q, r, sigma, dv=1e-4, method='central')
# vega_central2 = vega_fdm(prices, K, T, 0, r, sigma, dv=1e-4, method='central')
# error1 = vega_central - black_scholes_vega(prices, K, T, q, r, sigma)
# error2 = vega_central2 - vega_no_q(prices, K, T, r, sigma)
# plt.plot(prices, error1, label='black')
# plt.plot(prices, error2, label='lack')
# plt.legend()
# plt.xlabel('$S_0$')
# plt.ylabel('FDM Error')
# plt.show()

"----- theta -----------------------------------------------------------------------------------------------"
print(theta_call_fdm(100, 50, 0.25, 0, 0.12, 0.3, 0.5, method='backward'))
# print(theta_call_no_q(100, 100, 1, 0.05, 0.25))
print(theta_call_fdm(100, 50, 0.25, 0, 0.12, 0.3, 0.5, method='central'))
# print(theta_call_no_q(100, K, 0.5, r, sigma))
print(theta_call_fdm(100, 50, 0.25-1/254, 0, 0.12, 0.3, 1/254, method='forward'))
print(theta_call_no_q(100, 50, 0.25+1/365, 0.12, 0.3))

Ts = [1, 0.75, 0.5, 0.25 ]#,0.1, 0.05
for t in Ts:
    plt.plot(theta_call_fdm(prices, 50, t, 0.0, 0.12, 0.3, 1, method='forward'), label=f'T = {t}')

plt.legend()
plt.title('Theta of a call0')
plt.xlabel('$S_0$')
plt.ylabel('Theta')
plt.show()

for t in Ts:
    plt.plot(theta_call_no_q(prices, 50, t, 0.12, 0.3), label=f'T = {t}')

plt.legend()
plt.title('Theta of a call1')
plt.xlabel('$S_0$')
plt.ylabel('Theta')
plt.show()


"----- rho -----------------------------------------------------------------------------------------------"
# print(rho_call_no_q(S, K, T, r, sigma))
# print(rho_call_fdm(S, K, T, 0, r, sigma, 1e-5, method='central'))
#
# print(rho_call_fdm(S, K, T, q, r-0.001, sigma, 1e-10, method='central'))
#
# Ts = [0.0, 0.1, 0.15, 0.2, 0.25]
# for t in Ts:
#     plt.plot(rho_call_fdm(prices, K, t, 0, r, sigma, 1e-5, method='central'), label=f'T = {t}')
# plt.legend()
# plt.title('rho call by changing $S_0$')
# plt.xlabel('$S_0$')
# plt.ylabel('rho')
# plt.show()
#
# for t in Ts:
#     plt.plot(rho_put_fdm(prices, K, t, q, r, sigma, 1e-10, method='central'), label=f'T = {t}')
# plt.legend()
# plt.title('rho put by changing $S_0$')
# plt.xlabel('$S_0$')
# plt.ylabel('rho')
# plt.show()