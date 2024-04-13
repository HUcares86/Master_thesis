import sympy as sym
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
from Tools import *


# x,y = sym.symbols('x,y')
# eq1 = sym.Eq(x+y,5)
# eq2 = sym.Eq(x**2+y**2,17)
# result = sym.solve([eq1,eq2],(x,y))
# print(result)

# g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = 1.35, 2.5, 3.12, 1.56, 0.253

# g_beta_2, g_alpha_2, prob = 3.12, 1.56, 0.253


class double_gamma():
    def __init__(self, g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob):
        # jump upward
        self.g_beta_1 = g_beta_1
        self.g_alpha_1 = g_alpha_1
        # jump downward
        self.g_beta_2 = g_beta_2
        self.g_alpha_2 = g_alpha_2
        self.prob = prob
        # params
        self.mean = -1
        self.variance = -1
        self.skewness = -1
        self.kurtosis = -1

    def f_g_plus(self, x):
        f_of_x = ((self.g_beta_1**self.g_alpha_1)/math.gamma(self.g_alpha_1))*(x**(self.g_alpha_1-1))*(math.exp(-self.g_beta_1*x))
        return f_of_x

    def f_g_plus_array(self, x_array):
        f_of_xs_g_plus = []
        for x in x_array:
            f_of_x = ((self.g_beta_1**self.g_alpha_1)/math.gamma(self.g_alpha_1))*(x**(self.g_alpha_1-1))*(math.exp(-self.g_beta_1*x))
            f_of_xs_g_plus.append(f_of_x)

        Mean = n_th_moment(x_array, f_of_xs_g_plus, 0, 1)
        Variance = n_th_moment(x_array, f_of_xs_g_plus, Mean, 2)
        Skewness = n_th_moment(x_array, f_of_xs_g_plus, Mean, 3)
        Kurtosis = n_th_moment(x_array, f_of_xs_g_plus, Mean, 4)

        print("---"*20)
        print("parametrs of the right double gamma distribution")
        # print(f_of_xs_g_plus)
        print(f'Mean: {Mean}')
        print(f'Variance: {Variance}')
        print(f'Skewness: {Skewness}')
        print(f'Kurtosis: {Kurtosis}')

        return f_of_xs_g_plus

    def f_g_minus(self, x):
        f_of_x = ((self.g_beta_2**self.g_alpha_2)/math.gamma(self.g_alpha_2))*((-x)**(self.g_alpha_2-1))*(math.exp(self.g_beta_2*x))
        return f_of_x

    def f_g_minus_array(self, x_array):
        f_of_xs_g_minus = []
        for x in x_array:
            f_of_x = ((self.g_beta_2**self.g_alpha_2)/math.gamma(self.g_alpha_2))*((-x)**(self.g_alpha_2-1))*(math.exp(self.g_beta_2*x))
            f_of_xs_g_minus.append(f_of_x)

        Mean = n_th_moment(x_array, f_of_xs_g_minus, 0, 1)
        Variance = n_th_moment(x_array, f_of_xs_g_minus, Mean, 2)
        Skewness = n_th_moment(x_array, f_of_xs_g_minus, Mean, 3)
        Kurtosis = n_th_moment(x_array, f_of_xs_g_minus, Mean, 4)
        print("---"*20)
        print("parametrs of the left double gamma distribution")
        # print(f_of_xs_g_minus)
        print(f'Mean: {Mean}')
        print(f'Variance: {Variance}')
        print(f'Skewness: {Skewness}')
        print(f'Kurtosis: {Kurtosis}')
        return f_of_xs_g_minus

    def f_double_g(self, x_array):
        f_of_xs_double_g = []
        for x in x_array:
            if x > 0:
                f_of_x = self.prob * (self.f_g_plus(x))
            else:
                f_of_x = (1 - self.prob) * (self.f_g_minus(x))
            f_of_xs_double_g.append(f_of_x)

        Mean = n_th_moment(x_array, f_of_xs_double_g, 0, 1)
        Variance = n_th_moment(x_array, f_of_xs_double_g, Mean, 2)
        Skewness = n_th_moment(x_array, f_of_xs_double_g, Mean, 3)
        Kurtosis = n_th_moment(x_array, f_of_xs_double_g, Mean, 4)
        self.mean = Mean
        self.variance = Variance
        self.skewness = Skewness
        self.kurtosis = Kurtosis
        return f_of_xs_double_g

    def parameters_of_double_g(self):
        print("---"*20)
        print("parametrs of double gamma distribution")
        # print(f_of_xs_double_g)
        print(f'Mean: {self.mean}')
        print(f'Variance: {self.variance}')
        print(f'Skewness: {self.skewness}')
        print(f'Kurtosis: {self.kurtosis}')

    def double_g_n_th_moment(self, x_array, n, moment_type):
        f_of_xs_double_g = []
        for x in x_array:
            if x > 0:
                f_of_x = self.prob * (self.f_g_plus(x))
            else:
                f_of_x = (1 - self.prob) * (self.f_g_minus(x))
            f_of_xs_double_g.append(f_of_x)

        double_g_Mean = n_th_moment(x_array, f_of_xs_double_g, 0, 1)
        if moment_type == 'raw':
            double_g_moment = n_th_moment(x_array, f_of_xs_double_g, 0, n)
        if moment_type == 'center':
            double_g_moment = n_th_moment(x_array, f_of_xs_double_g, double_g_Mean, n)

        print("---" * 20)
        print(f'the {n} th {type} moment of normaldistribution is: {double_g_moment}')

    def plot_f_g_plus_and_f_g_minus(self, x_plus, x_minus):
        plt.plot(x_plus, self.f_g_plus(x_plus), label='plus')
        plt.plot(x_minus, self.f_g_minus(x_minus), label='minus')
        plt.axvline(0, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper right')
        plt.show()

    def plot_f_double_g(self, x_array):
        plt.plot(x_array, self.f_double_g(x_array), label='double gamma')
        plt.axvline(self.mean, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper right')
        plt.show()




def DG_solve_eq(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob, fix, mean, var):
    if fix == "b1,b2,p":
        g_alpha_1, g_alpha_2 = sym.symbols('g_alpha_1, g_alpha_2')
        eq1 = sym.Eq((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)), mean)
        eq2 = sym.Eq(prob * ((g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_1 / g_beta_1 + (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_2 / g_beta_2 +(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2), var)
        result = sym.nsolve([eq1, eq2], (g_alpha_1, g_alpha_2), [0, 0])
        # print(result)
        print("alpha1: ", result[0])
        print("alpha2: ", result[1])
        return result[0], result[1]
    if fix == "a1,a2,p":
        g_beta_1, g_beta_2 = sym.symbols('g_beta_1, g_beta_2')
        eq1 = sym.Eq((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)), mean)
        eq2 = sym.Eq(prob * ((g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_1 / g_beta_1 + (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_2 / g_beta_2 +(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2), var)
        result = sym.nsolve([eq1, eq2], (g_beta_1, g_beta_2), [1, 1])
        # print(result)
        print("beta1: ", result[0])
        print("beta2: ", result[1])
        return result[0], result[1]
    if fix == "a2,b2,p":
        g_alpha_1, g_beta_1 = sym.symbols('g_alpha_1, g_beta_1')
        eq1 = sym.Eq((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)), mean)
        eq2 = sym.Eq(prob * ((g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_1 / g_beta_1 + (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_2 / g_beta_2 +(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2), var)
        result = sym.nsolve([eq1, eq2], (g_alpha_1, g_beta_1), [0, 1])
        # print(result)
        print("g_alpha_1: ", result[0])
        print("g_beta_1: ", result[1])
        return result[0], result[1]
    if fix == "a1,b1,p":
        g_alpha_2, g_beta_2 = sym.symbols('g_alpha_2, g_beta_2')
        eq1 = sym.Eq((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)), mean)
        eq2 = sym.Eq(prob * ((g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_1 / g_beta_1 + (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 2 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * g_alpha_2 / g_beta_2 +(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2), var)
        result = sym.nsolve([eq1, eq2], (g_alpha_2, g_beta_2), [0, 1])
        # print(result)
        print("g_alpha_2: ", result[0])
        print("g_beta_2: ", result[1])
        return result[0], result[1]


def DG_solve_eq2(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob, fix, sk, kur):
    if fix == "b1,b2,p":
        g_alpha_1, g_alpha_2 = sym.symbols('g_alpha_1, g_alpha_2')
        # mu_analytical = (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2))
        eq1 = sym.Eq((prob * ((g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3) - 3 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) + 3 * (
                                             (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) * g_alpha_1 / g_beta_1 - (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 3) + \
                         (1 - prob) * (-(g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / ( g_beta_2 ** 3) - 3 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) - 3 * (
                        (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) * g_alpha_2 / g_beta_2 - (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 3)),sk)
        eq2 = sym.Eq((prob * (
                (g_alpha_1 + 3) * (g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 4) - 4 *(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2))* (
                    g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3)
                + 6 * ((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 4 * (
                            (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 3) * g_alpha_1 / g_beta_1 + (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 4) + \
                         (1 - prob) * ((g_alpha_2 + 3) * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 4) + 4 * (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 3)
                                       + 6 * ((prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 4 * (
                                                   (prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2))** 3) * g_alpha_2 / g_beta_2 +(prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)) ** 4)), kur)
        result = sym.nsolve([eq1, eq2], (g_alpha_1, g_alpha_2), [1, 1])
        # print(result)
        print("alpha1: ", result[0])
        print("alpha2: ", result[1])
        return result[0], result[1]




def DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob):
    mu_analytical = prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)
    # p * (a/ b) + (p - 1) * (c / d)

    var_analytical = prob * ((g_alpha_1 + 1) * g_alpha_1 / (
                g_beta_1 ** 2) - 2 * mu_analytical * g_alpha_1 / g_beta_1 + mu_analytical ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 2) + 2 * mu_analytical * g_alpha_2 / g_beta_2 + mu_analytical ** 2)
    # p((a + 1) a/ (b ** 2) - 2 * (p (a /b) + (p - 1) * (c / d)) * a / b + (p * (a / b) + (p - 1) (c / d)) ** 2) + (1 - p) ((c + 1)c / (d ** 2) + 2 * (p* (a/ b) + (p - 1) * (c / d)) * c / d +(p * (a / b) + (p - 1) * (c / d)) ** 2)

    Skewness_analytical = (prob * ((g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3) - 3 * mu_analytical * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) + 3 * (
                                             mu_analytical ** 2) * g_alpha_1 / g_beta_1 - mu_analytical ** 3) + \
                         (1 - prob) * (-(g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 3) - 3 * mu_analytical * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) - 3 * (
                                                   mu_analytical ** 2) * g_alpha_2 / g_beta_2 - mu_analytical ** 3))

    Kurtosis_analytical = (prob * (
                (g_alpha_1 + 3) * (g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 4) - 4 * mu_analytical * (
                    g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3)
                + 6 * (mu_analytical ** 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 4 * (
                            mu_analytical ** 3) * g_alpha_1 / g_beta_1 + mu_analytical ** 4) + \
                         (1 - prob) * ((g_alpha_2 + 3) * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 4) + 4 * mu_analytical * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 3)
                                       + 6 * (mu_analytical ** 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 4 * (
                                                   mu_analytical ** 3) * g_alpha_2 / g_beta_2 + mu_analytical ** 4))
    # print("g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob: ", g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
    # print("mu: ", mu_analytical)
    # print("var: ", var_analytical)
    # print("Skewness: ", Skewness_analytical)
    # print("Kurtosis: ", Kurtosis_analytical)
    # print("&",mu_analytical,"&", var_analytical,"&", Skewness_analytical,"&", Kurtosis_analytical)
    # print("&", np.round(mu_analytical, 4), "&", np.round(var_analytical, 4), "&", np.round(Skewness_analytical, 4), "&",np.round(Kurtosis_analytical, 4))
    return mu_analytical, var_analytical, Skewness_analytical, Kurtosis_analytical

