import pandas as pd
import os
import matplotlib.colors as mcolors
# -----------------------------
from CF_option_pricing import *
from IV import *
# -----------------------------
from Normal import *
from BS import *
from DG import *
from DE import *
from merton import *
# -----------------------------
from Greeks_mjdg import *
from Greeks_mjde import *
from Greeks_mjn import *
from Greeks_Hedging import *
import time

"----------------------------------------------------------------------------------------------------------------------"

fig = plt.figure()
K_array = np.arange(1, 200, 4)
K_array2 = np.arange(50, 200, 5)
S_array = np.arange(1, 200, 2)
# S_array = np.arange(90, 110, 10)
# S_array = np.arange(1, 1000, 1)
# S_array_2 = np.arange(1, 1000,  1)

S = 100
K = 100
T = 0.25
q = 0.01
r = 0.05  #0.04  0.05  , 0.065
sigma = 0.3
x_array = np.linspace(-10, 10, num=10000)
x_array2 = np.linspace(0, 200, num=600)
color_array = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728','#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
# k = [0.1, 0.2, 0.3 , 0.4 , 0.5 , 0.6 , 0.7]

call_exp = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "call", -2, 14, 0.01, 0.05, K_array, S_array, []).evaluate_integral_one_strike()
print(call_exp)
put_exp = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "put", -2, 14, 0.01, 1.5, K_array, S_array, []).evaluate_integral_one_S0(100)
print(put_exp)
# 5.45 5.450822448427715
# # paper1
# S = 100
# K = 100
# T = 0.25
# q = 0.0
# r = 0.05  #0.04  0.05  , 0.065
# sigma = 0.15
# params = [[0.3445, 0.1, 3.0465, 3.0775]]

# paper2 - 9.14732
# S = 100
# K = 98
# T = 0.5
# q = 0.0
# r = 0.05  #0.04  0.05  , 0.065
# sigma = 0.16
# params = [[0.4, 1, 10, 5]]

"======================================================================================================================"
"============  GBM  ===================================================================================================="
# hedging_d = gbm_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, [], 1000, "call")
# hedging_d.delta_hedging()
# hedging_d.check()
# hedging_d.param_output()
# hedging_results = hedging_d.hedging_results(x_array2)
# plt.plot(x_array2, hedging_results)
# plt.xlabel('$S_0$')
# plt.ylabel('hedging value')
# plt.legend()
# plt.title(f'GBM delta hedging')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.show()

# print('====='*20)
# print("deltaa_gamma")
# hedging_d_g = gbm_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, [], 100, "call")
# hedging_d_g.delta_gamma_hedging()
# hedging_d_g.check()
# hedging_d_g.param_output()
# hedging_results2 = hedging_d_g.hedging_results(x_array2)
# print(hedging_results2)
# plt.plot(x_array2, hedging_results2)
# plt.xlabel('$S_0$')
# plt.ylabel('hedging value')
# plt.legend()
# plt.title(f'GBM delta gamma hedging')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.show()


"======================================================================================================================"
"============  DE  ===================================================================================================="

"------ solve eq ----------"
# # # p_array = [0.1,0.2,  0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# p_array = [0.8]
# # p_array = [0.5, 0.6, 0.7, 0.8, 0.9]0.1, 0.2, 0.3, 0.4,
#
# for p in p_array:
#     print("----------"*10)
#     print("p: ", p)
#     a1, a2 = DE_solve_eq(0, 0, p, "a1,a2,mu,var", 0, 1.5)
#     double_exp_distribution = double_exp(a1, a2, p)
#     f_of_xs_double_g = double_exp_distribution.f_double_exp(x_array)
#     print("------- params ------------")
#     print("numerical")
#     double_exp_distribution.parameters_of_double_exp_numerical()
#     print("analytical")
#     DE_stats(a1, a2, p)
#     plt.plot(x_array, f_of_xs_double_g, label=f'alpha1 = {round(a1, 3)},alpha2 = {round(a2, 3)}, p = {p}')

# plt.axvline(0, color='black', linewidth=1)
# plt.axhline(0, color='black', linewidth=1)
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.title('DG: mean = 0.0 var = 1.5; fix g_beta_1 = g_beta_2 = 5')
# plt.legend()
# plt.ylim(0, 2)
# plt.xlim(-4, 4)
# plt.show()

"------ params ----------"
# # m = 0, var = 1, sk = 0, K = 6
# title = [0, 1, 0, 6]
# params = [
#     # [0.35 , 0.1 , 1.03774904332554 , 1.92724822331886],
#             [0.4 , 0.1 , 1.15470053837925 ,  1.73205080756888 ],
#             [0.45 , 0.1 , 1.27920429813366 , 1.56347191994114],
#             [0.5, 0.1, 1.4142135623731, 1.4142135623731],
#             [0.55 , 0.1 , 1.56347191994114 , 1.27920429813366 ],
#             [0.6 , 0.1 , 1.73205080756888, 1.15470053837925],
#             [0.65 , 0.1 , 1.92724822331886 , 1.03774904332554 ],
#
#           ]

# m = 0, var = 0.5, sk = 0, K = 1.5
# title = [0, 0.5, 0, 1.5]
# params = [
#             [0.3 , 0.1 , 1.30930734141595 , 3.05505046330389 ],
#             # [0.35 , 0.1 , 1.46759877141069 , 2.72554057547699],
#             # [0.36, 0.1, 1.5, 2.66666666666667],
#             # [0.37, 0.1, 1.53271208946963, 2.60975301720504],
#             # [0.38, 0.1, 1.56576272251763, 2.55466549463402],
#             # [0.39, 0.1, 1.59918011780422, 2.50128172271943],
#             [0.4 , 0.1 , 1.63299316185545 , 2.44948974278318 ],
#             [0.5 , 0.1 , 2 ,  2.00000000000000 ],
#             [0.6 , 0.1 , 2.44948974278318 , 1.63299316185545 ],
#             [0.7 , 0.1 , 3.05505046330389 , 1.30930734141595]
#           ]

# m = 0, var = 1.5, sk = 0, K = 13.5
# title = [0, 1.5, 0, 13.5]
# params = [
#     # [0.45 , 0.1 , 1.04446593573419 , 1.27656947700845 ],
#             [0.5 , 0.1 , 1.15470053837925 ,  1.15470053837925 ],
#             [0.55 , 0.1 , 1.27656947700845 ,  1.04446593573419 ],
#             [0.6 , 0.1 , 1.41421356237309 ,  0.942809041582063],
#             [0.65 , 0.1 , 1.57359158493889 ,  0.847318545736323 ],
#             [0.7 , 0.1 , 1.76383420737639  , 0.755928946018455 ],
#             [0.75 , 0.1 , 2.00000000000000 , 0.666666666666667],
#           ]

# m = 0.5, var = 1, sk = 0.216844596451432, K = 7.38066906496526
# title = [0.5, 1, 0.216844596451432,7.38066906496526]
# params = [
#             [0.7 , 0.1 , 1.11001113587127 , 2.29666295470958],
#              [0.8, 0.1, 1.24040820577346,  1.37979589711327],
#              [0.85, 0.1, 2.74873708374511,  0.485071250072666],
#              [0.9, 0.1, 3.46410161513775,  0.384900179459750],
#              [0.95, 0.1, 5.03322295684716,  0.264906471413009],
# ]

# m = 0.5, var = 1.5, sk = 0.294206665032169, K = 15.4760215401628
# title = [0.5, 1.5, 0.294206665032169, 15.4760215401628]
# params = [
#             # [0.75 , 0.1 , 1.04554884989668, 1.15034239616179],
#             [0.8 , 0.1 , 1.11696311977549 ,  0.924950591148529 ],
#         [0.85 , 0.1 , 1.20177057039238 ,  0.723624799525884 ],
#         [0.9 , 0.1 , 1.30971800299921 ,  0.534271301418844 ],
#         [0.95 , 0.1 , 1.46763340896423 ,  0.339441908647102 ],
# #     [0.96 , 0.1 , 1.51200309838002 , 1 , 0.296473447200503 ],
# # [0.97 , 0.1 , 1.56486686215592  , 0.250289836480354 ],
# # [0.98 , 0.1 , 1.63148508341551  , 0.198649741738096 ],
# # [0.99 , 0.1 , 1.72575890730462 , 0.135757669148497 ],
#           ]

# m = 0.5, var = 0.5, sk = 0.240221596568607, K = 2.08255644117388
# title = [0.5, 0.5, 0.240221596568607, 2.08255644117388]
# params = [
#             [0.7 , 0.1 , 1.36713805483493, 24.9614813967711],
# [0.75, 0.1, 1.42020410288673,  8.89897948556636],
#             [0.8 , 0.1 , 1.47759225007252 , 4.82842712474619],
#     [0.85, 0.1, 1.54196742333148,  2.92718271606583],
#             [0.9 , 0.1 , 1.61851286033891, 1.78361162489122],
#             # [0.92, 0.1, 1.65492440697157, 1.43070137332899],
#             # [0.94, 0.1, 1.69686031596161,  1.11184661579252],
#             # [0.96, 0.1, 1.74773603275423,  0.811654839115956],
#           ]

# --------------------------------------------------------------
# params = [
#             [0.5 , 0.1 , 1.2, 1.2],
            # [0.5 , 0.1 , 1.4, 1.4],
             # [0.5 , 0.1 , 1.5, 1.5],
            # [0.5 , 0.1 , 1.6, 1.6],
            # [0.5 , 0.1 , 1.8, 1.8],
            # [0.5 , 0.1 , 2, 2],
            # [0.5 , 0.1 , 2.2, 2.2],
            # [0.5 , 0.1 , 2.4, 2.4],
            # [0.5 , 0.1 , 2.6, 2.6],
            # [0.5 , 0.1 , 2.8, 2.8],
            # [0.5 , 0.1 , 3, 3]
          # ]

# params = [
#             [0.1 , 0.1 , 2 , 2 ],
            # [0.2 , 0.1 , 2 ,  2 ],
            # [0.3 , 0.1 , 2 ,  2 ],
            # [0.4 , 0.1 , 2 ,  2 ],
            # [0.5 , 0.1 , 2 ,  2 ] ,
            # [0.6 , 0.1 , 2 ,  2 ] ,
            # [0.7 , 0.1 , 2 ,  2 ],
            # [0.8 , 0.1 , 2 ,  2 ],
            # [0.9 , 0.1 , 2 , 2 ],
          # ]
"------ distributions -------"
# #
# double_exp_distribution = double_exp(params[0][2], params[0][3], params[0][0])
# f_of_xs_double_g = double_exp_distribution.f_double_exp(x_array)
# DE_stats(params[0][2], params[0][3], params[0][0])
# DE_stats(1.0455, 1.1503, 0.75)
# plt.plot(x_array, f_of_xs_double_g, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.axvline(0, color='black', linewidth=1)
# plt.axhline(0, color='black', linewidth=1)
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.title(f'DE: m = {title[0]}, var = {title[1]}, sk = {round(title[2],3)}, K = {round(title[3],3)}')
# plt.legend()
# plt.ylim(0, 2)
# plt.xlim(-4, 4)
# plt.show()

"------ call prices ----------"
#
# for i in range(len(params)):#
#     print(params[i][2])
#     call_exp = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 14, 0.01, 0.05, K_array, S_array, params[i])
#     # print(call_exp.params)
#     call_exp_prices_spot90 = call_exp.evaluate_integral_one_S0(90)
#     call_exp_prices_spot100 = call_exp.evaluate_integral_one_S0(100)
#     call_exp_prices_spot110 = call_exp.evaluate_integral_one_S0(110)
#     print("&", np.round(call_exp_prices_spot90,4), "&", np.round(call_exp_prices_spot100,4), "&", np.round(call_exp_prices_spot110,4))
#     # print("&", call_exp_prices_spot90, "&", call_exp_prices_spot100, "&", call_exp_prices_spot110)

#     call_exp_prices_spot = call_exp.evaluate_integral_many_S0()
#     plt.plot(S_array, call_exp_prices_spot,label=f'alpha1 = {round(params[i][2], 3)},alpha2 = {round(params[i][3], 3)}, p = {params[i][0]}')
#
# plt.xlabel('$S_0$')
# plt.ylabel('call value')
# # plt.title(f'Double_exp Call value:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()


# 1
# call_exp = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.05, 0.5, K_array, S_array, params[0])
# call_exp_prices_spot = call_exp.evaluate_integral_many_S0()
# plt.plot(S_array, call_exp_prices_spot, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('call value')
# plt.title(f'Double_exp Call value:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()


# 3
# call_exp = CfOptionPricing(90, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 16, 0.05, 0.5, K_array, S_array, params[0])
# call_exp_prices_spot = call_exp.evaluate_integral_one_strike()
# print(call_exp_prices_spot)
# print(call_exp_prices_spot-0.672677)
# print("---------------------------")
# call_exp = CfOptionPricing(100, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 16, 0.05, 0.5, K_array, S_array, params[0])
# call_exp_prices_spot = call_exp.evaluate_integral_one_strike()
# print(call_exp_prices_spot)
# print(call_exp_prices_spot-3.973479)
# print("---------------------------")
# call_exp = CfOptionPricing(110, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 16, 0.05, 0.5, K_array, S_array, params[0])
# call_exp_prices_spot = call_exp.evaluate_integral_one_strike()
# print(call_exp_prices_spot)
# print(call_exp_prices_spot-11.794583)
# print("---------------------------")

