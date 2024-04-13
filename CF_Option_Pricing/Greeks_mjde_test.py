from Greeks_mjde import *
from tqdm import trange, tqdm

" -------- call 1 -----------------------------------------------------------------------------------------"
K_array = np.arange(1, 250, 1)
S_array = np.arange(1, 250, 1)
S_array_2 = np.arange(1, 1000, 1)
# call1 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 1, 12, 0.25, 5, K_array, S_array)
# #  def __init__(self, S0, K, r, q, T, sigma, model, num, n, eta, alpha, K_array, S_array):
#
# # call_prices = call1.evaluate_integral_many_strikes()
# # print(call1.evaluate_integral_one_strike())
# # plt.plot(call_prices, label='Merton_Double_gamma No.1')
# # plt.title('Strike Price Effect on call price')
# # plt.xlabel('K')
# # plt.ylabel('Call prices')
# # plt.legend()
# # plt.show()

S = 100
K = 100
T = 1
q = 0.05
r = 0.01
sigma = 0.3

"delta"
# for num in trange(1, 6):
#     greeks_c_array = []
#     for S in tqdm(S_array):
#         greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
#         greeks_c_array.append(greeks_c)
#     print(greeks_c_array)
#     if num == 1:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.1, alpha_2 = 1.1')
#     elif num == 2:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5, alpha_2 = 1.5')
#     elif num == 3:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2, alpha_2 = 2')
#     elif num == 4:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5, alpha_2 = 2.5')
#     elif num == 5:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3, alpha_2 = 3')
#
# plt.xlabel('$S_0$')
# plt.ylabel('delta')
# plt.title('Effect of change in alpha on delta for Calls: prob = 0.5, poi_lamda = 1')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()
#
# for num in trange(6, 11):
#     greeks_c_array = []
#     for S in tqdm(S_array):
#         greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
#         greeks_c_array.append(greeks_c)
#     print(greeks_c_array)
#     if num == 6:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5')
#     elif num == 7:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2')
#     elif num == 8:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5')
#     elif num == 9:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3')
#     elif num == 10:
#         plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3.5')
#
# plt.xlabel('$S_0$')
# plt.ylabel('delta')
# plt.title('Effect of change in alpha_1 on delta for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()
#
# for num in trange(11, 16):
#     greeks_c_array = []
#     for S in tqdm(S_array):
#         greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
#         greeks_c_array.append(greeks_c)
#     print(greeks_c_array)
#     if num == 11:
#         plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0')
#     elif num == 12:
#         plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0.5')
#     elif num == 13:
#         plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1')
#     elif num == 14:
#         plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1.5')
#     elif num == 15:
#         plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 2')
#
# plt.xlabel('$S_0$')
# plt.ylabel('delta')
# plt.title('Effect of change in poi_lamda on delta for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

# for num in trange(16, 21):
#     greeks_c_array = []
#     for S in tqdm(S_array):
#         greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
#         greeks_c_array.append(greeks_c)
#     print(greeks_c_array)
#     if num == 16:
#         plt.plot(S_array, greeks_c_array, label=f'prob = 0.0')
#     elif num == 17:
#         plt.plot(S_array, greeks_c_array, label=f'prob = 0.25')
#     elif num == 18:
#         plt.plot(S_array, greeks_c_array, label=f'prob = 0.5')
#     elif num == 19:
#         plt.plot(S_array, greeks_c_array, label=f'prob = 0.75')
#     elif num == 20:
#         plt.plot(S_array, greeks_c_array, label=f'prob = 1')
#
# plt.xlabel('$S_0$')
# plt.ylabel('delta')
# plt.title('Effect of change in prob on delta for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
# plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
# plt.legend()
# plt.show()

