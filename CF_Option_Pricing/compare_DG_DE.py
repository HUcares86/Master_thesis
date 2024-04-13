from Greeks_mjdg import *
from Greeks_mjde import *
from tqdm import trange, tqdm

S = 100
K = 100
T = 1
q = 0.05
r = 0.01
sigma = 0.3

K_array = np.arange(1, 250, 1)
S_array = np.arange(1, 250, 1)
S_array_2 = np.arange(1, 1000, 1)
" -------- call 1 -----------------------------------------------------------------------------------------"
# exp alpha = 2 , 1/alpha  ;  gamma alpha = 1, beta = 2 , alpha/beta
call_exp = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_exp', 0, 12, 0.25, 5, K_array, S_array)
# call_gamma_1 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 33, 12, 0.25, 5, K_array, S_array)   # gamma alpha = 1, beta = 2 , alpha/beta
# call_gamma_2 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 30, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1.5, beta = 3 , alpha/beta
# call_gamma_3 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 31, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 2, beta = 4 , alpha/beta
# call_gamma_4 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 32, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 2.5, beta = 5 , alpha/beta
# call_gamma_5 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 33, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 2, beta = 4 , alpha/beta
# call_gamma_6 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 34, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1, beta = 1.1 , alpha/beta
# call_gamma_7 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 35, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1, beta = 1.5 , alpha/beta
# call_gamma_8 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 36, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1, beta = 2 , alpha/beta
# call_gamma_9 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 37, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 0, beta = 2 , alpha/beta
call_gamma_10 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 38, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 0.5, beta = 2 , alpha/beta
call_gamma_11 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 39, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1, beta = 2 , alpha/beta
call_gamma_12 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 40, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 1.5, beta = 2 , alpha/beta
call_gamma_13 = CfOptionPricing(100, 100, 0.05, 0.01, 1, 0.3, 'Merton_Double_gamma', 41, 12, 0.25, 5, K_array, S_array)  # gamma alpha = 2, beta = 2 , alpha/beta


#  def __init__(self, S0, K, r, q, T, sigma, model, num, n, eta, alpha, K_array, S_array):

# call_gamma_prices_strike = call_gamma.evaluate_integral_many_strikes()
# call_exp_prices_strike = call_exp.evaluate_integral_many_strikes()
# plt.plot(call_gamma_prices_strike, label='Merton_Double_gamma')
# plt.plot(call_exp_prices_strike, label='Merton_Double_exp ')
# plt.title('Strike Price Effect on call price')
# plt.xlabel('K')
# plt.ylabel('Call prices')
# plt.legend()
# plt.show()


# call_gamma_prices_spot_1 = call_gamma_1.evaluate_integral_many_S0()
# call_gamma_prices_spot_2 = call_gamma_2.evaluate_integral_many_S0()
# call_gamma_prices_spot_3 = call_gamma_3.evaluate_integral_many_S0()
# call_gamma_prices_spot_4 = call_gamma_4.evaluate_integral_many_S0()
# call_gamma_prices_spot_6 = call_gamma_6.evaluate_integral_many_S0()
# call_gamma_prices_spot_7 = call_gamma_7.evaluate_integral_many_S0()
# call_gamma_prices_spot_8 = call_gamma_8.evaluate_integral_many_S0()
# call_gamma_prices_spot_9 = call_gamma_9.evaluate_integral_many_S0()
call_gamma_prices_spot_10 = call_gamma_10.evaluate_integral_many_S0()
call_gamma_prices_spot_11 = call_gamma_11.evaluate_integral_many_S0()
call_gamma_prices_spot_12 = call_gamma_12.evaluate_integral_many_S0()
call_gamma_prices_spot_13 = call_gamma_13.evaluate_integral_many_S0()


# plt.plot(call_gamma_prices_spot_1, label='Double_gamma alpha = 0.55, beta = 1.1 ')
# plt.plot(call_gamma_prices_spot_2, label='Double_gamma alpha = 1.5, beta = 3')
# plt.plot(call_gamma_prices_spot_3, label='Double_gamma alpha = 2, beta = 4')
# plt.plot(call_gamma_prices_spot_4, label='Double_gamma alpha = 2.5, beta = 5')

# plt.plot(call_gamma_prices_spot_6, label='Double_gamma alpha = 0, beta = 2 ')
# plt.plot(call_gamma_prices_spot_7, label='Double_gamma alpha = 0.5, beta = 2 ')
# plt.plot(call_gamma_prices_spot_8, label='Double_gamma alpha = 1, beta = 2 ')
# plt.plot(call_gamma_prices_spot_7, label='Double_gamma alpha = 1.5, beta = 2 ')
# plt.plot(call_gamma_prices_spot_8, label='Double_gamma alpha = 2, beta = 2 ')
# plt.plot(call_gamma_prices_spot_9, label='Double_gamma alpha = 0, beta = 2 ')
plt.plot(call_gamma_prices_spot_10, label='Double_gamma alpha = 0.5, beta = 2 ')
plt.plot(call_gamma_prices_spot_11, label='Double_gamma alpha = 1, beta = 2 ')
plt.plot(call_gamma_prices_spot_12, label='Double_gamma alpha = 1.5, beta = 2 ')
plt.plot(call_gamma_prices_spot_13, label='Double_gamma alpha = 2, beta = 2 ')

call_exp_prices_spot = call_exp.evaluate_integral_many_S0()
plt.plot(call_exp_prices_spot, label='Double_exp alpha = 2')
plt.title('Double_gamma beta = 2')
plt.xlabel('S')
plt.ylabel('Call prices')
plt.legend()
plt.show()



"delta"
for num in trange(1, 6):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
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
plt.ylabel('delta')
plt.title('Effect of change in alpha on delta for Calls: prob = 0.5, poi_lamda = 1')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(6, 11):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
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
plt.ylabel('delta')
plt.title('Effect of change in alpha_1 on delta for Calls: prob = 0.5, poi_lamda = 1, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(11, 16):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
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
plt.ylabel('delta')
plt.title('Effect of change in poi_lamda on delta for Calls: prob = 0.5, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

for num in trange(16, 21):
    greeks_c_array = []
    for S in tqdm(S_array):
        greeks_c = delta_fdm_call_Double_exp(S, K, T, q, r, sigma, K_array, S_array, num, ds=1e-8, method='central')
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
plt.ylabel('delta')
plt.title('Effect of change in prob on delta for Calls: poi_lamda = 1, alpha_1 = 1.5, alpha_2 = 1.5')
plt.axvline(K, color='black', linestyle='dashed', linewidth=2, label="Strike")
plt.legend()
plt.show()

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