"----------- delta ----------------"
# print("----------- delta ----------------")
# for i in range(len(params)):#
#
#     greeks_delta1 = delta_fdm_Double_exp(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8, method='central')
#     greeks_delta2 = delta_fdm_Double_exp(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8,method='central')
#     greeks_delta3 = delta_fdm_Double_exp(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8,method='central')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))

# greeks_delta_array = []
# for S in tqdm(S_array):
#     greeks_delta = delta_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, -2, params[0], "call", ds=1e-8, method='central')
#     greeks_delta_array.append(greeks_delta)

# plt.plot(S_array, greeks_delta_array, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('delta')
# plt.title(f'Double_exp delta value:   m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

"----------- gamma ----------------"
# print("----------- gamma ----------------")
# for i in range(len(params)):#
#
#     greeks_delta1 = gamma_fdm_Double_exp(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
#     greeks_delta2 = gamma_fdm_Double_exp(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
#     greeks_delta3 = gamma_fdm_Double_exp(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))

# greeks_gamma_array = []
# for S in tqdm(S_array):
#     greeks_gamma = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, -2, params[0], "call", ds=1e-2,method='central')
#     greeks_gamma_array.append(greeks_gamma)
# plt.plot(S_array, greeks_gamma_array, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('gamma')
# plt.title(f'Double_exp gamma value:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

"---------------- Vega -----------------"
# print("----------- Vega ----------------")
# for i in range(len(params)):#
#
#     greeks_delta1 = vega_fdm_Double_exp(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
#     greeks_delta2 = vega_fdm_Double_exp(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
#     greeks_delta3 = vega_fdm_Double_exp(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))

# greeks_Vega_array = []
# for S in tqdm(S_array):
#     greeks_Vega = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, -2, params[0], "call", dv=1e-4, method='central')
#     greeks_Vega_array.append(greeks_Vega)
# plt.plot(S_array, greeks_Vega_array, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('Vega')
# plt.title(f'Double_exp Vega value:   m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

"---------------- theta ----------------"
# print("----------- theta ----------------")
# for i in range(len(params)):#
#
#     greeks_delta1 = theta_fdm_Double_exp(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-8, method='forward')
#     greeks_delta2 = theta_fdm_Double_exp(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-8, method='forward')
#     greeks_delta3 = theta_fdm_Double_exp(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-8, method='forward')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))

# greeks_theta_array = []
# for S in tqdm(S_array):
#     greeks_theta = theta_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, -2, params[0], "call", 1e-8, method='forward')
#     greeks_theta_array.append(greeks_theta)
# plt.plot(S_array, greeks_theta_array, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('theta')
# plt.title(f'Double_exp theta value:   m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

"---------------- rho ----------------"
# print("----------- rho ----------------")
# for i in range(len(params)):#
#     greeks_delta1 = rho_fdm_Double_exp(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
#     greeks_delta2 = rho_fdm_Double_exp(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
#     greeks_delta3 = rho_fdm_Double_exp(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))

# greeks_rho_array = []
# for S in tqdm(S_array):
#     greeks_rho = rho_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, -2, params[0], "call", dr=1e-5, method='central')
#     greeks_rho_array.append(greeks_rho)
# plt.plot(S_array, greeks_rho_array, label=f'alpha1 = {round(params[0][2], 3)},alpha2 = {round(params[0][3], 3)}, p = {params[0][0]}')
# plt.xlabel('$S_0$')
# plt.ylabel('rho')
# plt.title(f'Double_exp rho value:   m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

"---------------- pandas ----------------"
# # dictionary of lists
# dict = {'S': S_array,
#         'call': call_exp_prices_spot,
#         'delta': greeks_delta_array,
#         'gamma': greeks_gamma_array,
#         'Vega': greeks_Vega_array,
#         'theta': greeks_theta_array,
#         'rho': greeks_rho_array,
# }
# df = pd.DataFrame(dict)
# print(df)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_0_v_1_l_01_1.csv', index=False)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_0_v_05_l_005_1.csv', index=False)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_05_v_1_l_005_1.csv', index=False)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_05_v_15_l_005_1.csv', index=False)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_05_v_05_l_005_1.csv', index=False)
"---------------- hedging ----------------"

#
# print('====='*20)
# # print("delta_gamma")
# for i in range(len(params)):#
#     print(i)
#     print("delta")
#     # hedging_results = []
#     hedging_d = exp_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, params[i], -100, "call")
#     hedging_d.delta_hedging()
#     hedging_d.check()
#     hedging_d.param_output()
#     hedging_results1 = hedging_d.hedging_results(90)
#     hedging_results2 = hedging_d.hedging_results(110)
#     print(np.round(hedging_results1,4), "&", np.round(hedging_results2,4))
#
#     # hedging_results = hedging_d.hedging_results(x_array2)
#     # plt.plot(x_array2, hedging_results,label="portfolio earnings")
#     # plt.xlabel('$S_0$')
#     # plt.ylabel('hedging value')
#     # plt.legend()
#     # plt.title(f'Double_exp delta hedging:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
#     # plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
#     # plt.show()
#     print("delta gamma ")
#     hedging_d_g = exp_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, params[i], -100, "call")
#     hedging_d_g.delta_gamma_hedging()
#     hedging_d_g.check()
#     hedging_d_g.param_output()
#     hedging_results1 = hedging_d_g.hedging_results(90)
#     hedging_results2 = hedging_d_g.hedging_results(110)
#     print(np.round(hedging_results1,4), "&",np.round( hedging_results2,4))
#     print("+++++++"*20)
# # hedging_results22 = hedging_d_g.hedging_results(x_array2)
# # plt.plot(x_array2, hedging_results22,label="portfolio earnings")
# # plt.xlabel('$S_0$')
# # plt.ylabel('hedging value')
# # plt.legend()
# # plt.title(f'Double_exp delta gamma hedging:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
# # plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# # plt.show()
"---------------- IV ----------------"

# # m = 0, var = 1, sk = 0, K = 6
# m = 0, var = 0.5, sk = 0, K = 1.5
# m = 0, var = 1.5, sk = 0, K = 13.5
# m = 0.5, var = 1, sk = 0.216844596451432, K = 7.38066906496526
# m = 0.5, var = 1.5, sk = 0.294206665032169, K = 15.4760215401628
# m = 0.5, var = 0.5, sk = 0.240221596568607, K = 2.08255644117388

# title = [
#             [0, 1, 0, 6],
#             [0, 0.5, 0, 1.5],
#             [0, 1.5, 0, 13.5],
#             [0.5, 1, 0.216844596451432,7.38066906496526],
#             [0.5, 1.5, 0.294206665032169, 15.4760215401628],
#             [0.5, 0.5, 0.240221596568607, 2.08255644117388]
#             ]
#
# params = [
#             [0.5, 0.1, 1.41421356237310, 1.41421356237310],
#             [0.5, 0.1, 2.01421356237310, 2.01421356237310],
#             [0.5, 0.1, 1.15470053837925, 1.15470053837925],
#             [0.819, 0.05, 1.26922943944091, 1.26922943944091],
#             [0.765, 0.05, 1.06590576033518, 1.07946978122234],
#             [0.91, 0.05, 1.63616021054384, 1.60198637503398]
#           ]
#
# call_exp_array1 = []
# call_exp_array2 = []
# call_exp_array3 = []
# call_exp_array4 = []
# call_exp_array5 = []
# call_exp_array6 = []
#
#
# for K in K_array2:
#     call_exp1 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[0])
#     call_exp_prices_spot1 = call_exp1.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot1, S, K, T, q, r)
#     call_exp_array1.append(iv)

# for K in K_array2:
#     call_exp2 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[1])
#     call_exp_prices_spot2 = call_exp2.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot2, S, K, T, q, r)
#     call_exp_array2.append(iv)
#
# for K in K_array2:
#     call_exp3 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[2])
#     call_exp_prices_spot3 = call_exp3.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot3, S, K, T, q, r)
#     call_exp_array3.append(iv)
#
# for K in K_array2:
#     call_exp4 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[3])
#     call_exp_prices_spot4 = call_exp4.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot4, S, K, T, q, r)
#     call_exp_array4.append(iv)
#
# for K in K_array2:
#     call_exp5 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[4])
#     call_exp_prices_spot5 = call_exp5.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot5, S, K, T, q, r)
#     call_exp_array5.append(iv)
#
# for K in K_array2:
#     call_exp6 = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2, 12, 0.25, 0.5, K_array, S_array, params[5])
#     call_exp_prices_spot6 = call_exp6.evaluate_integral_one_strike()
#     iv = implied_volatility_bisec(call_exp_prices_spot6, S, K, T, q, r)
#     call_exp_array6.append(iv)

#
# plt.plot(call_exp_array1)
# plt.show()
# # dictionary of lists
# dict = {'S': S_array,
#         'call': call_exp_prices_spot,
#         'delta': greeks_delta_array,
#         'gamma': greeks_gamma_array,
#         'Vega': greeks_Vega_array,
#         'theta': greeks_theta_array,
#         'rho': greeks_rho_array,
# }
# df = pd.DataFrame(dict)
# print(df)
# df.to_csv('/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DE/DE_m_0_v_1_l_01_1.csv', index=False)


"======================================================================================================================"
"============  DG  ===================================================================================================="


"------ solve eq ----------"
"---fix g_beta_1, g_beta_2, m = 0 var = 1 -------------------------------------------------"
# # # # p_array = [0.1, 0.2, 0.3, 0.4, 0.5 ,0.6,  0.7, 0.8, 0.9]
# p_array = [0.5]
# # p_array = [0.5, 0.6, 0.7, 0.8, 0.9]
# g_beta_1, g_beta_2 = 4, 4
# # x_array = np.linspace(-10, 10, num=10000)
# for p in p_array:
#     print("----------"*10)
#     print("p: ", p)
#     # a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0, 0.5)
#     # a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0, 1)
#     # a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0, 1.5)
#     # a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0.5, 0.5)
#     # a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0.5, 1)
#     a1_2, a2_2 = DG_solve_eq(g_beta_1, 0, g_beta_2, 0, p, "b1,b2,p", 0.5, 1.5)
#
#     #
#     # a1_2, a2_2, p = DG_solve_eq2(g_beta_1, 0, g_beta_2, 0, 0, "m,v,sk", 0.0, 1, 0, 1)
#     double_gamma_distribution = double_gamma(g_beta_1, a1_2, g_beta_2, a2_2, p)
#     f_of_xs_double_g = double_gamma_distribution.f_double_g(x_array)
#     # DE_stats(a1_2, a2_2, p)
#     print(p,"," ,0.1,",", g_beta_1,",", a1_2,",", g_beta_2,",", a2_2)
#     DG_stats(g_beta_1, a1_2, g_beta_2, a2_2, p)
    # plt.plot(x_array, f_of_xs_double_g, label=f'alpha1 = {round(a1_2, 3)},alpha2 = {round(a2_2, 3)}, p = {p}')



# plt.axvline(0, color='black', linewidth=1)
# plt.axhline(0, color='black', linewidth=1)
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.title('DG: mean = 0.0 var = 1.5; fix g_beta_1 = g_beta_2 = 5')
# plt.legend()
# plt.ylim(0, 2)
# plt.xlim(-4, 4)
# plt.show()

"---fix g_beta_1, g_beta_2, m = 0 var = 1 -------------------------------------------------"
# p_array = [0.5 ,0.6,0.7, 0.8, 0.9]0.1,0.2, 0.3,0.4,
# p_array = [0.8]
# # # p_array = [0.5, 0.6, 0.7, 0.8, 0.9]
# # g_beta_1, g_beta_2 = 1.15470053837925, 1.15470053837925
# g_alpha_1, g_alpha_2 = 3, 3
# # x_array = np.linspace(-10, 10, num=10000)
# for p in p_array:
#     print("------WE---"*10)
#     print("p: ", p)
#     b1_2, b2_2 = DG_solve_eq(3, g_alpha_1, 3, g_alpha_2, p,  "a1,a2,p", 0.5, 1.5)
#     # "b1,b2,p"
#     # a1_2, a2_2, p = DG_solve_eq2(g_beta_1, 0, g_beta_2, 0, 0, "m,v,sk", 0.0, 1, 0, 1)
#     double_gamma_distribution = double_gamma(b1_2, g_alpha_1, b2_2, g_alpha_2, p)
#     f_of_xs_double_g = double_gamma_distribution.f_double_g(x_array)
#     # DE_stats(a1_2, a2_2, p)
#     print(p,"," ,0.1,",", b1_2,",", g_alpha_1,",", b2_2,",",g_alpha_2)
#     # print(p,"&", np.round(b1_2, 4),"&", np.round(b2_2,4),"&" ,0.1)  #"&",g_alpha_2,"&", g_alpha_1
#     print(p, "&", b1_2, "&", b2_2, "&", 0.1)  # "&",g_alpha_2,"&", g_alpha_1
#     DG_stats(b1_2, g_alpha_1, b2_2, g_alpha_2, p)
#     mean, var, Skewness, Kurtosis = DG_stats(b1_2, g_alpha_1, b2_2, g_alpha_2, p)
#     print( mean, "&", var, "&", Skewness, "&", Kurtosis)
#     plt.plot(x_array, f_of_xs_double_g, label=f'alpha1 = {round(g_alpha_1, 3)},alpha2 = {round(g_alpha_2, 3)}, p = {p}')
# plt.axvline(0, color='black', linewidth=1)
# plt.axhline(0, color='black', linewidth=1)
# plt.xlabel('x')
# plt.ylabel('probability')
# plt.title('DG: mean = 0.0 var = 1.5; fix g_beta_1 = g_beta_2 = 5')
# plt.legend()
# plt.ylim(0, 2)
# plt.xlim(-4, 4)
# plt.show()

