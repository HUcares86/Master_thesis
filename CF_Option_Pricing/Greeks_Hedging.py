from Greeks_mjdg import *
from Greeks_mjde import *
from BS import *
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# K_array = np.arange(1, 250, 1)
# S_array = np.arange(1, 250, 1)
#
#
# S = 100
# K = 100
# T = 0.25
# q = 0.01
# r = 0.05  #0.04  0.05  , 0.065
# sigma = 0.3
# params = [0.5, 0.1, 1.5, 1.08113883008419, 1.5, 1.08113883008419]


class gamma_hedging_strats():
    def __init__(self, S, K, T, q, r, sigma, K_array, S_array, params, buy_num, buy_type):
        # input params
        self.S = S
        self.K = K
        self.T = T
        self.q = q
        self.r = r
        self.sigma = sigma
        self.K_array = K_array
        self.S_array = S_array
        self.params = params
        self.buy_num = buy_num
        self.buy_type =  buy_type

        # hedge params
        self.call_value = CfOptionPricing(self.S, K, r, q, T, sigma, 'Merton_Double_gamma', "call",  -2, 14, 0.01, 0.05, K_array,S_array, params).evaluate_integral_one_strike()
        self.call_delta = delta_fdm_Double_gamma(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "call", ds=1e-8, method='central')
        self.call_gamma = gamma_fdm_Double_gamma(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "call", ds=1e-2, method='central')
        self.put_value = CfOptionPricing(self.S, K, r, q, T, sigma, 'Merton_Double_gamma', "put", -2, 14, 0.01, 1.5, K_array,S_array, params).evaluate_integral_one_strike()
        self.put_delta = delta_fdm_Double_gamma(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "put", ds=1e-8,method='central')
        self.put_gamma = gamma_fdm_Double_gamma(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "put", ds=1e-2, method='central')
        self.call_position = 0
        self.put_position = 0
        self.stock_position = 0
        self.total_spent = 0

    def delta_hedging(self):
        if self.buy_type == "call":
            self.call_position = self.buy_num
            self.stock_position = -self.buy_num * self.call_delta
            self.total_spent = self.stock_position * self.S + self.call_value * self.buy_num
            # print("call_value: ", self.call_value)
            # print("call_delta: ", self.call_delta)
            # print("call position: ", self.buy_num)
            # print("call spending's: ", self.call_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

        if self.buy_type == "put":
            self.put_position = self.buy_num
            self.stock_position = -self.buy_num * self.put_delta
            self.total_spent = self.stock_position*self.S + self.put_value*self.buy_num
            # print("put value: ", self.put_value)
            # print("put delta: ", self.put_delta)
            # print("put position: ", self.buy_num)
            # print("put spending's: ", self.put_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

    def delta_gamma_hedging(self):
        if self.buy_type == "call":
            # first delta neutral
            self.call_position = self.buy_num
            stock_num_1 = -self.buy_num*self.call_delta
            # gamma neutral
            self.put_position = -self.buy_num*self.call_gamma/self.put_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.put_position * self.put_delta)
            self.stock_position = stock_num_1 + stock_num_2
            self.total_spent = self.stock_position*self.S + self.call_value*self.call_position + self.put_value*self.put_position

        if self.buy_type == "put":
            # first delta neutral
            self.put_position = self.buy_num
            stock_num_1 = -self.buy_num * self.put_delta
            # gamma neutral
            self.call_position = -self.buy_num*self.put_gamma/self.call_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.call_position * self.call_delta)
            self.stock_position = stock_num_1 + stock_num_2

            self.total_spent = self.stock_position * self.S + self.call_value * self.call_position + self.put_value * self.put_position

    def check(self):
        print("delta: ", self.call_delta*self.call_position + self.put_delta*self.put_position + self.stock_position)
        print("gamma: ", self.call_gamma*self.call_position + self.put_gamma*self.put_position)
        print("-------" * 20)

    def param_output(self):
        # print("stock_position: ", self.stock_position)
        # print("call_value: ", self.call_value)
        # print("call_position: ", self.call_position)
        # print("call_delta: ", self.call_delta)
        # print("call_gamma: ", self.call_gamma)
        # print("put_value: ", self.put_value)
        # print("put_position: ", self.put_position)
        # print("put_delta: ", self.put_delta)
        # print("put_gamma: ", self.put_gamma)
        # print("total_spent: ", self.total_spent)
        # print("-------"*20)
        # print("&",np.round(self.stock_position,4),"&",np.round(self.call_delta,4),"&",np.round(self.call_gamma, 4),"&",np.round(self.call_position,4),
        #       "&",np.round(self.put_delta,4),"&",np.round(self.put_gamma,4),"&",np.round(self.put_position,4))
        #
        # print("&", np.round(self.stock_position, 4), "&", np.round(self.call_delta, 4), "&",np.round(self.call_position, 4))
        print("&", np.round(self.stock_position, 4),  "&",np.round(self.call_position, 4), "&")
        print("&",np.round(self.stock_position,4),"&",np.round(self.call_position,4),"&",np.round(self.put_position,4), "&")


    def hedging_results(self, S2):
        call_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "call",  -2, 14, 0.01, 0.05, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        put_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "put", -2, 14, 0.01, 1.5, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        results = (S2 - self.S)*self.stock_position + (put_value2 - self.put_value)*self.put_position + (call_value2 - self.call_value)*self.call_position
        # print((S2 - self.S)*self.stock_position)
        # print((put_value2 - self.put_value)*self.put_position)
        # print((call_value2 - self.call_value)*self.call_position)
        # print("call",self.call_value ,call_value2, self.call_position)
        # print("put",self.put_value, put_value2, self.put_position)
        # print(np.round(results,4))
        print(self.call_value, self.call_delta, self.call_gamma, self.put_value, self.put_delta,  self.put_gamma,  abs(self.call_delta)+abs(self.put_delta))
        return results

    def exp_hedging_results(self, S2, S3, pos1):
        call_value1 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "call", -2, 14, 0.01, 0.01, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        put_value1 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "put", -2, 14, 0.75, 2.5, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        results1 = (S2 - self.S)*self.stock_position + (put_value1 - self.put_value)*self.put_position + (call_value1 - self.call_value)*self.call_position

        exp_stock_pos1 = pos1[0]
        exp_call_pos1 = pos1[1]
        exp_put_pos1 = pos1[2]

        results1_2 = (S2 - self.S)*exp_stock_pos1 + (put_value1 - self.put_value)*exp_put_pos1 + (call_value1 - self.call_value)*exp_call_pos1
        error1 = results1 - results1_2
        print(exp_stock_pos1, exp_call_pos1, exp_put_pos1)
        print(self.stock_position,  self.call_position,self.put_position )

        "------------------------------------------------------------------------------------------------------------------------------------------------"
        call_value2 = CfOptionPricing(S3, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "call", -2, 14, 0.01, 0.05, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        put_value2 = CfOptionPricing(S3, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_gamma', "put", -2, 14, 0.75, 2.5, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        results2 = (S3 - self.S)*self.stock_position + (put_value2 - self.put_value)*self.put_position + (call_value2 - self.call_value)*self.call_position

        # exp_stock_pos = pos1[0]
        # exp_call_pos = pos1[1]
        # exp_put_pos = pos1[2]

        results2_2 = (S3 - self.S)*exp_stock_pos1 + (put_value2 - self.put_value)*exp_put_pos1+ (call_value2 - self.call_value)*exp_call_pos1
        error2 = results2 - results2_2
        # print(call_value2)
        # print(put_value2)
        print(exp_stock_pos1, exp_call_pos1, exp_put_pos1)
        print(self.stock_position,  self.call_position,self.put_position )
        print("&", np.round(results1, 4), "&", np.round(results2, 4), "&", np.round(results1_2, 4), "&", np.round(results2_2, 4),"&", np.round(error1, 4), "&", np.round(error2, 4))
        # return results


#
class exp_hedging_strats():
    def __init__(self, S, K, T, q, r, sigma, K_array, S_array, params, buy_num, buy_type):
        # input params
        self.S = S
        self.K = K
        self.T = T
        self.q = q
        self.r = r
        self.sigma = sigma
        self.K_array = K_array
        self.S_array = S_array
        self.params = params
        self.buy_num = buy_num
        self.buy_type =  buy_type

        # hedge params
        self.call_value = CfOptionPricing(self.S, K, r, q, T, sigma, 'Merton_Double_exp', "call", -2,  14, 0.01, 0.01, K_array,S_array, params).evaluate_integral_one_strike()
        self.call_delta = delta_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "call", ds=1e-8, method='central')
        self.call_gamma = gamma_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "call", ds=1e-2, method='central')
        # self.call_theta = theta_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "call", dt=1e-8,method='forward')

        self.put_value = CfOptionPricing(self.S, K, r, q, T, sigma, 'Merton_Double_exp', "put", -2, 14, 0.01, 1.5, K_array,S_array, params).evaluate_integral_one_strike()
        self.put_delta = delta_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "put", ds=1e-5,method='central')
        self.put_gamma = gamma_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "put", ds=1e-2, method='central')
        # self.put_theta = theta_fdm_Double_exp(self.S, K, T, q, r, sigma, K_array, S_array, -2, params, "put", dt=1e-8,method='forward')

        self.call_position = 0
        self.put_position = 0
        self.stock_position = 0
        self.total_spent = 0

    def delta_hedging(self):
        if self.buy_type == "call":
            self.call_position = self.buy_num
            self.stock_position = -self.buy_num * self.call_delta
            self.total_spent = self.stock_position * self.S + self.call_value * self.buy_num
            # print("call_value: ", self.call_value)
            # print("call_delta: ", self.call_delta)
            # print("call position: ", self.buy_num)
            # print("call spending's: ", self.call_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

        if self.buy_type == "put":
            self.put_position = self.buy_num
            self.stock_position = -self.buy_num * self.put_delta
            self.total_spent = self.stock_position*self.S + self.put_value*self.buy_num
            # print("put value: ", self.put_value)
            # print("put delta: ", self.put_delta)
            # print("put position: ", self.buy_num)
            # print("put spending's: ", self.put_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

    def delta_gamma_hedging(self):
        if self.buy_type == "call":
            # first delta neutral
            self.call_position = self.buy_num
            stock_num_1 = -self.buy_num*self.call_delta
            # gamma neutral
            self.put_position = -self.buy_num*self.call_gamma/self.put_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.put_position * self.put_delta)
            self.stock_position = stock_num_1 + stock_num_2
            self.total_spent = self.stock_position*self.S + self.call_value*self.call_position + self.put_value*self.put_position

        if self.buy_type == "put":
            # first delta neutral
            self.put_position = self.buy_num
            stock_num_1 = -self.buy_num * self.put_delta
            # gamma neutral
            self.call_position = -self.buy_num*self.put_gamma/self.call_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.call_position * self.call_delta)
            self.stock_position = stock_num_1 + stock_num_2

            self.total_spent = self.stock_position * self.S + self.call_value * self.call_position + self.put_value * self.put_position

    def check(self):
        print("delta: ", self.call_delta*self.call_position + self.put_delta*self.put_position + self.stock_position)
        print("gamma: ", self.call_gamma*self.call_position + self.put_gamma*self.put_position)
        print("-------" * 20)

    def param_output(self):
        # print("stock_position: ", self.stock_position)
        # print("call_value: ", self.call_value)
        # print("call_position: ", self.call_position)
        # print("call_delta: ", self.call_delta)
        # print("call_gamma: ", self.call_gamma)
        # print("put_value: ", self.put_value)
        # print("put_position: ", self.put_position)
        # print("put_delta: ", self.put_delta)
        # print("put_gamma: ", self.put_gamma)
        # print("total_spent: ", self.total_spent)
        # print("-------"*20)

        # print("&",np.round(self.stock_position,4),"&",np.round(self.call_delta,4),"&",np.round(self.call_gamma, 4),"&",np.round(self.call_position,4),
        #       "&",np.round(self.put_delta,4),"&",np.round(self.put_gamma,4),"&",np.round(self.put_position,4))

        # print("&",np.round(self.stock_position,4),"&",np.round(self.call_delta,4),"&",np.round(self.call_position,4))
        print("&", np.round(self.stock_position, 4),  "&",np.round(self.call_position, 4), "&")
        print("&",np.round(self.stock_position,4),"&",np.round(self.call_position,4),"&",np.round(self.put_position,4), "&")


    def hedging_results(self, S2):
        call_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_exp', "call",  -2, 14, 0.01, 0.05, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        put_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, 'Merton_Double_exp', "put", -2, 14, 0.01, 1.5, self.K_array,self.S_array, self.params).evaluate_integral_one_strike()
        results = (S2 - self.S)*self.stock_position + (put_value2 - self.put_value)*self.put_position + (call_value2 - self.call_value)*self.call_position
        # theory_results = (self.call_theta + self.put_theta)*
        # print(call_value2)
        # print(put_value2)
        # print(np.round(results,4))
        return results

