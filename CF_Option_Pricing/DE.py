import sympy as sym
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
from Tools import *


class double_exp():
    def __init__(self, exp_alpha_1, exp_alpha_2, prob):
        # jump upward
        self.exp_alpha_1 = exp_alpha_1
        # jump downward
        self.exp_alpha_2 = exp_alpha_2
        self.prob = prob
        # params
        # double_exp
        self.mean = -1
        self.variance = -1
        self.skewness = -1
        self.kurtosis = -1
        self.f_of_xs_double_exp = []
        # exp_plus
        self.plus_Mean = -1
        self.plus_Variance = -1
        self.plus_Skewness = -1
        self.plus_Kurtosis = -1
        self.f_of_xs_exp_plus = []
        # exp_minus
        self.minus_Mean = -1
        self.minus_Variance = -1
        self.minus_Skewness = -1
        self.minus_Kurtosis = -1
        self.f_of_xs_exp_minus = []

    def f_exp_plus(self, x):
        f_of_x = self.exp_alpha_1*math.exp(-x*self.exp_alpha_1)
        return f_of_x

    def f_exp_plus_array(self, x_array):
        self.f_of_xs_exp_plus = []
        for x in x_array:
            f_of_x = self.exp_alpha_1*math.exp(-x*self.exp_alpha_1)
            self.f_of_xs_exp_plus.append(f_of_x)

        self.plus_Mean = n_th_moment(x_array, self.f_of_xs_exp_plus, 0, 1)
        self.plus_Variance = n_th_moment(x_array, self.f_of_xs_exp_plus, self.plus_Mean, 2)
        self.plus_Skewness = n_th_moment(x_array, self.f_of_xs_exp_plus, self.plus_Mean, 3)
        self.plus_Kurtosis = n_th_moment(x_array, self.f_of_xs_exp_plus, self.plus_Mean, 4)

        return self.f_of_xs_exp_plus

    def f_exp_minus(self, x):
        f_of_x = self.exp_alpha_2*math.exp(x*self.exp_alpha_2)
        return f_of_x

    def f_exp_minus_array(self, x_array):
        self.f_of_xs_exp_minus = []
        for x in x_array:
            f_of_x = self.exp_alpha_2*math.exp(x*self.exp_alpha_2)
            self.f_of_xs_exp_minus.append(f_of_x)

        self.minus_Mean = n_th_moment(x_array, self.f_of_xs_exp_minus, 0, 1)
        self.minus_Variance = n_th_moment(x_array, self.f_of_xs_exp_minus, self.minus_Mean, 2)
        self.minus_Skewness = n_th_moment(x_array, self.f_of_xs_exp_minus, self.minus_Mean, 3)
        self.minus_Kurtosis = n_th_moment(x_array, self.f_of_xs_exp_minus, self.minus_Mean, 4)
        return self.f_of_xs_exp_minus

    def parameters_of_exp_minus_and_exp_plus(self):
        print("---"*20)
        print("parameters of right exponential distribution")
        print(f'Mean: {self.plus_Mean}')
        print(f'Variance: {self.plus_Variance}')
        print(f'Skewness: {self.plus_Skewness}')
        print(f'Kurtosis: {self.plus_Kurtosis}')
        print("parameters of left exponential distribution")
        print(f'Mean: {self.minus_Mean}')
        print(f'Variance: {self.minus_Variance}')
        print(f'Skewness: {self.minus_Skewness}')
        print(f'Kurtosis: {self.minus_Kurtosis}')

    def f_double_exp(self, x_array):
        self.f_of_xs_double_exp = []
        for x in x_array:
            if x > 0:
                f_of_x = self.prob * (self.f_exp_plus(x))
            else:
                f_of_x = (1 - self.prob) * (self.f_exp_minus(x))
            self.f_of_xs_double_exp.append(f_of_x)

        self.mean = n_th_moment(x_array, self.f_of_xs_double_exp, 0, 1)
        self.variance = n_th_moment(x_array, self.f_of_xs_double_exp, self.mean, 2)
        self.skewness = n_th_moment(x_array, self.f_of_xs_double_exp, self.mean, 3)
        self.kurtosis = n_th_moment(x_array, self.f_of_xs_double_exp, self.mean, 4)

        return self.f_of_xs_double_exp

    def parameters_of_double_exp_numerical(self):
        print("---"*20)
        print("parametrs of double exponential distribution")
        print(f'Mean: {self.mean}')
        print(f'Variance: {self.variance}')
        print(f'Skewness: {self.skewness}')
        print(f'Kurtosis: {self.kurtosis}')

    def double_exp_n_th_moment(self, x_array, n, moment_type):
        double_exp_Mean = n_th_moment(x_array, self.f_of_xs_double_exp, 0, 1)
        double_exp_moment = -1
        if moment_type == 'raw':
            double_exp_moment = n_th_moment(x_array, self.f_of_xs_double_exp, 0, n)
        if moment_type == 'center':
            double_exp_moment = n_th_moment(x_array, self.f_of_xs_double_exp, double_exp_Mean, n)

        print("---" * 20)
        print(f'the {n} th {moment_type} moment of normaldistribution is: {double_exp_moment}')

    def plot_f_exp_plus_and_f_exp_minus(self, x_plus, x_minus):
        plt.plot(x_plus, self.f_of_xs_exp_plus, label='plus')
        plt.plot(x_minus, self.f_of_xs_exp_minus, label='minus')
        plt.axvline(0, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper right')
        plt.show()

    def plot_f_double_exp(self, x_array):
        plt.plot(x_array, self.f_of_xs_double_exp, label='double exponential')
        plt.axvline(0, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('probability')
        plt.title(f'double exponential mean = 0.0, var = 1,  alpha1 = {self.exp_alpha_1},  alpha2 = {self.exp_alpha_2} ')
        plt.legend(loc='upper right')
        plt.show()


def DE_solve_eq(e_alpha_1, e_alpha_2, prob, fix, mean, var):
    if fix == "a1,a2,mu,var":
        e_alpha_1, e_alpha_2 = sym.symbols('e_alpha_1, e_alpha_2')
        eq1 = sym.Eq((prob * (1 / e_alpha_1) + (prob-1) * (1 / e_alpha_2))
                     , mean)
        eq2 = sym.Eq((prob * (e_alpha_1*(prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_1))*(e_alpha_1*(prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_1)) - 2) + 2)/(e_alpha_1**2)
                    + (1 - prob) * (e_alpha_2*(prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_1))*(e_alpha_2*(prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_1)) + 2) + 2)/(e_alpha_2**2)), var)
        result = sym.nsolve([eq1, eq2], (e_alpha_1, e_alpha_2), [0.5, 0.5])
        print(result)
        print(e_alpha_1, e_alpha_2, prob)
        print("e_alpha_1: ", result[0])
        print("e_alpha_2: ", result[1])
        return result[0], result[1]


def DE_stats(e_alpha_1, e_alpha_2, prob):
    mu_analytical = prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_2)
    # p * (a/ b) + (p - 1) * (c / d)
    var_analytical = prob * (e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical - 2) + 2)/(e_alpha_1**2) \
                    + (1 - prob) * (e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical + 2) + 2)/(e_alpha_2**2)
    Skewness_analytical = prob * (6 - e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical - 3) + 6))/(e_alpha_1**3) \
                         + (1 - prob) * (-1)*(6 + e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical + 3) + 6))/(e_alpha_2**3)

    Kurtosis_analytical = prob * (e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical*(e_alpha_1*mu_analytical - 4) + 12) - 24) + 24)/(e_alpha_1**4) \
                         + (1 - prob) * (e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical*(e_alpha_2*mu_analytical + 4) + 12) + 24) + 24)/(e_alpha_2**4)


    print("e_alpha_1, e_alpha_2, prob: ", e_alpha_1, e_alpha_2, prob)
    print("mu: ", mu_analytical)
    print("var: ", var_analytical)
    print("Skewness: ", Skewness_analytical)
    print("Kurtosis: ", Kurtosis_analytical)
    return mu_analytical, var_analytical, Skewness_analytical, Kurtosis_analytical