"------ params ----------"
"---fix alpha , -------------------------------------------------"
# params = [
#             [0.5 , 0.1 , 1.2, 1, 1.2, 1],
#             [0.5 , 0.1 , 1.4, 1, 1.4, 1],
#             [0.5 , 0.1 , 1.6, 1, 1.6, 1],
#             [0.5 , 0.1 , 1.8, 1, 1.8, 1],
#             [0.5 , 0.1 , 2, 1, 2, 1],
#             [0.5 , 0.1 , 2.4, 1, 2.4, 1],
#             [0.5 , 0.1 , 2.6, 1, 2.6, 1],
#             [0.5 , 0.1 , 2.8, 1, 2.8, 1],
#             [0.5 , 0.1 , 3, 1, 3, 1]
#           ]

# params = [
#             [0.5, 0.1, 2, 1.2, 2, 1.2],
#             [0.5, 0.1, 2, 1.4, 2, 1.4],
#             [0.5, 0.1, 2, 1.6, 2, 1.6],
#             [0.5, 0.1, 2, 1.8, 2, 1.8],
#             [0.5, 0.1, 2, 2, 2, 2],
#             [0.5, 0.1, 2, 2.2, 2, 2.2],
#             [0.5, 0.1, 2, 2.4, 2, 2.4],
#             [0.5, 0.1, 2, 2.6, 2, 2.6],
#             [0.5, 0.1, 2, 2.4, 2, 2.4],
#             [0.5, 0.1, 2, 2.6, 2, 2.6],
#           ]
"--- test2 , -------------------------------------------------"
# params = [
#     [0.5 , 0.1 , 1.19932366229484 , 1.5 , 1.19932366229484 , 1.5],
#     [0.5 , 0.1 , 1.94675874014046 , 2 , 1.94675874014046 , 2],
#     [0.5 , 0.1 , 3.50826822121439 , 3 , 3.50826822121439 , 3],
#     [0.6 , 0.1 , 1.24566526679612 , 1.5 , 1.17413601136449 , 1.5],
#     [0.6 , 0.1 , 2.23552765127886 , 2 , 1.68429066337629 , 2],
#     [0.6 , 0.1 , 4.79805799050777 , 3 , 2.25737270181245 , 3],
#
#
#         ]

"---fix alpha ,g_beta_1, g_beta_2, m  var -------------------------------------------------"

# mean = 0, var = 1 fix beta --------------------------------------------------------------------------------
title = [0, 1]

# fix alpha = 1
# params = [
#             # [0.35 , 0.1 , 1.03774904332554 , 1 , 1.92724822331886 , 1],
#             [0.4 , 0.1 , 1.15470053837925 , 1 , 1.73205080756888 , 1],
#             # [0.45 , 0.1 , 1.27920429813366 , 1 , 1.56347191994114 , 1],
#             # [0.5, 0.1, 1.4142135623731, 1.0, 1.4142135623731, 1.0],
#             # [0.55 , 0.1 , 1.56347191994114 , 1 , 1.27920429813366 , 1],
#             [0.6 , 0.1 , 1.73205080756888 , 1 , 1.15470053837925 , 1],
#             # [0.65 , 0.1 , 1.92724822331886 , 1 , 1.03774904332554 , 1],
#                 [0.7 , 0.1 , 2.16024689946929 , 1 , 0.925820099772552 , 1],
#                 [0.8 , 0.1 , 2.82842712474619 , 1 , 0.707106781186547 , 1],
#           ]

# params = [
#             # [0.35 , 0.1 , 1.03774904332554 , 1 , 1.92724822331886 , 1],
#             [0.4 , 0.1 , 1.15470053837925 , 2 , 1.73205080756888 , 2],
#             [0.45 , 0.1 , 1.27920429813366 , 2 , 1.56347191994114 , 2],
#             [0.5, 0.1, 1.4142135623731, 2, 1.4142135623731, 2],
#             [0.55 , 0.1 , 1.56347191994114 , 2 , 1.27920429813366 , 2],
#             [0.6 , 0.1 , 1.73205080756888 , 2 , 1.15470053837925 , 2],
#             [0.65 , 0.1 , 1.92724822331886 , 2 , 1.03774904332554 , 2],
#                 # [0.7 , 0.1 , 2.16024689946929 , 2 , 0.925820099772552 , 2],
#                 # [0.8 , 0.1 , 2.82842712474619 , 2 , 0.707106781186547 , 2],
#           ]

# params = [
#             [0.35 , 0.1 , 1.4142135623731 , 1.38390897394297 , 1.4142135623731 , 0.745181755200060],
#             [0.4 , 0.1 , 1.4142135623731 , 1.23303027798234 , 1.4142135623731 , 0.822020185321561],
#             [0.45 , 0.1 , 1.4142135623731 , 1.10739085445904 , 1.4142135623731 , 0.906047062739213],
#             [0.5 , 0.1 , 1.4142135623731 , 1.00000000000000 , 1.4142135623731 , 1.00000000000000],
#             [0.55 , 0.1 , 1.4142135623731 , 0.906047062739213 , 1.4142135623731 , 1.10739085445904],
#             [0.6 , 0.1 , 1.4142135623731 , 0.822020185321561 , 1.4142135623731 , 1.23303027798234],
#             [0.65 , 0.1 , 1.4142135623731 , 0.745181755200060 , 1.4142135623731 , 1.38390897394297],
#           ]

# mu:  0
# var:  1.00000000000000
# Skewness:  0
# Kurtosis:  6.00000000000000

# params = [
#           [0.1, 0.1, 1.5, 3.68911756223351, 1.5, 0.409901951359278],
#           [0.2, 0.1, 1.5, 2.30483493925200, 1.5, 0.576208734813001],
#           [0.3, 0.1, 1.5, 1.69582971014219, 1.5, 0.726784161489509],
#           [0.4, 0.1, 1.5, 1.33261480900877, 1.5, 0.888409872672513],
#           [0.5, 0.1, 1.5, 1.08113883008419, 1.5, 1.08113883008419],
#           [0.6, 0.1, 1.5, 0.888409872672513, 1.5, 1.33261480900877],
#           [0.7, 0.1, 1.5, 0.726784161489509, 1.5, 1.69582971014219],
#           [0.8, 0.1, 1.5, 0.576208734813001, 1.5, 2.30483493925200],
#           [0.9, 0.1, 1.5, 0.409901951359278, 1.5, 3.68911756223351],
#           ]

# params = [[0.1, 0.1, 2, 5.16712452484701, 2, 0.574124947205223],
#           [0.2, 0.1, 2, 3.27921561087423, 2, 0.819803902718557],
#           [0.3, 0.1, 2, 2.43421973277773, 2, 1.04323702833331],
#           [0.4, 0.1, 2, 1.92190404258370, 2, 1.28126936172247],
#           [0.5, 0.1, 2, 1.56155281280883, 2, 1.56155281280883],
#           [0.6, 0.1, 2, 1.28126936172247, 2, 1.92190404258370],
#           [0.7, 0.1, 2, 1.04323702833331, 2, 2.43421973277773],
#           [0.8, 0.1, 2, 0.819803902718557, 2, 3.27921561087423],
#           [0.9, 0.1, 2, 0.574124947205223, 2, 5.16712452484701],
#           ]


# params = [[0.5 , 0.1 , 0.866025403784439 , 0.5 , 0.866025403784439 , 0.5]]

# mean = 0.0, var = 0.5 fix beta --------------------------------------------------------------------------------


# title = [0, 0.5]

# fix alpha = 1
# params = [
#             [0.3 , 0.1 , 1.30930734141595 , 1 , 3.05505046330389 , 1],
#             # [0.35 , 0.1 , 1.46759877141069 , 1 , 2.72554057547699 , 1],
#             # [0.36 , 0.1 , 1.50000000000000 , 1 , 2.66666666666667 , 1],
#             # [0.37 , 0.1 , 1.53271208946963 , 1 , 2.60975301720504 , 1],
#             # [0.38 , 0.1 , 1.56576272251763 , 1 , 2.55466549463402 , 1],
#             # [0.39 , 0.1 , 1.59918011780422 , 1 , 2.50128172271943 , 1],
#             [0.4 , 0.1 , 1.63299316185545 , 1 , 2.44948974278318 , 1],
#             [0.5 , 0.1 , 2.00000000000000 , 1 , 2.00000000000000 , 1],
#             [0.6 , 0.1 , 2.44948974278318 , 1 , 1.63299316185545 , 1],
#             [0.7 , 0.1 , 3.05505046330389 , 1 , 1.30930734141595 , 1]
#           ]
# params = [
#             [0.3 , 0.1 , 1.30930734141595 , 2 , 3.05505046330389 , 2],
#             # [0.35 , 0.1 , 1.46759877141069 , 1 , 2.72554057547699 , 1],
#             # [0.36 , 0.1 , 1.50000000000000 , 1 , 2.66666666666667 , 1],
#             # [0.37 , 0.1 , 1.53271208946963 , 1 , 2.60975301720504 , 1],
#             # [0.38 , 0.1 , 1.56576272251763 , 1 , 2.55466549463402 , 1],
#             # [0.39 , 0.1 , 1.59918011780422 , 1 , 2.50128172271943 , 1],
#             [0.4 , 0.1 , 1.63299316185545 , 2 , 2.44948974278318 , 2],
#             [0.5 , 0.1 , 2.00000000000000 , 2 , 2.00000000000000 , 2],
#             [0.6 , 0.1 , 2.44948974278318 , 2 , 1.63299316185545 , 2],
#             [0.7 , 0.1 , 3.05505046330389 , 2 , 1.30930734141595 , 2]
#           ]

# params = [
#             [0.1, 0.1, 1.5, 2.40681115275729, 1.5, 0.267423461417477],
#           [0.2, 0.1, 1.5, 1.46715680975093, 1.5, 0.366789202437732],
#           [0.3, 0.1, 1.5, 1.06493625947228, 1.5, 0.456401254059548],
#           [0.4, 0.1, 1.5, 0.830908802125418, 1.5, 0.553939201416946],
#           [0.5, 0.1, 1.5, 0.672603939955857, 1.5, 0.672603939955857],
#           [0.6, 0.1, 1.5, 0.553939201416946, 1.5, 0.830908802125418],
#           [0.7, 0.1, 1.5, 0.456401254059548, 1.5, 1.06493625947228],
#           [0.8, 0.1, 1.5, 0.366789202437732, 1.5, 1.46715680975093],
#           [0.9, 0.1, 1.5, 0.267423461417477, 1.5, 2.40681115275729],
#           ]

# params = [
#           # [0.1, 0.1, 2, 3.43704968844029, 2, 0.381894409826699],
#           # [0.2, 0.1, 2, 2.13938769133981, 2, 0.534846922834953],dr
#           [0.3, 0.1, 2, 1.57082951070015, 2, 0.673212647442920],
#           [0.4, 0.1, 2, 1.23303027798234, 2, 0.822020185321557],
#           [0.5, 0.1, 2, 1.0, 2, 1.0],
#           [0.6, 0.1, 2, 0.822020185321557, 2, 1.23303027798234],
#           [0.7, 0.1, 2, 0.673212647442920, 2, 1.57082951070015],
#           # [0.8, 0.1, 2, 0.534846922834953, 2, 2.13938769133981],
#           # [0.9, 0.1, 2, 0.381894409826699, 2, 3.43704968844029],
#           ]


# mean = 0.0, var = 1.5 fix beta --------------------------------------------------------------------------------
# title = [0, 1.5]

# fix alpha = 1
# params = [
#     # [0.45 , 0.1 , 1.04446593573419 , 1 , 1.27656947700845 , 1],
#             [0.5 , 0.1 , 1.15470053837925 , 1 , 1.15470053837925 , 1],
#             [0.55 , 0.1 , 1.27656947700845 , 1 , 1.04446593573419 , 1],
#             [0.6 , 0.1 , 1.41421356237309 , 1 , 0.942809041582063 , 1],
#             [0.65 , 0.1 , 1.57359158493889 , 1 , 0.847318545736323 , 1],
#             [0.7 , 0.1 , 1.76383420737639 , 1 , 0.755928946018455 , 1],
#             [0.75 , 0.1 , 2.00000000000000 , 1 , 0.666666666666667 , 1],
#           ]

# params = [
#     # [0.45 , 0.1 , 1.04446593573419 , 1 , 1.27656947700845 , 1],
#             [0.5 , 0.1 , 1.15470053837925 , 2 , 1.15470053837925 , 2],
#             [0.55 , 0.1 , 1.27656947700845 , 2 , 1.04446593573419 , 2],
#             [0.6 , 0.1 , 1.41421356237309 , 2 , 0.942809041582063 , 2],
#             [0.65 , 0.1 , 1.57359158493889 , 2 , 0.847318545736323 , 2],
#             [0.7 , 0.1 , 1.76383420737639 , 2 , 0.755928946018455 , 2],
#             [0.75 , 0.1 , 2.00000000000000 , 2 , 0.666666666666667 , 2],
#           ]

