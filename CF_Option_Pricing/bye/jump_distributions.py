import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy


def n_th_moment(x, counts, c, n):
    return np.sum(counts*(x-c)**n) / np.sum(counts)


class normal():
    def __init__(self, mu_normal, sig_normal):
        self.mu_normal = mu_normal
        self.sig_normal = sig_normal
        # parameters
        self.mean = -1
        self.variance = -1
        self.skewness = -1
        self.kurtosis = -1

    def f_n(self, x_array):
        f_of_xs_n = []
        for x in x_array:
            f_of_x = (1/(np.sqrt(2*np.pi*self.sig_normal))) * np.exp(-((x-self.mu_normal)**2)/(2*self.sig_normal**2))
            f_of_xs_n.append(f_of_x)

        Mean = n_th_moment(x_array, f_of_xs_n, 0, 1)
        Variance = n_th_moment(x_array, f_of_xs_n, Mean, 2)
        Skewness = n_th_moment(x_array, f_of_xs_n, Mean, 3)
        Kurtosis = n_th_moment(x_array, f_of_xs_n, Mean, 4)
        self.mean = Mean
        self.variance = Variance
        self.skewness = Skewness
        self.kurtosis = Kurtosis

        return f_of_xs_n

    def parameters_of_normal(self):
        print("---"*20)
        print("parametrs of normal distribution")
        print(f'Mean: {self.mean}')
        print(f'Variance: {self.variance}')
        print(f'Skewness: {self.skewness}')
        print(f'Kurtosis: {self.kurtosis}')

    def normal_n_th_moment(self, x_array, n, moment_type):
        f_of_xs_n = []
        for x in x_array:
            f_of_x = (1/(np.sqrt(2*np.pi*self.sig_normal))) * np.exp(-((x-self.mu_normal)**2)/(2*self.sig_normal**2))
            f_of_xs_n.append(f_of_x)
        Mean = n_th_moment(x_array, f_of_xs_n, 0, 1)
        if moment_type == 'raw':
            moment = n_th_moment(x_array, f_of_xs_n, 0, n)
        if moment_type == 'center':
            moment = n_th_moment(x_array, f_of_xs_n, Mean, n)

        print("---"*20)
        print(f'the {n} th {moment_type} moment of normal distribution is: {moment}')

    def plot_f_n(self, x_array):
        plt.plot(x_array, self.f_n(x_array), label='normal')
        plt.axvline(self.mu_normal, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper right')
        plt.show()


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

    def parameters_of_double_exp(self):
        print("---"*20)
        print("parametrs of double exponential distribution")
        print(f'Mean: {self.mean}')
        print(f'Variance: {self.variance}')
        print(f'Skewness: {self.skewness}')
        print(f'Kurtosis: {self.kurtosis}')

    def double_exp_n_th_moment(self, x_array, n, moment_type):
        double_exp_Mean = n_th_moment(x_array, self.f_of_xs_double_exp, 0, 1)
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
        plt.plot(x_array, self.f_of_xs_double_exp, label='double gamma')
        plt.axvline(self.mean, color='black', linewidth=0.4)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc='upper right')
        plt.show()







