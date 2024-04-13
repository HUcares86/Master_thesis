from Tools import *


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



def Normal_stats_analytical(mu, sig):
    mu_analytical = mu
    # p * (a/ b) + (p - 1) * (c / d)
    var_analytical = sig**2
    Skewness_analytical = 0
    Kurtosis_analytical = 3*sig**4

    print("Normal_stats_analytical: ")
    print("mu: ", mu_analytical)
    print("var: ", var_analytical)
    print("Skewness: ", Skewness_analytical)
    print("Kurtosis: ", Kurtosis_analytical)
    return mu_analytical, var_analytical, Skewness_analytical, Kurtosis_analytical