# params = [
#           [0.1, 0.1, 1.5, 4.68435314069589, 1.5, 0.520483682299543],
#           [0.2, 0.1, 1.5, 2.96031913539263, 1.5, 0.740079783848158],
#           [0.3, 0.1, 1.5, 2.19223097279591, 1.5, 0.939527559769678],
#           [0.4, 0.1, 1.5, 1.72862620443900, 1.5, 1.15241746962600],
#           [0.5, 0.1, 1.5, 1.40394327646598, 1.5, 1.40394327646598],
#           [0.6, 0.1, 1.5, 1.15241746962600, 1.5, 1.72862620443900],
#           [0.7, 0.1, 1.5, 0.939527559769678, 1.5, 2.19223097279591],
#           [0.8, 0.1, 1.5, 0.740079783848158, 1.5, 2.96031913539263],
#           [0.9, 0.1, 1.5, 0.520483682299543, 1.5, 4.68435314069589],
#           ]
# # #
# params = [
#           [0.1, 0.1, 2, 6.50337760755184, 2, 0.722597511950204],
#           [0.2, 0.1, 2, 4.16386945839634, 2, 1.04096736459909],
#           [0.3, 0.1, 2, 3.10657326213486, 2, 1.33138854091494],
#           [0.4, 0.1, 2, 2.45941170815567, 2, 1.63960780543711],
#           [0.5, 0.1, 2, 2.00, 2, 2.00],
#           [0.6, 0.1, 2, 1.63960780543711, 2, 2.45941170815567],
#           [0.7, 0.1, 2, 1.33138854091494, 2, 3.10657326213486],
#           [0.8, 0.1, 2, 1.04096736459909, 2, 4.16386945839634],
#           [0.9, 0.1, 2, 0.722597511950204, 2, 6.50337760755184],
#           ]


# mean = 0.5, var = 1. fix beta --------------------------------------------------------------------------------
# title = [0.5, 1.0]
# fix alpha = 1
# params = [
#             [0.7 , 0.1 , 1.11001113587127 , 1 , 2.29666295470958 , 1],
#             [0.75 , 0.1 , 1.17157287525381 , 1 , 1.78361162489122 , 1],
#             [0.8 , 0.1 , 1.24040820577346 , 1 , 1.37979589711327 , 1],
#             [0.85 , 0.1 , 1.32057154523713 , 1 , 1.04412691931271 , 1],
#             [0.9 , 0.1 , 1.42020410288673 , 1 , 0.747877538267963 , 1],
#           ]

# params = [
#             [0.7 , 0.1 , 1.11001113587127 , 2 , 2.29666295470958 , 2],
#             [0.75 , 0.1 , 1.17157287525381 , 2 , 1.78361162489122 , 2],
#             [0.8 , 0.1 , 1.24040820577346 , 2 , 1.37979589711327 , 2],
#             [0.85 , 0.1 , 1.32057154523713 , 2 , 1.04412691931271 , 2],
#             [0.9 , 0.1 , 1.42020410288673 , 2 , 0.747877538267963 , 2],
#           ]

# params = [[0.819 , 0.1 , 1.5 , 1.22035601862857 , 1.5 , 1.37829601799337]]
# mu:  0.500000000000000
# var:  1.00000000000000
# Skewness:  -0.101397886544433
# Kurtosis:  6.33153202892176


# params = [[0.819 , 0.1 , 2 , 1.69977642169060 , 2 , 2.16639165394809]]
#mu:  0.500000000000000
# var:  1.00000000000000
# Skewness:  -0.533464740479102
# Kurtosis:  5.25925458996032

# params = [
#         # [0.1 , 0.1 , 1.5 , 4.99392845984467 , 1.5 , -0.278452393350592],
#         # [0.2 , 0.1 , 1.5 , 3.33230690505755 , 1.5 , -0.104423273735612],
#         [0.3 , 0.1 , 1.5 , 2.58771550808990 , 1.5 , 0.0375923606099588],
#         [0.4 , 0.1 , 1.5 , 2.13997487421324 , 1.5 , 0.176649916142160],
#         [0.5 , 0.1 , 1.5 , 1.83113883008419 , 1.5 , 0.331138830084190],
#         [0.6 , 0.1 , 1.5 , 1.59899959967968 , 1.5 , 0.523499399519519],
#         [0.7 , 0.1 , 1.5 , 1.41214047088473 , 1.5 , 0.794994432064365],
#         [0.8 , 0.1 , 1.5 , 1.25000000000000 , 1.5 , 1.25000000000000],
#         [0.9 , 0.1 , 1.5 , 1.08969686527576 , 1.5 , 2.30727178748188]
# ]
#
# params = [
#         # [0.1 , 0.1 , 2 , 6.73400331624879 , 2 , -0.362888520416801],
#         # [0.2 , 0.1 , 2 , 4.56348484585429 , 2 , -0.109128788536429],
#         [0.3 , 0.1 , 2 , 3.57973576171415 , 2 , 0.105601040734634],
#         [0.4 , 0.1 , 2 , 2.98069758011279 , 2 , 0.320465053408525],
#         [0.5 , 0.1 , 2 , 2.56155281280883 , 2 , 0.561552812808830],
#         [0.6 , 0.1 , 2 , 2.24113781667882 , 2 , 0.861706725018234],
#         [0.7 , 0.1 , 2 , 1.97783298707505 , 2 , 1.28161030317511],
#         [0.8 , 0.1 , 2 , 1.74339811320566 , 2 , 1.97359245282264],
#         [0.9 , 0.1 , 2 , 1.50461190490724 , 2 , 3.54150714416512]
# ]
#
# # mean = 0.5, var = 1.5 fix beta --------------------------------------------------------------------------------
# title = [0.5, 1.5]
# fix alpha = 1
#

# params = [
#             # [0.75 , 0.1 , 1.04554884989668 , 1 , 1.15034239616179 , 1],
#             [0.8 , 0.1 , 1.11696311977549 , 1 , 0.924950591148529 , 1],
#             [0.85 , 0.1 , 1.20177057039238 , 1 , 0.723624799525884 , 1],
#             [0.9 , 0.1 , 1.30971800299921 , 1 , 0.534271301418844 , 1],
#             [0.95 , 0.1 , 1.46763340896423 , 1 , 0.339441908647102 , 1],
#             # [0.96 , 0.1 , 1.51200309838002 , 1 , 0.296473447200503 , 1],
#             # [0.97 , 0.1 , 1.56486686215592 , 1 , 0.250289836480354 , 1],
#             # [0.98 , 0.1 , 1.63148508341551 , 1 , 0.198649741738096 , 1],
#             # [0.99 , 0.1 , 1.72575890730462 , 1 , 0.135757669148497 , 1],
#           ]

# params = [
#              # [0.75 , 0.1 , 1.04554884989668 , 1 , 1.15034239616179 , 1],
#             [0.8 , 0.1 , 1.11696311977549 , 2 , 0.924950591148529 , 2],
#             [0.85 , 0.1 , 1.20177057039238 , 2 , 0.723624799525884 , 2],
#             [0.9 , 0.1 , 1.30971800299921 , 2 , 0.534271301418844 , 2],
#             [0.95 , 0.1 , 1.46763340896423 , 2 , 0.339441908647102 , 2],
#             # [0.96 , 0.1 , 1.51200309838002 , 1 , 0.296473447200503 , 1],
#             # [0.97 , 0.1 , 1.56486686215592 , 1 , 0.250289836480354 , 1],
#             # [0.98 , 0.1 , 1.63148508341551 , 1 , 0.198649741738096 , 1],
#             # [0.99 , 0.1 , 1.72575890730462 , 1 , 0.135757669148497 , 1],
#           ]


# params = [[0.91 , 0.1 , 1.5 , 1.19015755485236 , 1.5 , 3.70048194350720]]
# # mu:  0.500000000000000
# # var:  1.50000000000000
# # Skewness:  -2.77699525650527
# # Kurtosis:  21.3159722154214
#
# params = [[0.91 , 0.1 , 2 , 1.63139288346066 , 2 , 5.38408359943561]]
# # mu:  0.500000000000000
# # var:  1.50000000000000
# # Skewness:  -3.45710525322229
# # Kurtosis:  20.6777594775636


# params = [
# #     # [0.1 , 0.1 , 1.5 , 5.89855354609679 , 1.5 , -0.177938494878135],
# #     [0.2 , 0.1 , 1.5 , 3.94249295553543 , 1.5 , 0.0481232388838564],
# #     [0.3 , 0.1 , 1.5 , 3.06081384346492 , 1.5 , 0.240348790056394],
# #     [0.4 , 0.1 , 1.5 , 2.52644692766323 , 1.5 , 0.434297951775486],
# #     [0.5 , 0.1 , 1.5 , 2.15394327646598 , 1.5 , 0.653943276465977],
# #     [0.6 , 0.1 , 1.5 , 1.86986841535707 , 1.5 , 0.929802623035599],
# #     [0.7 , 0.1 , 1.5 , 1.63653155999204 , 1.5 , 1.31857363998143],
# #     [0.8 , 0.1 , 1.5 , 1.42820840351251 , 1.5 , 1.96283361405006],
# #     [0.9 , 0.1 , 1.5 , 1.21421036266036 , 1.5 , 3.42789326394323],
# # ]
#
# # params = [
# #     # [0.1 , 0.1 , 2 , 7.97464284904401 , 2 , -0.225039683439554],
# #     [0.2 , 0.1 , 2 , 5.40000000000000 , 2 , 0.100000000000000],
# #     [0.3 , 0.1 , 2 , 4.22725519075770 , 2 , 0.383109367467588],
# #     [0.4 , 0.1 , 2 , 3.50805405358401 , 2 , 0.672036035722674],
# #     [0.5 , 0.1 , 2 , 3.00000000000000 , 2 , 1.00000000000000],
# #     [0.6 , 0.1 , 2 , 2.60665559243899 , 2 , 1.40998338865848],
# #     [0.7 , 0.1 , 2 , 2.27797338380595 , 2 , 1.98193789554722],
# #     [0.8 , 0.1 , 2 , 1.97898261225516 , 2 , 2.91593044902064],
# #     [0.9 , 0.1 , 2 , 1.66666666666667 , 2 , 5.00000000000000],
# # ]
#
# # mean = 0.5, var =0.5 fix beta --------------------------------------------------------------------------------
# title = [0.5, 0.5]
# fix alpha = 1
#
# params = [
#             [0.7 , 0.1 , 1.36713805483493 , 1 , 24.9614813967711 , 1],
#             [0.75 , 0.1 , 1.42020410288673 , 1 , 8.89897948556636 , 1],
#             [0.8 , 0.1 , 1.47759225007252 , 1 , 4.82842712474619 , 1],
#             [0.85 , 0.1 , 1.54196742333148 , 1 , 2.92718271606583 , 1],
#             [0.9 , 0.1 , 1.61851286033891 , 1 , 1.78361162489122 , 1],
#             # [0.92 , 0.1 , 1.65492440697157 , 1 , 1.43070137332899 , 1],
#             # [0.94 , 0.1 , 1.69686031596161 , 1 , 1.11184661579252 , 1],
#             # [0.96 , 0.1 , 1.74773603275423 , 1 , 0.811654839115956 , 1]
#           ]

# params = [
#             [0.7 , 0.1 , 1.36713805483493 , 2 , 24.9614813967711 , 2],
#             [0.75 , 0.1 , 1.42020410288673 , 2 , 8.89897948556636 , 2],
#             [0.8 , 0.1 , 1.47759225007252 , 2 , 4.82842712474619 , 2],
#             [0.85 , 0.1 , 1.54196742333148 , 2 , 2.92718271606583 , 2],
#             [0.9 , 0.1 , 1.61851286033891 , 2 , 1.78361162489122 , 2],
#             # [0.92 , 0.1 , 1.65492440697157 , 1 , 1.43070137332899 , 1],
#             # [0.94 , 0.1 , 1.69686031596161 , 1 , 1.11184661579252 , 1],
#             # [0.96 , 0.1 , 1.74773603275423 , 1 , 0.811654839115956 , 1]
#           ]

# params = [[0.765 , 0.1 , 1.5 , 1.04292555550652 , 1.5 , 0.203566170053124]]
# mu:  0.500000000000000
# var:  0.500000000000000
# Skewness:  0.556959558728520
# Kurtosis:  2.11472502696896

# params = [[0.765 , 0.1 , 2 , 1.47689439346787 , 2 , 0.552443451076244]]
# mu:  0.500000000000000
# var:  0.500000000000000
# Skewness:  0.276937726874535
# Kurtosis:  1.47033537509073