class gbm_hedging_strats():
    def __init__(self, S, K, T, q, r, sigma, K_array, S_array, params, buy_num, buy_type):
        # input params
        self.S = S
        self.K = K
        self.T = T
        self.q = q
        self.r = r
        self.sigma = sigma
        self.K_array = K_array
        self.S_array = S_array
        self.params = params
        self.buy_num = buy_num
        self.buy_type =  buy_type

        # hedge params
        self.call_value = CfOptionPricing(self.S, K, r, q, T, sigma, "GBM", "call", -2, 12, 0.01, 0.5, K_array,S_array, params).evaluate_integral_one_strike()
        self.call_delta = delta_call(S, K, T, q, r, sigma)
        self.call_gamma = gamma(S, K, T, q, r, sigma)
        self.put_value = CfOptionPricing(self.S, K, r, q, T, sigma, "GBM", "put", -2, 12, 0.75, 2.5, K_array,S_array, params).evaluate_integral_one_strike()
        self.put_delta = delta_put(S, K, T, q, r, sigma)
        self.put_gamma = gamma(S, K, T, q, r, sigma)
        self.call_position = 0
        self.put_position = 0
        self.stock_position = 0
        self.total_spent = 0

    def delta_hedging(self):
        if self.buy_type == "call":
            self.call_position = self.buy_num
            self.stock_position = -self.buy_num * self.call_delta
            self.total_spent = self.stock_position * self.S + self.call_value * self.buy_num
            # print("call_value: ", self.call_value)
            # print("call_delta: ", self.call_delta)
            # print("call position: ", self.buy_num)
            # print("call spending's: ", self.call_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

        if self.buy_type == "put":
            self.put_position = self.buy_num
            self.stock_position = -self.buy_num * self.put_delta
            self.total_spent = self.stock_position*self.S + self.put_value*self.buy_num
            # print("put value: ", self.put_value)
            # print("put delta: ", self.put_delta)
            # print("put position: ", self.buy_num)
            # print("put spending's: ", self.put_value*self.buy_num)
            # print("stock position: ", self.stock_position)
            # print("stock spending's:", self.stock_position*S)
            # print("total spending's:", self.total_spent)

    def delta_gamma_hedging(self):
        if self.buy_type == "call":
            # first delta neutral
            self.call_position = self.buy_num
            stock_num_1 = -self.buy_num*self.call_delta
            # gamma neutral
            self.put_position = -self.buy_num*self.call_gamma/self.put_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.put_position * self.put_delta)
            self.stock_position = stock_num_1 + stock_num_2
            self.total_spent = self.stock_position*self.S + self.call_value*self.call_position + self.put_value*self.put_position

        if self.buy_type == "put":
            # first delta neutral
            self.put_position = self.buy_num
            stock_num_1 = -self.buy_num * self.put_delta
            # gamma neutral
            self.call_position = -self.buy_num*self.put_gamma/self.call_gamma
            # 2nd delta neutral
            stock_num_2 = -(self.call_position * self.call_delta)
            self.stock_position = stock_num_1 + stock_num_2

            self.total_spent = self.stock_position * self.S + self.call_value * self.call_position + self.put_value * self.put_position

    def check(self):
        print("delta: ", self.call_delta*self.call_position + self.put_delta*self.put_position + self.stock_position)
        print("gamma: ", self.call_gamma*self.call_position + self.put_gamma*self.put_position)
        print("-------" * 20)

    def param_output(self):
        print("stock_position: ", self.stock_position)
        print("call_value: ", self.call_value)
        print("call_position: ", self.call_position)
        print("call_delta: ", self.call_delta)
        print("call_gamma: ", self.call_gamma)
        print("put_value: ", self.put_value)
        print("put_position: ", self.put_position)
        print("put_delta: ", self.put_delta)
        print("put_gamma: ", self.put_gamma)
        print("total_spent: ", self.total_spent)
        print("-------"*20)
        print("&",np.round(self.stock_position,4),"&",np.round(self.call_delta,4),"&",np.round(self.call_gamma, 4),"&",np.round(self.call_position,4),
              "&",np.round(self.put_delta,4),"&",np.round(self.put_gamma,4),"&",np.round(self.put_position,4))

        print("&", np.round(self.stock_position, 4), "&", np.round(self.call_delta, 4), "&",np.round(self.call_position, 4))

    def hedging_results(self, S2):
        call_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, "GBM", "call", -2, 12, 0.01, 0.5, self.K_array,self.S_array, []).evaluate_integral_one_strike()
        put_value2 = CfOptionPricing(S2, self.K, self.r, self.q, self.T, self.sigma, "GBM", "put", -2, 12, 0.75, 2.5, self.K_array,self.S_array, []).evaluate_integral_one_strike()
        results = (S2 - self.S)*self.stock_position + (put_value2 - self.put_value)*self.put_position + (call_value2 - self.call_value)*self.call_position
        print(call_value2)
        print(put_value2)
        print(np.round(results,4))
        return np.round(results,4)






