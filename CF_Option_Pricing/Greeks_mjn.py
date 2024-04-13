# Delta	Option price	Value of underlying asset
# Gamma	Delta	Value of underlying asset
# Vega	Option price	Volatility
# Theta	Option price	Time to maturity
# Rho	Option price	Interest rate

from CF_option_pricing import *



"------ delta ------------------------------------------------------"


def delta_fdm_Normal(S, K, T, q, r, sigma, K_array, S_array, num, params, option_type, ds=1e-8, method='central'):
    # finite difference method
    method = method.lower()
    call_plus = CfOptionPricing(S + ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call = CfOptionPricing(S, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_minus = CfOptionPricing(S - ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    if method == 'central':
        return (call_plus.evaluate_integral_one_strike() -
                call_minus.evaluate_integral_one_strike()) / (2 * ds)
    elif method == 'forward':
        return (call_plus.evaluate_integral_one_strike() -
                call.evaluate_integral_one_strike()) / ds
    elif method == 'backward':
        return (call.evaluate_integral_one_strike() -
                call_minus.evaluate_integral_one_strike()) / ds


"------------- gamma ------------------------------------------------------"


def gamma_fdm_Normal(S, K, T, q, r, sigma, K_array, S_array, num, params, option_type, ds=1e-5, method='central'):
    call_2_plus = CfOptionPricing(S + 2*ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_plus = CfOptionPricing(S + ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call = CfOptionPricing(S, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_minus = CfOptionPricing(S - ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_2_minus = CfOptionPricing(S - 2*ds, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    method = method.lower()
    if method =='central':
        return (call_plus.evaluate_integral_one_strike() - 2 * call.evaluate_integral_one_strike() +
                call_minus.evaluate_integral_one_strike()) / ds ** 2
    elif method == 'forward':
        return (call_2_plus.evaluate_integral_one_strike() - 2*call_plus.evaluate_integral_one_strike() +
                call.evaluate_integral_one_strike()) / ds ** 2
    elif method == 'backward':
        return (call.evaluate_integral_one_strike() - 2*call_minus.evaluate_integral_one_strike() +
                call_2_minus.evaluate_integral_one_strike()) / ds ** 2


"------- Vega --------------------------------------------------------------------------------------------"


def vega_fdm_Normal(S, K, T, q, r, sigma, K_array, S_array, num, params, option_type, dv=1e-4, method='central'):
    call_plus = CfOptionPricing(S, K, r, q, T, sigma+dv, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call = CfOptionPricing(S, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_minus = CfOptionPricing(S, K, r, q, T, sigma-dv, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    method = method.lower()
    if method == 'central':
        return (call_plus.evaluate_integral_one_strike() - call.evaluate_integral_one_strike())/(2*dv)
    elif method == 'forward':
        return (call_plus.evaluate_integral_one_strike() - call.evaluate_integral_one_strike())/dv
    elif method == 'backward':
        return (call.evaluate_integral_one_strike() - call_minus.evaluate_integral_one_strike())/dv


"------ theta ---------------------------------------------------------------------------------------------"


def theta_fdm_Normal(S, K, T, q, r, sigma, K_array, S_array, num, params, option_type, dt, method='central'):
    call_plus = CfOptionPricing(S, K, r, q, T+dt, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call = CfOptionPricing(S, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_minus = CfOptionPricing(S, K, r, q, T-dt, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)

    if method == 'central':
        return -(call_plus.evaluate_integral_one_strike() - call_minus.evaluate_integral_one_strike()) / (2 * dt)
    elif method == 'forward':
        return -(call_plus.evaluate_integral_one_strike() - call.evaluate_integral_one_strike()) / dt
    elif method == 'backward':
        return -(call.evaluate_integral_one_strike() - call_minus.evaluate_integral_one_strike()) / dt


"------ rho ---------------------------------------------------------------------------------------------"


def rho_fdm_Normal(S, K, T, q, r, sigma, K_array, S_array, num, params, option_type, dr=1e-5, method='central'):
    call_plus = CfOptionPricing(S, K, r+dr, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call = CfOptionPricing(S, K, r, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)
    call_minus = CfOptionPricing(S, K, r-dr, q, T, sigma, "Merton_Double_exp", option_type, num, 12, 0.25, 5, K_array, S_array, params)

    method = method.lower()
    if method == 'central':
        return (call_plus.evaluate_integral_one_strike() - call_minus.evaluate_integral_one_strike()) / (2 * dr)
    elif method == 'forward':
        return (call_plus.evaluate_integral_one_strike() - call.evaluate_integral_one_strike()) / dr
    elif method == 'backward':
        return (call.evaluate_integral_one_strike() - call_minus.evaluate_integral_one_strike()) / dr