# params = [
#     # [0.1 , 0.1 , 1.5 , 3.89165807559224 , 1.5 , -0.400926880489751],
#     # [0.2 , 0.1 , 1.5 , 2.58438797446390 , 1.5 , -0.291403006384025],
#     # [0.3 , 0.1 , 1.5 , 2.00320249846246 , 1.5 , -0.212913214944660],
#     # [0.4 , 0.1 , 1.5 , 1.65748134316813 , 1.5 , -0.145012437887911],
#     # [0.5 , 0.1 , 1.5 , 1.42260393995586 , 1.5 , -0.0773960600441427],
#     # [0.6 , 0.1 , 1.5 , 1.25000000000000 , 1.5 , -1.12757180344224e-16],
#     [0.7 , 0.1 , 1.5 , 1.11601158291086 , 1.5 , 0.104027026792005],
#     [0.8 , 0.1 , 1.5 , 1.00689167206243 , 1.5 , 0.277566688249706],
#     [0.9 , 0.1 , 1.5 , 0.911406452355969 , 1.5 , 0.702658071203718],
# ]
#
# # params = [
# #     # [0.1 , 0.1 , 2 , 5.20000000000000 , 2 , -0.533333333333333],
# #     # [0.2 , 0.1 , 2 , 3.52264954516723 , 2 , -0.369337613708192],
# #     # [0.3 , 0.1 , 2 , 2.76779253585061 , 2 , -0.242374627492594],
# #     # [0.4 , 0.1 , 2 , 2.31311264697090 , 2 , -0.124591568686067],
# #     # [0.5 , 0.1 , 1.5 , 2 , 1.5 , 0],
# #     # [0.6 , 0.1 , 2 , 1.76619037896906 , 2 , 0.149285568453590],
# #     [0.7 , 0.1 , 2 , 1.58074643667419 , 2 , 0.355075018906447],
# #     [0.8 , 0.1 , 2 , 1.42449979983984 , 2 , 0.697999199359359],
# #     [0.9 , 0.1 , 2 , 1.27859388972002 , 2 , 1.50734500748016],
# # ]
"------------------------------"
# params = [
#             # [0.5 , 0.1 , 1.2 , 1, 1.2 , 1],
#             [0.5 , 0.1 , 1.4 , 1, 1.4 , 1],
#             # [0.5 , 0.1 , 1.6 , 1, 1.6 , 1],
#             # [0.5 , 0.1 , 1.8 , 1, 1.8 , 1],
#             [0.5 , 0.1 , 2   , 1,   2 , 1] ,
#             # [0.5 , 0.1 , 2.2 , 1, 2.2 , 1] ,
#             # [0.5 , 0.1 , 2.4 , 1, 2.4 , 1],
#             # [0.5 , 0.1 , 2.6 , 1, 2.6 , 1],
#             # [0.5 , 0.1 , 2.8 , 1, 2.8 , 1],
#             [0.5 , 0.1 , 3   , 1,   3 , 1]
#           ]

# params = [
#             # [0.5 , 0.1 , 1.2 , 2, 1.2 , 2],
#             [0.5 , 0.1 , 1.4 , 2, 1.4 , 2],
#             [0.5 , 0.1 , 1.6 , 2, 1.6 , 2],
#             [0.5 , 0.1 , 1.8 , 2, 1.8 , 2],
#             [0.5 , 0.1 , 2.0 , 2, 2.0 , 2] ,
#             [0.5 , 0.1 , 2.2 , 2, 2.2 , 2] ,
#             [0.5 , 0.1 , 2.4 , 2, 2.4 , 2],
#             [0.5 , 0.1 , 2.6 , 2, 2.6 , 2],
#             [0.5 , 0.1 , 2.8 , 2, 2.8 ,2],
#             [0.5 , 0.1 , 3.0 , 2, 3.0 , 2]
#           ]
#
# params = [
#             # [0.9 , 0.1 , 1.2 , 2, 1.2 , 2],
#             [0.9 , 0.1 , 1.4 , 2, 1.4 , 2],
#             [0.9 , 0.1 , 1.6 , 2, 1.6 , 2],
#             [0.9 , 0.1 , 1.8 , 2, 1.8 , 2],
#             [0.9 , 0.1 , 2.0 , 2, 2.0 , 2] ,
#             [0.9 , 0.1 , 2.2 , 2, 2.2 , 2] ,
#             [0.9 , 0.1 , 2.4 , 2, 2.4 , 2],
#             [0.9 , 0.1 , 2.6 , 2, 2.6 , 2],
#             [0.9 , 0.1 , 2.8 , 2, 2.8 ,2],
#             [0.9 , 0.1 , 3.0 , 2, 3.0 , 2]
#           ]

# params = [
#             # [0.5 , 0.1 , 1.2 , 2, 1.2 , 2],
#             # [0.9 , 0.1 , 1.2 , 2, 1.2 , 2],
#             [0.5 , 0.1 , 1.4 , 2.0, 1.4 , 2.0],
#             # [0.9 , 0.1 , 1.4 , 2, 1.4 , 2],
#             # [0.5, 0.1, 1.5, 2, 1.5, 2],
#             # [0.9, 0.1, 1.5, 2, 1.5, 2],
#             # [0.5 , 0.1 , 1.6 , 2, 1.6 , 2],
#             # [0.9 , 0.1 , 1.6 , 2, 1.6 , 2],
#             # [0.5 , 0.1 , 1.8 , 2, 1.8 , 2],
#             [0.5 , 0.1 , 2.0 , 2.0, 2.0 , 2.0] ,
#             # [0.9, 0.1, 2.0, 2, 2.0, 2],
#             # [0.5 , 0.1 , 2.2 , 2, 2.2 , 2] ,
#             # [0.5 , 0.1 , 2.4 , 2, 2.4 , 2],
#             # [0.5 , 0.1 , 2.6 , 2, 2.6 , 2],
#             # [0.5 , 0.1 , 2.8 , 2, 2.8 ,2],
#             [0.5 , 0.1 , 3.0 , 2.0, 3.0 , 2.0],
#             [0.9, 0.1, 3.0, 2.0, 3.0, 2.0]
#           ]

"------------------------------"
# params = [
#             [0.5 , 0.1 , 2 , 1.2, 2 , 1.2],
#             [0.5 , 0.1 , 2 , 1.4, 2 , 1.4],
#             [0.5 , 0.1 , 2 , 1.6, 2 , 1.6],
#             [0.5 , 0.1 , 2 , 1.8, 2 , 1.8],
#             [0.5 , 0.1 , 2 , 2.0,   2 , 2.0],
#             [0.5 , 0.1 , 2 , 2.2, 2 , 2.2] ,
#             [0.5 , 0.1 , 2 , 2.4, 2 , 2.4],
#             [0.5 , 0.1 , 2 , 2.6, 2,  2.6],
#             [0.5 , 0.1 , 2 , 2.8, 2 , 2.8],
#             [0.5 , 0.1 , 2 , 3.0,   2 , 3.0]
#           ]
# #
# params = [
#             [0.5 , 0.1 , 3 , 1.2, 3 , 1.2],
#             [0.5 , 0.1 , 3 , 1.4, 3 , 1.4],
#             [0.5 , 0.1 , 3 , 1.6, 3 , 1.6],
#             [0.5 , 0.1 , 3 , 1.8, 3 , 1.8],
#             [0.5 , 0.1 , 3 , 2.0, 3 , 2.0],
#             [0.5 , 0.1 , 3 , 2.2, 3 , 2.2] ,
#             [0.5 , 0.1 , 3 , 2.4, 3 , 2.4],
#             [0.5 , 0.1 , 3 , 2.6, 3,  2.6],
#             [0.5 , 0.1 , 3 , 2.8, 3 , 2.8],
#             [0.5 , 0.1 , 3 , 3.0, 3 , 3.0]
#           ]

# params = [
#             [0.5 , 0.1 , 2.0 , 1.2, 2.0 , 1.2],
#             # [0.5 , 0.1 , 2 , 1.4, 2 , 1.4],
#             # [0.5 , 0.1 , 2 , 1.6, 2 , 1.6],
#             # [0.5 , 0.1 , 2 , 1.8, 2 , 1.8],
#             [0.5 , 0.1 , 2.0 , 2.0,   2.0 , 2.0],
#             # [0.5 , 0.1 , 2 , 2.2, 2 , 2.2] ,
#             # [0.5 , 0.1 , 2 , 2.4, 2 , 2.4],
#             # [0.5 , 0.1 , 2 , 2.6, 2,  2.6],
#             # [0.5 , 0.1 , 2 , 2.8, 2 , 2.8],
#             [0.5 , 0.1 , 2.0 , 3.0,   2.0 , 3.0],
#             [0.5 , 0.1 , 3.0 , 3.0, 3.0 , 3.0]
#           ]

"------------------------------"
# params = [
#             # [0.1 , 0.1 , 2 , 2, 2 , 2],
#             # [0.2 , 0.1 , 2 , 2, 2 , 2],
#             # [0.3 , 0.1 , 2 , 2, 2 , 2],
#             [0.4 , 0.1 , 2 ,  2, 2 , 2],
#             # [0.5 , 0.1 , 2  , 2,   2 , 2],
#             [0.6 , 0.1 , 2 ,  2, 2 , 2] ,
#             # [0.7 , 0.1 , 2 ,  2, 2 , 2],
#             # [0.8 , 0.1 , 2 ,  2, 2 , 2],
#             # [0.9 , 0.1 , 2 ,  2, 2 , 2],
#           ]
#
# params = [
#             # [0.1 , 0.1 , 3 , 2, 3 , 2],
#             # [0.2 , 0.1 , 3 , 2, 3 , 2],
#             # [0.3 , 0.1 , 3 , 2, 3 , 2],
#             [0.4 , 0.1 , 3 , 2, 3 , 2],
#             [0.5 , 0.1 , 3 , 2, 3 , 2],
#             [0.6 , 0.1 , 3 , 2, 3 , 2] ,
#             # [0.7 , 0.1 , 3 , 2, 3 , 2],
#             # [0.8 , 0.1 , 3 , 2, 3 , 2],
#             # [0.9 , 0.1 , 3 , 2, 3 , 2],
# ]
# params = [
#             [0.5 , 0.1 , 2  , 2,   2 , 2],
#              [0.5, 0.1, 3, 2, 3, 2],
#
#
#           ]

"------------------------------"
# params = [
#             [0.1 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.2 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.3 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.4 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.5 , 0.1 , 2 , 0.5, 2 , 0.5] ,
#             [0.6 , 0.1 , 2 , 0.5, 2 , 0.5] ,
#             [0.7 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.8 , 0.1 , 2 , 0.5, 2 , 0.5],
#             [0.9 , 0.1 , 2 , 0.5, 2 , 0.5],
#           ]

#
# params = [
#             # [0.1 , 0.1 , 2 , 1, 2 , 1],
#             # [0.2 , 0.1 , 2 , 1, 2 , 1],
#             # [0.3 , 0.1 , 2 , 1, 2 , 1],
#             # [0.4 , 0.1 , 2 , 1, 2 , 1],
#             [0.5 , 0.1 , 2 , 1, 2 , 1] ,
#             [0.6 , 0.1 , 2 , 1, 2 , 1] ,
#             [0.7 , 0.1 , 2 , 1, 2 , 1],
#             [0.8 , 0.1 , 2 , 1, 2 , 1],
#             [0.9 , 0.1 , 2 , 1, 2 , 1],
#           ]
# #
# params = [
#             [0.1 , 0.1 ,  2 , 2, 2 , 2],
#             [0.2 , 0.1 ,  2 , 2, 2 , 2],
#             [0.3 , 0.1 ,  2 , 2, 2 , 2],
#             [0.4 , 0.1 ,  2 , 2, 2 , 2],
#             [0.5 , 0.1 ,  2 , 2, 2 , 2] ,
#             [0.6 , 0.1 ,  2 , 2, 2 , 2] ,
#             [0.7 , 0.1 ,  2 , 2, 2 , 2],
#             [0.8 , 0.1 ,  2 , 2, 2 , 2],
#             [0.9 , 0.1 ,  2 , 2, 2 , 2],
#           ]

params = [
                [0.1 , 0.1 ,  2 , 2, 2 , 2],
            # [0.2 , 0.1 , 2 , 0.5, 2 , 0.5],
            # [0.3 , 0.1 , 2 , 0.5, 2 , 0.5],
            # [0.4 , 0.1 , 2 , 0.5, 2 , 0.5],
                [0.5 , 0.1 ,  2 , 2, 2 , 2] ,
            # [0.6 , 0.1 , 2 , 0.5, 2 , 0.5] ,
            # [0.7 , 0.1 , 2 , 0.5, 2 , 0.5],
            # [0.8 , 0.1 , 2 , 0.5, 2 , 0.5],
             [0.9, 0.1, 2, 2, 2, 2],
            [0.9 , 0.1 , 2 , 0.5, 2 , 0.5],
    # [0.9, 0.1, 2, 2, 2, 2],

          ]

" draw -----------------------------"
# 0.8
# params = [
#             [0.8 , 0.1 , 3.39411254969543 , 0.8 , 0.848528137423857 , 0.8 ],
#             # [0.8 , 0.1 , 2.40000000000000 , 0.8 , 0.600000000000000 , 0.8 ],
#             # [0.8 , 0.1 , 1.95959179422654 , 0.8 , 0.489897948556636 , 0.8 ]    ,
#             # [0.8 , 0.1 , 1.24158521961633 , 0.8 , 10.3425625842204 , 0.8 ],
#             # [0.8 , 0.1 , 1.03041608050353 , 0.8 , 1.32113137106891 , 0.8 ],
#             # [0.8 , 0.1 , 0.926739420118208 , 0.8 , 0.839484027731201 , 0.8 ],
#           ]


