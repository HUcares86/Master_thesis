import numpy as np
import pandas as pd
import os
from scipy.optimize import minimize
from scipy.stats import norm
import math
from Config import *

config = Config()
PARAM_NUM = config.PARAM_NUM
class IVParamOptim:
    def __init__(self, paramMat, tArray, kArray, targetVolMat, calendar=True, butterfly=True):
        self.paramMat = paramMat
        self.tArray = tArray
        self.kArray = kArray
        self.logKArray = np.log(kArray)
        self.targetVolMat = targetVolMat
        self.calendar = calendar
        self.butterfly = butterfly


    def svi_vol(self, k, params):
        a, b, tilde_rho, m, tilde_sigma = params
        return a + b * (tilde_rho * (k - m) + ((k - m) ** 2 + tilde_sigma ** 2) ** 0.5)

    def objective_function(self, params, k, target_vols):
        # Calculate the fitted option prices using the SVI model
        fitted_vols = self.svi_vol(k, params)
        # fitted_prices = black_scholes(S0, K, T, R, fitted_vol, Q)
        # Calculate the difference between the fitted and observed option prices
        diff = fitted_vols - target_vols
        # Square the differences and sum across all strikes and expiries
        sum_squared_diff = np.sum(diff ** 2)
        return sum_squared_diff

    def objective_function_slices(self, params, k, target_vol1, target_vol2, t1, t2):
        # t1 < t2
        params_1 = params[:PARAM_NUM]
        params_2 = params[PARAM_NUM:]
        # Calculate the fitted option prices using the SVI model
        fitted_vols_1 = self.svi_vol(k, params_1)
        fitted_vols_2 = self.svi_vol(k, params_2)
        # Calculate the difference between the fitted and observed option prices

        diff_1 = fitted_vols_1 - target_vol1
        diff_2 = fitted_vols_2 - target_vol2
        # Square the differences and sum across all strikes and expiries
        sum_diff_1 = np.sum(diff_1 ** 2)
        sum_diff_2 = np.sum(diff_2 ** 2)

        # calendar
        pen_weight_cale = config.pen_weight_cale
        # pen_weight_cale = params_1[5]
        clan_pen_term = [pen_weight_cale * max(0, (fitted_vols_1 - fitted_vols_2)[i]) for i in range(len(fitted_vols_1))]
        sum_pen_cale = np.sum(clan_pen_term)

        # butterfly
        b_1 = params_1[1]
        rho_1 = params_1[2]
        b_2 = params_2[1]
        rho_2 = params_2[2]
        pen_weight_butt = config.pen_weight_butt
        targetPen_1 =  min(0, b_1 * (1 +abs(rho_1)) - 4 / t1)
        targetPen_2 = min(0, b_2 * (1 + abs(rho_2)) - 4 / t2)

        return sum_diff_1 + sum_diff_2 + sum_pen_cale + pen_weight_butt * (targetPen_1 + targetPen_2)


    def optimizing(self):
        # T is row, K is col
        # first round optim
        for T in range(len(self.tArray)):
            params = self.paramMat[T]
            target_vols = self.targetVolMat[T]
            log_K = self.logKArray
            # optim
            result = minimize(self.objective_function, params, args=(log_K, target_vols))
            newParams = result.x
            self.paramMat[T] = newParams
        # first round fitted parameters
        resultParaMat = np.copy(self.paramMat)

        # plot round1 surface
        result_vol1 = np.copy(self.targetVolMat)
        for T in range(self.paramMat.shape[0]):
            params = self.paramMat[T]
            log_K = self.logKArray
            sviVol = self.svi_vol(log_K, params)
            result_vol1[T] = sviVol

        # second round optim
        for T in range(len(self.tArray)):
            log_K = self.logKArray
            params_1 = self.paramMat[T]
            target_vols_1 = self.targetVolMat[T]
            t1 = self.tArray[T]
            if T < len(self.tArray) - 1:
                params_2 = self.paramMat[T + 1]
                target_vols_2 = self.targetVolMat[T + 1]
                t2 = self.tArray[T + 1]
            else:
                params_2 = self.paramMat[T - 1]
                target_vols_2 = self.targetVolMat[T - 1]
                t2 = self.tArray[T - 1]
            params = np.concatenate((params_1, params_2))
            result = minimize(self.objective_function_slices, params, args=(log_K, target_vols_1, target_vols_2, t1, t2))
            newParams_1 = result.x[:PARAM_NUM]
            newParams_2 = result.x[PARAM_NUM:]
            self.paramMat[T] = newParams_1
            if T < len(self.tArray) - 1:
                self.paramMat[T + 1] = newParams_2
            else:
                self.paramMat[T - 1] = newParams_2

        # plot round2 surface
        result_vol2 = np.copy(self.targetVolMat)
        for T in range(self.paramMat.shape[0]):
            params = self.paramMat[T]
            log_K = self.logKArray
            sviVol = self.svi_vol(log_K, params)
            result_vol2[T] = sviVol

        return result_vol1, result_vol2, resultParaMat, self.paramMat

    def toCsv(self, paraMat, csvName):
        # Convert the Numpy array to a pandas DataFrame and specify the row index
        colName = ["a", "b", "rho", "m", "sig"]
        time = [round(t, 4) for t in self.tArray]
        df = pd.DataFrame(paraMat, index=time, columns=colName)
        df.index.name = 'Time'
        # Write the DataFrame to a CSV file
        df.to_csv(os.path.join("output/", csvName))

# # Define the initial guess of the SVI parameters
# params = [0.1, 0.1, 0.1, 0.1, 0.1]
#
# # Define the option strikes and expiries
# s = [100, 101, 102, 103, 104, 105]
# k1 = [95, 96, 97, 98, 99, 100]
# k2 = [105, 106, 107, 108, 109, 110]
#
# # Define the observed mid option prices for each strike and expiry
# prices1 = [0.2, 0.2, 0.1732, 0.1544, 0.1446, 0.1375]
# prices2 = [0.1585, 0.1537, 0.1487, 0.1437, 0.1386, 0.1334]
#
# # time
# params2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
#
#
# # Minimize the objective function
# result1 = minimize(objective_function, params, args=(np.log(k1), prices1))
# # result2 = minimize(objective_function, params, args=(s, k2, prices2))
# output = result1.x
#
# result3 = minimize(objective_function_slices, params2, args=(np.log(k1), prices1, prices2))