for num in trange(21, 26):
    greeks_c_array = []
    for S in tqdm(S_array_2):
        greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array_2, num, ds=1e-8, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 21:
        plt.plot(S_array_2, greeks_c_array, label=f'alpha_2 = 1.5')
    elif num == 22:
        plt.plot(S_array_2, greeks_c_array, label=f'alpha_2 = 2')
    elif num == 23:
        plt.plot(S_array_2, greeks_c_array, label=f'alpha_2 = 2.5')
    elif num == 24:
        plt.plot(S_array_2, greeks_c_array, label=f'alpha_2 = 3')
    elif num == 25:
        plt.plot(S_array_2, greeks_c_array, label=f'alpha_2 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('delta')
plt.title('Effect of change in alpha_2 on delta for Calls: prob = 0.5, poi_lamda = 1, alpha_1 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()


" ----- gamma -----------------------------"
for num in trange(1, 6):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-3, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 1:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.1, alpha_2 = 1.1')
    elif num == 2:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5, alpha_2 = 1.5')
    elif num == 3:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2, alpha_2 = 2')
    elif num == 4:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5, alpha_2 = 2.5')
    elif num == 5:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3, alpha_2 = 3')

plt.xlabel('$S_0$')
plt.ylabel('Gamma')
plt.title('Effect of change in alpha on Gamma for Calls: prob = 0.5, poi_lamda = 1')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(6, 11):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-3, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 6:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5')
    elif num == 7:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2')
    elif num == 8:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5')
    elif num == 9:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3')
    elif num == 10:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('Gamma')
plt.title('Effect of change in alpha_1 on Gamma for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(11, 16):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-3, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 11:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0')
    elif num == 12:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0.5')
    elif num == 13:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1')
    elif num == 14:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1.5')
    elif num == 15:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 2')

plt.xlabel('$S_0$')
plt.ylabel('Gamma')
plt.title('Effect of change in poi_lamda on Gamma for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(16, 21):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-3, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 16:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.0')
    elif num == 17:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.25')
    elif num == 18:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.5')
    elif num == 19:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.75')
    elif num == 20:
        plt.plot(S_array, greeks_c_array, label=f'prob = 1')

plt.xlabel('$S_0$')
plt.ylabel('Gamma')
plt.title('Effect of change in prob on Gamma for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(21, 26):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = gamma_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-3, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 21:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 1.5')
    elif num == 22:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2')
    elif num == 23:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2.5')
    elif num == 24:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3')
    elif num == 25:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('Gamma')
plt.title('Effect of change in alpha_2 on Gamma for Calls: prob = 0.5, poi_lamda = 1, alpha_1 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

" Vega -"
for num in trange(1, 6):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dv=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 1:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.1, alpha_2 = 1.1')
    elif num == 2:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5, alpha_2 = 1.5')
    elif num == 3:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2, alpha_2 = 2')
    elif num == 4:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5, alpha_2 = 2.5')
    elif num == 5:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3, alpha_2 = 3')

plt.xlabel('$S_0$')
plt.ylabel('Vega')
plt.title('Effect of change in alpha on Vega for Calls: prob = 0.5, poi_lamda = 1')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(6, 11):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dv=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 6:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5')
    elif num == 7:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2')
    elif num == 8:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5')
    elif num == 9:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3')
    elif num == 10:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('Vega')
plt.title('Effect of change in alpha_1 on Vega for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(11, 16):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dv=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 11:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0')
    elif num == 12:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0.5')
    elif num == 13:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1')
    elif num == 14:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1.5')
    elif num == 15:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 2')

plt.xlabel('$S_0$')
plt.ylabel('Vega')
plt.title('Effect of change in poi_lamda on Vega for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(16, 21):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dv=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 16:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.0')
    elif num == 17:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.25')
    elif num == 18:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.5')
    elif num == 19:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.75')
    elif num == 20:
        plt.plot(S_array, greeks_c_array, label=f'prob = 1')

plt.xlabel('$S_0$')
plt.ylabel('Vega')
plt.title('Effect of change in prob on Vega for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(21, 26):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = vega_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dv=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 21:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 1.5')
    elif num == 22:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2')
    elif num == 23:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2.5')
    elif num == 24:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3')
    elif num == 25:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('Vega')
plt.title('Effect of change in alpha_2 on Vega for Calls: prob = 0.5, poi_lamda = 1, alpha_1 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

" theta "
for num in trange(1, 6):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = theta_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dt=1e-10, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 1:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.1, alpha_2 = 1.1')
    elif num == 2:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5, alpha_2 = 1.5')
    elif num == 3:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2, alpha_2 = 2')
    elif num == 4:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5, alpha_2 = 2.5')
    elif num == 5:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3, alpha_2 = 3')

plt.xlabel('$S_0$')
plt.ylabel('theta')
plt.title('Effect of change in alpha on theta for Calls: prob = 0.5, poi_lamda = 1')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(6, 11):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = theta_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dt=1e-10, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 6:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5')
    elif num == 7:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2')
    elif num == 8:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5')
    elif num == 9:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3')
    elif num == 10:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('theta')
plt.title('Effect of change in alpha_1 on theta for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(11, 16):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = theta_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dt=1e-10, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 11:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0')
    elif num == 12:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0.5')
    elif num == 13:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1')
    elif num == 14:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1.5')
    elif num == 15:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 2')

plt.xlabel('$S_0$')
plt.ylabel('theta')
plt.title('Effect of change in poi_lamda on theta for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(16, 21):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = theta_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dt=1e-10, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 16:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.0')
    elif num == 17:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.25')
    elif num == 18:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.5')
    elif num == 19:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.75')
    elif num == 20:
        plt.plot(S_array, greeks_c_array, label=f'prob = 1')

plt.xlabel('$S_0$')
plt.ylabel('theta')
plt.title('Effect of change in prob on theta for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(21, 26):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = theta_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dt=1e-10, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 21:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 1.5')
    elif num == 22:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2')
    elif num == 23:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2.5')
    elif num == 24:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3')
    elif num == 25:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('theta')
plt.title('Effect of change in alpha_2 on theta for Calls: prob = 0.5, poi_lamda = 1, alpha_1 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

"rho "
for num in trange(1, 6):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = rho_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dr=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 1:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.1, alpha_2 = 1.1')
    elif num == 2:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5, alpha_2 = 1.5')
    elif num == 3:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2, alpha_2 = 2')
    elif num == 4:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5, alpha_2 = 2.5')
    elif num == 5:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3, alpha_2 = 3')

plt.xlabel('$S_0$')
plt.ylabel('rho')
plt.title('Effect of change in alpha on rho for Calls: prob = 0.5, poi_lamda = 1')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(6, 11):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = rho_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dr=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 6:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 1.5')
    elif num == 7:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2')
    elif num == 8:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 2.5')
    elif num == 9:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3')
    elif num == 10:
        plt.plot(S_array, greeks_c_array, label=f'alpha_1 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('rho')
plt.title('Effect of change in alpha_1 on rho for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(11, 16):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = rho_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dr=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 11:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0')
    elif num == 12:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 0.5')
    elif num == 13:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1')
    elif num == 14:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 1.5')
    elif num == 15:
        plt.plot(S_array, greeks_c_array, label=f'poi_lamda = 2')

plt.xlabel('$S_0$')
plt.ylabel('rho')
plt.title('Effect of change in poi_lamda on rho for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(16, 21):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = rho_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dr=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 16:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.0')
    elif num == 17:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.25')
    elif num == 18:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.5')
    elif num == 19:
        plt.plot(S_array, greeks_c_array, label=f'prob = 0.75')
    elif num == 20:
        plt.plot(S_array, greeks_c_array, label=f'prob = 1')

plt.xlabel('$S_0$')
plt.ylabel('rho')
plt.title('Effect of change in prob on rho for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(21, 26):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = rho_call_fdm_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, dr=1e-4, method='central')
        greeks_c_array.append(greeks_c)
    print(greeks_c_array)
    if num == 21:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 1.5')
    elif num == 22:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2')
    elif num == 23:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 2.5')
    elif num == 24:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3')
    elif num == 25:
        plt.plot(S_array, greeks_c_array, label=f'alpha_2 = 3.5')

plt.xlabel('$S_0$')
plt.ylabel('rho')
plt.title('Effect of change in alpha_2 on rho for Calls: prob = 0.5, poi_lamda = 1, alpha_1 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()