# fix m v change  beta
# 1
# params = [
#             [0.8 , 0.1 , 4 , 1 , 1 , 1],
#             [0.8 , 0.1 , 2.82842712474619 , 1 , 0.707106781186547 , 1],
#             [0.8 , 0.1 , 2.30940107675850, 1 ,  0.577350269189626, 1 ]    ,
#             [0.8 , 0.1 , 1.47759225007252 , 1 , 4.82842712474619 , 1],
#             [0.8 , 0.1 , 1.24040820577346 , 1 , 1.37979589711327 , 1],
#             [0.8 , 0.1 , 1.11696311977549 , 1 , 0.924950591148529 , 1],
#           ]

# 2
# params = [
#             [0.8 , 0.1 , 6.92820323027551 , 2 , 1.73205080756888 , 2],
#             [0.8 , 0.1 , 4.89897948556636 , 2 , 1.22474487139159 , 2 ],
#             [0.8 , 0.1 , 4.00000000000000 , 2 , 1.00000000000000 , 2]    ,
#             [0.8 , 0.1 , 2.66666666666667 , 2 , 4.00000000000000 , 2 ],
#             [0.8 , 0.1 , 2.26787888807066 , 2 , 1.94642422238587 , 2 ],
#             [0.8 , 0.1 , 2.04349882769577 , 2 , 1.41357319932449 , 2 ],
#           ]

# params = [
#                 # [0.8 , 0.1 , 3.39411254969543 , 0.8 , 0.848528137423857 , 0.8 ],
#                 [0.8 , 0.1 , 2.40000000000000 , 0.8 , 0.600000000000000 , 0.8 ],
#                 # [0.8 , 0.1 , 1.95959179422654 , 0.8 , 0.489897948556636 , 0.8 ]    ,
#             # [0.8 , 0.1 , 4 , 1 , 1 , 1],
#             [0.8 , 0.1 , 2.82842712474619 , 1.0 , 0.707106781186547 , 1.0],
#             # [0.8 , 0.1 , 2.30940107675850, 1 ,  0.577350269189626, 1 ]    ,
#             # [0.8 , 0.1 , 6.92820323027551 , 2 , 1.73205080756888 , 2],
#             [0.8 , 0.1 , 4.89897948556636 , 2.0 , 1.22474487139159 , 2.0 ],
#             # [0.8 , 0.1 , 4.00000000000000 , 2 , 1.00000000000000 , 2]    ,
#
#
# ]


# params = [
#     [0.8 , 0.1 , 6.92820323027551 , 2 , 1.73205080756888 , 2],
#     [0.8, 0.1, 4.89897948556636, 2, 1.22474487139159, 2],
#     [0.8 , 0.1 , 4.00000000000000 , 2 , 1.00000000000000 , 2]
# ]

# params = [
#     [0.8 , 0.1 , 8.36660026534076 , 2.5 , 2.09165006633519 , 2.5],
#     [0.8 , 0.1 , 5.91607978309962 , 2.5 , 1.47901994577490 , 2.5],
#     [0.8 , 0.1 , 4.83045891539648 , 2.5 , 1.20761472884912 , 2.5]
# ]
#
# params = [
#     [0.8 , 0.1 , 9.79795897113272 , 3 , 2.44948974278318 , 3],
#     [0.8 , 0.1 , 6.92820323027551 , 3 , 1.73205080756888 , 3],
#     [0.8 , 0.1 , 5.65685424949238 , 3 , 1.41421356237309 , 3]
# ]


# params = [
#     # [0.8, 0.1, 6.92820323027551, 2, 1.73205080756888, 2],
#     [0.8, 0.1, 4.89897948556636, 2, 1.22474487139159, 2],
#     # [0.8, 0.1, 4.00000000000000, 2, 1.00000000000000, 2]
#     # [0.8, 0.1, 8.36660026534076, 2.5, 2.09165006633519, 2.5],
#     [0.8, 0.1, 5.91607978309962, 2.5, 1.47901994577490, 2.5],
#     # [0.8, 0.1, 4.83045891539648, 2.5, 1.20761472884912, 2.5]
#     # [0.8, 0.1, 9.79795897113272, 3, 2.44948974278318, 3],
#     [0.8, 0.1, 6.92820323027551, 3, 1.73205080756888, 3],
#     # [0.8, 0.1, 5.65685424949238, 3, 1.41421356237309, 3]
#           ]

# params = [
#     [0.8 , 0.1 , 2.66666666666667 , 2 , 4.00000000000000 , 2],
#     [0.8 , 0.1 , 2.26787888807066 , 2 , 1.94642422238587 , 2],
#     [0.8 , 0.1 , 2.04349882769577 , 2 , 1.41357319932449 , 2]
#           ]
#
# params = [
#     [0.8 , 0.1 , 3.25834261322606 , 2.5 , 4.39332590941915 , 2.5],
#     [0.8 , 0.1 , 2.77502783967818 , 2.5 , 2.26538033235720 , 2.5],
#     [ 0.8 , 0.1 , 2.50000000000000 , 2.5 , 1.66666666666667 , 2.5]
#           ]
#
# params = [
#     [0.8 , 0.1 , 3.84857895818228 , 3 , 4.85410196624968 , 3  ],
#     [0.8 , 0.1 , 3.28020100629408 , 3 , 2.58997487421324 , 3 ],
#     [0.8 , 0.1 , 2.95453501482385 , 3 , 1.92116460960662 , 3 ]
#           ]

# params = [
#     # [0.8, 0.1, 2.66666666666667, 2, 4.00000000000000, 2],
#     [0.8, 0.1, 2.26787888807066, 2, 1.94642422238587, 2],
#     # [0.8, 0.1, 2.04349882769577, 2, 1.41357319932449, 2]
#     # [0.8, 0.1, 3.25834261322606, 2.5, 4.39332590941915, 2.5],
#     [0.8, 0.1, 2.77502783967818, 2.5, 2.26538033235720, 2.5],
#     # [0.8, 0.1, 2.50000000000000, 2.5, 1.66666666666667, 2.5]
#     #
#     # [0.8 , 0.1 , 3.84857895818228 , 3 , 4.85410196624968 , 3  ],
#     [0.8 , 0.1 , 3.28020100629408 , 3 , 2.58997487421324 , 3 ],
#     # [0.8 , 0.1 , 2.95453501482385 , 3 , 1.92116460960662 , 3 ]
#           ]



# fix m v change p
# 0.75
# params = [
#             [0.75 , 0.1 , 6.00000000000000 , 2 , 2.00000000000000 , 2],
#             [0.75 , 0.1 , 4.24264068711928 , 2 , 1.41421356237310 , 2],
#             [0.75 , 0.1 , 3.46410161513775 , 2 , 1.15470053837925 , 2]    ,
#             [0.75 , 0.1 , 2.53589838486225 , 2 , 5.46410161513775 , 2],
#             [0.75 , 0.1 , 2.12549213361246 , 2 , 2.43050087404306 , 2],
#             [0.75 , 0.1 , 1.89974874213240 , 2 , 1.72664991614216 , 2],
#           ]

# 0.8
# params = [
#             [0.8 , 0.1 , 6.92820323027551 , 2 , 1.73205080756888 , 2 ],
#             [0.8 , 0.1 , 4.89897948556636 , 2 , 1.22474487139159 , 2],
#             [0.8 , 0.1 , 4.00000000000000 , 2 , 1.00000000000000 , 2 ]    ,
#             [0.8 , 0.1 , 2.66666666666667 , 2 , 4.00000000000000 , 2 ],
#             [0.8 , 0.1 , 2.26787888807066 , 2 , 1.94642422238587 , 2 ],
#             [0.8 , 0.1 , 2.04349882769577 , 2 , 1.41357319932449 , 2 ],
#           ]
#
# params = [
#             [0.75 , 0.1 , 2.53589838486225 , 2 , 5.46410161513775 , 2],
#             # [0.75 , 0.1 , 2.12549213361246 , 2 , 2.43050087404306 , 2],
#             [0.8 , 0.1 , 2.66666666666667 , 2 , 4.00000000000000 , 2 ],
#             # [0.8 , 0.1 , 2.26787888807066 , 2 , 1.94642422238587 , 2 ],
#           ]
# fix m v change alpha
# 3
# params = [
#             [0.5 , 0.1 , 3 , 1.67944947177034 , 3 , 1.67944947177034],
#             [0.5 , 0.1 , 3 , 2.54138126514911 , 3 , 2.54138126514911],
#             [0.5 , 0.1 , 3 , 3.20809924354783 , 3 , 3.20809924354783]    ,
#             [0.5 , 0.1 , 3 , 3.17944947177034 , 3 , 0.179449471770337],
#             [0.5 , 0.1 , 3 , 4.04138126514911 , 3 , 1.04138126514911],
#             [0.5 , 0.1 , 3 , 4.70809924354783 , 3 , 1.70809924354783],
#           ]

# 4
# params = [
#             [0.5 , 0.1 , 4 , 2.37228132326901 , 4 , 2.37228132326901],
#             [0.5 , 0.1 , 4 , 3.53112887414928 , 4 , 3.53112887414928],
#             [0.5 , 0.1 , 4 , 4.42442890089805 , 4 , 4.42442890089805]    ,
#             [0.5 , 0.1 , 4 , 4.37228132326901 , 4 , 0.372281323269014],
#             [0.5 , 0.1 , 4 , 5.53112887414927 , 4 , 1.53112887414927],
#             [0.5 , 0.1 , 4 , 6.42442890089805 , 4 , 2.42442890089805],
# #           ]
# params = [
#                 [0.5 , 0.1 , 3 , 3.17944947177034 , 3 , 0.179449471770337],
#                 [0.5 , 0.1 , 3 , 4.04138126514911 , 3 , 1.04138126514911],
#                 [0.5 , 0.1 , 4 , 4.37228132326901 , 4 , 0.372281323269014],
#             # [0.5 , 0.1 , 4 , 5.53112887414927 , 4 , 1.53112887414927],
#           ]



#
# params = [
#             [0.4 , 1 , 10 ,1 , 5 , 1],
#
#           ]

"--------------------"

# exp
# params = [0.5 , 0.1 , 1.41421356237310 , 1 , 1.41421356237310 , 1]
#
# #
# params = [
#
#             [0.5 , 0.1 , 1.20000000000000 , 0.8 , 1.20000000000000 , 0.8] ,
#             [0.5 , 0.1 , 1.41421356237310 , 1 , 1.41421356237310 , 1] ,
#             [0.5 , 0.1 , 2.44948974278318 , 2 , 2.44948974278318 , 2] ,
#             [0.5 , 0.1 , 5.47722557505166 , 5 , 5.47722557505166 , 5] ,
#             [0.5 , 0.1 , 10.4880884796639 , 10 , 10.4880884796639 , 10] ,
#           ]

# params = [
#             [0.5, 0.1, 1.29034879005639, 0.9, 1.43372087784044, 1],
#             [0.5, 0.1, 1.41421356237310, 1, 1.41421356237310, 1],
#             [0.5, 0.1, 2.64575131106459, 2, 1.32287565553230, 1],
#             [0.5 , 0.1 , 5.09901951359278 , 4 , 1.27475487839820 , 1] ,
#             [0.5 , 0.1 , 7.54983443527075 , 6 , 1.25830573921179 , 1] ,
#             [0.5 , 0.1 , 10.0000000000000 , 8 , 1.25000000000000 , 1] ,
#           ]
#
# params = [
#             [0.5, 0.1, 1.43372087784044, 1, 1.29034879005639, 0.9],
#             [0.5, 0.1, 1.41421356237310, 1, 1.41421356237310, 1],
#             [0.5, 0.1, 1.32287565553230, 1, 2.64575131106459, 2],
#             [0.5 , 0.1, 1.27475487839820 , 1 , 5.09901951359278 , 4 ] ,
#             [0.5 , 0.1  , 1.25830573921179 , 1, 7.54983443527075 , 6] ,
#             [0.5 , 0.1  , 1.25000000000000 , 1, 10.0000000000000 , 8] ,
#           ]
"----------------"
#
"------ distributions -------"
# print("-----------------------------------------------")
# for i in range(len(params)):
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4],  params[i][5], params[i][0],
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     print(prob,",=",g_beta_1,",=", g_beta_2, "&", mean, "&", var, "&", Skewness, "&", Kurtosis)
#     # print(prob,",=",g_alpha_1,",=", g_alpha_2, "&", mean, "&", var, "&", Skewness, "&", Kurtosis)

#
# # mean, var, Skewness, Kurtosis = 0,0,0,0
# for i in range(len(params)):
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4],  params[i][5], params[i][0]
#     x_array = np.linspace(-10, 10, num=10000)
#     double_gamma_distribution = double_gamma(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # double_gamma_distribution_1.parameters_of_double_g()
#     f_of_xs_double_g = double_gamma_distribution.f_double_g(x_array)
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print(prob,",=",g_beta_1,",=", g_beta_2, "&", mean, "&", var, "&", Skewness, "&", Kurtosis)
#     print(",=", g_beta_1, ",=", g_beta_2, ",=", g_alpha_1, ",=", g_alpha_2, "&", mean, "&", var, "&", Skewness, "&", Kurtosis)
#     # print(prob, ",=", g_alpha_1, ",=", g_alpha_2, "&", mean, "&", var, "&", Skewness, "&", Kurtosis)
#
#     # plt.plot(x_array, f_of_xs_double_g, label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 3)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     #
#     # plt.plot(x_array, f_of_xs_double_g, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     #
#     # plt.plot(x_array, f_of_xs_double_g, label=f' \u03B8$_{1}$ = \u03B8$_{2}$ = {round(params[i][3],2)}', c=color_array[i])
#     # plt.plot(x_array, f_of_xs_double_g, label=f' \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}',c=color_array[i])
#     # plt.plot(x_array, f_of_xs_double_g,  label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = {round(params[i][3],2)},  \u03B8$_{2}$ = {round(params[i][5],2)} ', c=color_array[i])
#     plt.plot(x_array, f_of_xs_double_g, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#     # plt.plot(x_array, f_of_xs_double_g, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ', c=color_array[i])
#     # plt.plot(x_array, f_of_xs_double_g, label=f'p = {round(params[i][0], 2)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ',c=color_array[i])
#     # plt.plot(x_array, f_of_xs_double_g,label=f'\u03B8$_{1}$ = {round(params[i][3], 2)},  \u03B8$_{2}$ = {round(params[i][5], 2)} ',c=color_array[i])
#
#     # rho = {round(params[i][2],2)}
#     # plt.plot(x_array, f_of_xs_double_g, label=f'\u03C1$_{1}$ = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     # sk = {round(Skewness,3)}, K = {round(Kurtosis,3)}
# plt.rc('font', size= 25)
# plt.axvline(0, color='black', linewidth=1)
# plt.axhline(0, color='black', linewidth=1)
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('x', fontsize=25)
# plt.ylabel('p(x)', fontsize=25)
# # plt.title(f'DE: m = {title[0]}, var = {title[1]}, beta = {params[0][2]}')
# plt.legend()
# plt.legend(loc ="upper right")
# # plt.legend(loc ="upper left")
# plt.ylim(0, 4)
# plt.xlim(-10, 10)
# plt.show()
#

"------ call prices ----------"
# for i in range(len(params)):#
#     print("DG call_______________________________________")
#     # call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "call", -2, 14, 0.01, 0.01, K_array, S_array, params[i])
#     call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "call", -2, 14, 0.01, 0.05, K_array, S_array, params[i])
#     # print(call_gamma.params)
#     call_gamma_prices_spot90 = call_gamma.evaluate_integral_one_S0(90)
#     call_gamma_prices_spot100 = call_gamma.evaluate_integral_one_S0(100)
#     call_gamma_prices_spot110 = call_gamma.evaluate_integral_one_S0(110)
#
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#     print("&", np.round(call_gamma_prices_spot90,5), "&", np.round(call_gamma_prices_spot100,5), "&", np.round(call_gamma_prices_spot110,5))
#

#
#
# for i in range(len(params)):#
#     print("DG call_______________________________________")
#     call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "call", -2, 14, 0.01, 0.01, K_array, S_array, params[i])
#     # call_gamma_prices_spot = call_gamma.evaluate_integral_many_S0()
#     # call_gamma_prices_spot90 = call_gamma.evaluate_integral_one_S0(90)
#     call_gamma_prices_spot100 = call_gamma.evaluate_integral_one_S0(100)
#     # call_gamma_prices_spot110 = call_gamma.evaluate_integral_one_S0(110)
#     # print("&", np.round(call_gamma_prices_spot90,4), "&", np.round(call_gamma_prices_spot100,4), "&", np.round(call_gamma_prices_spot110,4))
#     print(np.round(call_gamma_prices_spot100,4))

#
#
#
# # 1
call_arrays = []
for i in trange(len(params)):#
    call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "call", -2, 14, 0.05, 0.05, K_array, S_array, params[i])
    call_gamma_prices_spot = call_gamma.evaluate_integral_many_S0()
    # call_gamma_prices_spot2 = call_gamma.evaluate_integral_one_strike()
    # print(call_gamma_prices_spot2, 1)
    call_arrays.append(call_gamma_prices_spot)
    print(call_gamma_prices_spot)
    plt.plot(S_array, call_gamma_prices_spot, label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
    # alpha_2 = {round(params[i][4], 3)}


    g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
    mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
    # print("test")
    # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
    # plt.plot(S_array, call_gamma_prices_spot, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
    # plt.plot(S_array, call_gamma_prices_spot,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
    # plt.plot(S_array, call_gamma_prices_spot,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])

    # plt.plot(S_array, call_gamma_prices_spot, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
    # plt.plot(S_array, call_gamma_prices_spot, label=f'beta_1 = {round(params[i][2], 3)}, beta_2 = {round(params[i][4], 3)}, p = {params[i][0]}')

plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('$S_0$', fontsize=25)
plt.ylabel('call value', fontsize=25)
# plt.title(f'Effect of change in alpha on Call value: mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# plt.title(f'DE Call value fixing mean and variance')
# mean = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]},  beta1 =  beta2 = {params[0][2]}
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
plt.rc('font', size= 22)
plt.legend()
plt.legend(loc ="upper left")
plt.show()

# # # dictionary of lists
# # dict_call = {'S': S_array,
# #              'p01': call_arrays[0],
# #              'p02': call_arrays[1],
# #              'p03': call_arrays[2],
# #              'p04': call_arrays[3],
# #              'p05': call_arrays[1],
# #              'p06': call_arrays[5],
# #              'p07': call_arrays[6],
# #              'p08': call_arrays[7],
# #              'p09': call_arrays[8],
# #
# # }
# # df_call = pd.DataFrame(dict_call)
# # print(df_call)
# # # df_call.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_call_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # df_call.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_call_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # # df_call.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/5/DG_call_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # df_call.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_call_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #
#
#
# "---------"
# # call_gamma1 = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "call", -2, 12, 0.75, 2.5, K_array, S_array, [])
# # call_gamma_prices_spot1 = call_gamma1.evaluate_integral_many_S0()
# # print(call_gamma1.evaluate_integral_one_strike())
# # plt.plot(S_array, call_gamma_prices_spot1)
# # plt.show()
# #
# # call_gamma1 = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "call", -2, 12, 0.01, 0.5, K_array, S_array, [])
# # call_gamma_prices_spot1 = call_gamma1.evaluate_integral_many_S0()
# # print(call_gamma1.evaluate_integral_one_strike())
# # plt.plot(S_array, call_gamma_prices_spot1)
# # plt.show()
# #
# # call_gamma2 = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "put", -2, 12, 0.75, 2.5, K_array, S_array, [])
# # print(call_gamma2.evaluate_integral_one_strike())
# # call_gamma_prices_spot2 = call_gamma2.evaluate_integral_many_S0()
# # plt.plot(S_array, call_gamma_prices_spot2)
# # plt.show()
# #
# # call_gamma2 = CfOptionPricing(S, K, r, q, T, sigma, 'GBM', "put", -2, 12, 0.01, 0.5, K_array, S_array, [])
# # print(call_gamma2.evaluate_integral_one_strike())
# # call_gamma_prices_spot2 = call_gamma2.evaluate_integral_many_S0()
# # plt.plot(S_array, call_gamma_prices_spot2)
# # plt.show()
# #
# # call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "put", -2, 12, 0.75, 2.5, K_array, S_array, params[4])
# # call_gamma_prices_spot = call_gamma.evaluate_integral_many_S0()
# # print(call_gamma.evaluate_integral_one_strike())
# # plt.plot(S_array, call_gamma_prices_spot)
# # plt.show()
# #
# # call_gamma = CfOptionPricing(S, K, r, q, T, sigma, 'Merton_Double_gamma', "put", -2, 12, 0.01, 0.5, K_array, S_array, params[4])
# # call_gamma_prices_spot = call_gamma.evaluate_integral_many_S0()
# # print(call_gamma.evaluate_integral_one_strike())
# # plt.plot(S_array, call_gamma_prices_spot)
# # plt.show()
#
"----------- delta ----------------"
# print("----------- delta ----------------")
# for i in range(len(params)):#
#
#     greeks_delta1 = delta_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8, method='central')
#     greeks_delta2 = delta_fdm_Double_gamma(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8,method='central')
#     greeks_delta3 = delta_fdm_Double_gamma(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8,method='central')
#     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))
#
# # #
# # # #
# delta_arrays = []
# for i in trange(len(params)):
#     greeks_delta_array = []
#     for S in tqdm(S_array):
#         greeks_delta = delta_fdm_Double_gamma(S, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-8,method='central')
#         greeks_delta_array.append(greeks_delta)
#     # print(greeks_c_array)
#     delta_arrays.append(greeks_delta_array)
#     # plt.plot(S_array, greeks_delta_array, label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#
#     # plt.plot(S_array, greeks_delta_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     plt.plot( S_array, greeks_delta_array  , label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#     # plt.plot(S_array, greeks_delta_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array, label=f'\u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)}, \u03B8$_{1}$ = {round(params[i][3],2)}, \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#     # plt.plot(S_array, greeks_delta_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array,label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array, greeks_delta_array,label=f'\u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c=color_array[i])
#
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('$S_0$', fontsize=25)
# plt.ylabel('delta', fontsize=25)
# # plt.title(f' mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# # plt.title(f'DE Delta value fixing mean and variance')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
# plt.rc('font', size= 20)
# plt.legend()
# plt.legend(loc ="upper left")
# # plt.legend(loc ="lower right")
# plt.show()
# #
# # # # dictionary of lists
# # # dict_delta = {'S': S_array,
# # #              'p01': delta_arrays[0],
# # #              'p02': delta_arrays[1],
# # #              'p03': delta_arrays[2],
# # #              'p04': delta_arrays[3],
# # #              'p05': delta_arrays[4],
# # #              'p06': delta_arrays[5],
# # #              'p07': delta_arrays[6],
# # #              'p08': delta_arrays[7],
# # #              'p09': delta_arrays[8],
# # #
# # # }
# # # df_delta = pd.DataFrame(dict_delta)
# # # print(df_delta)
# # # # df_delta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_delta_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # # df_delta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_delta_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # # df_delta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_delta_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #
# "----------- gamma ----------------"
# # print("----------- gamma ----------------")
# # for i in range(len(params)):#
# #
# #     greeks_delta1 = gamma_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
# #     greeks_delta2 = gamma_fdm_Double_gamma(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
# #     greeks_delta3 = gamma_fdm_Double_gamma(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2,method='central')
# #     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))
# # #
# gamma_arrays = []
# for i in trange(len(params)):
#     greeks_gamma_array = []
#     for S in tqdm(S_array):
#         greeks_gamma = gamma_fdm_Double_gamma(S, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", ds=1e-2, method='forward')
#         greeks_gamma_array.append(greeks_gamma)
#     gamma_arrays.append(greeks_gamma_array)
#     # plt.plot(S_array, greeks_gamma_array, label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#
#     # plt.plot(S_array, greeks_gamma_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array,  greeks_gamma_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     plt.plot(S_array,  greeks_gamma_array   , label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#
#
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#     # plt.plot(S_array, greeks_gamma_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
#     # plt.plot(S_array,  greeks_gamma_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#     # plt.plot(S_array, greeks_gamma_array, label=f'\u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#     # plt.plot(S_array, greeks_gamma_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
#     # plt.plot(S_array, greeks_gamma_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
#     # plt.plot(S_array,  greeks_gamma_array,label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c =color_array[i])
#     # plt.plot(S_array,  greeks_gamma_array,label=f'\u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('$S_0$', fontsize=25)
# plt.ylabel('gamma', fontsize=25)
# # plt.title(f' mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# # plt.title(f'DE Gamma value fixing mean and variance')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
# plt.rc('font', size= 20)
# plt.legend()
# plt.legend(loc ="upper right")
# plt.show()
# # #
# # # # dictionary of lists
# # # dict_gamma = {'S': S_array,
# # #              'p01': gamma_arrays[0],
# # #              'p02': gamma_arrays[1],
# # #              'p03': gamma_arrays[2],
# # #              'p04': gamma_arrays[3],
# # #              'p05': gamma_arrays[4],
# # #              'p06': gamma_arrays[5],
# # #              'p07': gamma_arrays[6],
# # #              'p08': gamma_arrays[7],
# # #              'p09': gamma_arrays[8],
# # # }
# # # df_gamma = pd.DataFrame(dict_gamma)
# # # print(df_gamma)
# # # # df_gamma.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_gamma_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # # df_gamma.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_gamma_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # # df_gamma.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_gamma_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #
# "---------------- Vega -----------------"
# # print("----------- Vega ----------------")
# # for i in range(len(params)):#
# #
# #     greeks_delta1 = vega_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
# #     greeks_delta2 = vega_fdm_Double_gamma(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
# #     greeks_delta3 = vega_fdm_Double_gamma(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
# #     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))
# #
# Vega_arrays = []
# for i in trange(len(params)):
#     greeks_Vega_array = []
#     for S in tqdm(S_array):
#         greeks_Vega = vega_fdm_Double_gamma(S, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dv=1e-4, method='central')
#         greeks_Vega_array.append(greeks_Vega)
#     Vega_arrays.append(greeks_Vega_array)
#     # plt.plot(S_array, greeks_Vega_array, label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#
#     # plt.plot(S_array, greeks_Vega_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array, greeks_Vega_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     plt.plot( S_array, greeks_Vega_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#
#
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#     # plt.plot(S_array, greeks_Vega_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
#     # plt.plot(S_array,  greeks_Vega_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#     # plt.plot(S_array, greeks_Vega_array, label=f'\u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#     # plt.plot(S_array, greeks_Vega_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
#     # plt.plot(S_array,  greeks_Vega_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
#     # plt.plot( S_array, greeks_Vega_array, label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c =color_array[i])
#     # plt.plot(S_array, greeks_Vega_array, label=f'\u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}',c=color_array[i])
#
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('$S_0$', fontsize=25)
# plt.ylabel('Vega', fontsize=25)
# # plt.title(f' mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# # plt.title(f'DE Vega value fixing mean and variance')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
# plt.rc('font', size=20)
# plt.legend()
# # plt.legend(loc ="upper right")
# plt.legend(loc ="upper left")
# plt.show()
# # #
# # # # dictionary of lists
# # # dict_Vega = {'S': S_array,
# # #              'p01': Vega_arrays[0],
# # #              'p02': Vega_arrays[1],
# # #              'p03': Vega_arrays[2],
# # #              'p04': Vega_arrays[3],
# # #              'p05': Vega_arrays[4],
# # #              'p06': Vega_arrays[5],
# # #              'p07': Vega_arrays[6],
# # #              'p08': Vega_arrays[7],
# # #              'p09': Vega_arrays[8],
# # #
# # # }
# # # df_Vega = pd.DataFrame(dict_Vega)
# # # print(df_Vega)
# # # # df_Vega.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_Vega_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # # df_Vega.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_Vega_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # # df_Vega.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_Vega_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #
# #
# "---------------- theta ----------------"
# # print("----------- theta ----------------")
# # for i in range(len(params)):#
# #
# #     greeks_delta1 = theta_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-2, method='forward')
# #     greeks_delta2 = theta_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-8, method='forward')
# #     greeks_delta3 = theta_fdm_Double_gamma(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-8, method='forward')
# #     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))
# #
# theta_arrays = []
# for i in trange(len(params)):
#     greeks_theta_array = []
#     for S in tqdm(S_array):
#         greeks_theta = theta_fdm_Double_gamma(S, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", 1e-2, method='central')
#         greeks_theta_array.append(greeks_theta)
#     theta_arrays.append(greeks_theta_array)
#     # plt.plot(S_array, greeks_theta_array, label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#
#     # plt.plot(S_array, greeks_theta_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array, greeks_theta_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     plt.plot(S_array, greeks_theta_array   , label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#
#
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#     # plt.plot(S_array, greeks_theta_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
#     # plt.plot(S_array,  greeks_theta_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#     # plt.plot(S_array, greeks_theta_array, label=f'\u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#     # plt.plot(S_array, greeks_theta_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
#     # plt.plot(S_array, greeks_theta_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
#     # plt.plot(S_array,greeks_theta_array, label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c =color_array[i])
#     # plt.plot(S_array,greeks_theta_array, label=f'\u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
#
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('$S_0$', fontsize=25)
# plt.ylabel('theta', fontsize=25)
# # plt.title(f' mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# # plt.title(f'DE Theta value fixing mean and variance')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
# plt.rc('font', size= 20)
# plt.legend()
# plt.legend(loc ="lower left")
# plt.show()
# # #
# # # # dictionary of lists
# # # dict_theta = {'S': S_array,
# # #              'p01': theta_arrays[0],
# # #              'p02': theta_arrays[1],
# # #              'p03': theta_arrays[2],
# # #              'p04': theta_arrays[3],
# # #              'p05': theta_arrays[4],
# # #              'p06': theta_arrays[5],
# # #              'p07': theta_arrays[6],
# # #              'p08': theta_arrays[7],
# # #              'p09': theta_arrays[8],
# # #
# # # }
# # # df_theta = pd.DataFrame(dict_theta)
# # # print(df_theta)
# # # # df_theta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_theta_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # # df_theta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_theta_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # # df_theta.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_theta_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #
# "---------------- rho ----------------"
# # print("----------- rho ----------------")
# # for i in range(len(params)):#
# #     greeks_delta1 = rho_fdm_Double_gamma(90, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
# #     greeks_delta2 = rho_fdm_Double_gamma(100, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
# #     greeks_delta3 = rho_fdm_Double_gamma(110, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5, method='central')
# #     print("&", np.round(greeks_delta1,4), "&", np.round(greeks_delta2,4), "&", np.round(greeks_delta3,4))
# #
# rho_arrays = []
# for i in trange(len(params)):
#     greeks_rho_array = []
#     for S in tqdm(S_array):
#         greeks_rho = rho_fdm_Double_gamma(S, K, T, q, r, sigma, K_array, S_array, -2, params[i], "call", dr=1e-5,method='central')
#         greeks_rho_array.append(greeks_rho)
#     rho_arrays.append(greeks_rho_array)
#     # plt.plot(S_array, greeks_rho_array, label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3],2)}, p = {params[i][0]}', c=color_array[i])
#     g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
#     mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
#     # print("test")
#
#     # plt.plot(S_array,greeks_rho_array, label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, \u03B8$_{1}$ = {round(params[i][3], 2)}, \u03B8$_{2}$ = {round(params[i][5], 2)}, p = {params[i][0]}', c=color_array[i])
#     # plt.plot(S_array,greeks_rho_array,  label=f'\u03C1$_{1}$  = {round(params[i][2], 3)}, \u03C1$_{2}$ = {round(params[i][4], 3)}, p = {params[i][0]}', c=color_array[i])
#     plt.plot(S_array,greeks_rho_array,   label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#
#
#     # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
#     # plt.plot(S_array, greeks_rho_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
#
#     # plt.plot(S_array, greeks_rho_array, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = = {params[i][3]}', c=color_array[i])
#     # plt.plot(S_array, greeks_rho_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
#     # plt.plot(S_array,  greeks_rho_array,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)} ', c=color_array[i])
#
#     # plt.plot( S_array,greeks_rho_array, label=f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}, p = {params[i][0]}', c = color_array[i])
#     # plt.plot(S_array,greeks_rho_array, label=f'\u03C1$_{1}$ = {round(params[i][2], 2)},  \u03C1$_{2}$ = {round(params[i][4], 2)}, \u03B8$_{1}$ = \u03B8$_{2}$ ={round(params[i][3],2)}', c =color_array[i])
# #
#
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.xlabel('$S_0$', fontsize=25)
# plt.ylabel('rho', fontsize=25)
# # plt.title(f' mean = 0.0, var = 0.5, poi_lamda = 1,  alpha1 =  alpha2 = {params[0][3]} ')
# # plt.title(f'DE Rho value fixing mean and variance')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="strike")
# plt.rc('font', size= 20)
# plt.legend()
# plt.legend(loc ="upper left")
# # plt.legend(loc ="lower right")
# plt.show()
# #
# # # dictionary of lists
# # dict_rho = {'S': S_array,
# #              'p01': rho_arrays[0],
# #              'p02': rho_arrays[1],
# #              'p03': rho_arrays[2],
# #              'p04': rho_arrays[3],
# #              'p05': rho_arrays[4],
# #              'p06': rho_arrays[5],
# #              'p07': rho_arrays[6],
# #              'p08': rho_arrays[7],
# #              'p09': rho_arrays[8],
# #
# # }
# # df_rho = pd.DataFrame(dict_rho)
# # print(df_rho)
# # # df_rho.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_rho_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# # # df_rho.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_1/1_5/DG_rho_m_{title[0]}_v_{title[1]}_l_005_1.csv', index=False)
# # df_rho.to_csv(f'/Users/huzuwang/我的雲端硬碟/code/實驗室code/python/CFOptionPricing2/data/DG/m_0_v_15/2/DG_rho_m_{title[0]}_v_{title[1]}_l_01_1.csv', index=False)
# #

"---------------- hedging1 ----------------"
print('S$_\u0394 t $')
print('S_{\u0394 t }')
print("DG")
print("=+=+"*30)
print("DG")
for i in range(len(params)):
    # #
    # # # #
    # print(i)
    # print("delta")
    # hedging_results = []
    # hedging_d = gamma_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, params[i], -100, "call")
    # hedging_d.delta_hedging()
    # hedging_d.check()
    # hedging_d.param_output()
    # hedging_results1 = hedging_d.hedging_results(90)
    # hedging_results2 = hedging_d.hedging_results(110)
    # print(np.round(hedging_results1,4), "&",np.round( hedging_results2,4))
    # print("+++++++"*20)
    # hedging_results3 = hedging_d.hedging_results(x_array2)
    # # plt.plot(x_array2, hedging_results3,label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3], 2)}, p = {params[i][0]}', c=color_array[i])
    #
    # g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
    # mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
    # # print("test")
    # # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
    # # plt.plot(x_array2, hedging_results3,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
    #
    # # plt.plot(x_array2, hedging_results3, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)} ', c=color_array[i])
    # # plt.plot(x_array2, hedging_results3, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
    # # plt.plot(x_array2, hedging_results3, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = \u03C1$_{2}$ = {params[i][3]}', c=color_array[i])
    # # plt.plot(x_array2, hedging_results3, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
    # # plt.plot(x_array2, hedging_results3, label = f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)},  \u03B8$_{1}$ = \u03B8$_{2}$ = {round(params[i][3], 2)}, p = {params[i][0]}', c =color_array[i])
    # plt.plot(x_array2, hedging_results3, label = f'\u03C1$_{1}$ = {round(params[i][2], 2)}, \u03C1$_{2}$ = {round(params[i][4], 2)}, p = {params[i][0]}', c =color_array[i])


    print('====='*20)
    print("deltaa_gamma")
    hedging_d_g = gamma_hedging_strats(S, K, T, q, r, sigma, K_array, S_array, params[i], -100, "call")
    hedging_d_g.delta_gamma_hedging()
    hedging_d_g.check()
    hedging_d_g.param_output()
    hedging_results11 = hedging_d_g.hedging_results(90)
    hedging_results12 = hedging_d_g.hedging_results(110)
    print(np.round(hedging_results11,4), "&",np.round( hedging_results12,4))
    print("+++++++"*20)
    hedging_results13 = hedging_d_g.hedging_results(x_array2)
    # plt.plot(x_array2, hedging_results13,label=f'alpha_1 = {round(params[i][2], 3)}, alpha_2 = {round(params[i][4], 3)}, beta = {round(params[i][3], 2)}, p = {params[i][0]}', c=color_array[i])
    g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = params[i][2], params[i][3], params[i][4], params[i][5], params[i][0]
    mean, var, Skewness, Kurtosis = DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
    # print("test")
    # print(abs(np.round(mean, 1)), np.round(var, 1), np.round(Skewness, 3), np.round(Kurtosis, 3))
    # plt.plot(x_array2, hedging_results13,label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}', c=color_array[i])
    # plt.plot(x_array2, hedging_results3, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = \u03C1$_{2}$ = {params[i][3]}', c=color_array[i])
    # plt.plot(x_array2, hedging_results13, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, p = {round(params[i][0], 2)} ',c=color_array[i])
    # plt.plot(x_array2, hedging_results13, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)} ', c=color_array[i])
    # plt.plot(x_array2, hedging_results13, label=f'mean = {abs(np.round(mean, 1))}, variance = {np.round(var, 1)}, \u03B8$_{1}$ = \u03B8$_{2}$ = {params[i][3]}', c=color_array[i])
    plt.plot(x_array2, hedging_results13, label = f'\u03C1$_{1}$ = {round(params[i][2], 2)}, \u03C1$_{2}$ = {round(params[i][4], 2)}, p = {params[i][0]}', c =color_array[i])

    # plt.plot(x_array2, hedging_results13, label = f'\u03C1$_{1}$ = \u03C1$_{2}$ = {round(params[i][2], 2)},  \u03B8$_{1}$ = \u03B8$_{2}$ = {round(params[i][3], 2)}, p = {params[i][0]}', c =color_array[i])
    #
    # # 1
    # # # plt.xlabel('$S_0$')
    # # # plt.ylabel('hedging value')
    # # # plt.legend()
    # # # plt.title(f'Double_exp delta gamma hedging:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
    # # # plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
    # # # plt.show()

plt.xlabel('S$_{t+ \u03B4 t}$', fontsize=30)
plt.ylabel(r'$\Delta \Pi$', fontsize=30)
plt.legend()
plt.rc('font', size= 20)
# plt.legend(loc ="lower center")
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

# plt.rc('font', size= 20)
# plt.legend(loc ="upper right")
# plt.legend(loc ="lower center")
plt.legend(loc ="lower left")
# plt.legend(loc ="lower right")
# plt.title(f'Double_exp delta hedging:  m = {title[0]}, var = {title[1]}, poi_lamda = {params[0][1]}')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.show()



# hedging_results_error2_2 = hedging_d_g.exp_hedging_results(90, 110, [-99.7561 , 100, -99.9847])
# hedging_results_error2_3 = hedging_d_g.exp_hedging_results(90, 110, [-90.2603 , 100, -100.14877])
# hedging_results_error2_4 = hedging_d_g.exp_hedging_results(90, 110, [-94.7314 , 100, -99.6502])
# hedging_results_error2_5 = hedging_d_g.exp_hedging_results(90, 110, [-99.7783 , 100, -99.9455])
# hedging_results_error2_6 = hedging_d_g.exp_hedging_results(90, 110, [-85.1787 , 100, -99.7021])
#
#
#










