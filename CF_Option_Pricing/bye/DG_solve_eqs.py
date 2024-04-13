import sympy as sym
# x,y = sym.symbols('x,y')
# eq1 = sym.Eq(x+y,5)
# eq2 = sym.Eq(x**2+y**2,17)
# result = sym.solve([eq1,eq2],(x,y))
# print(result)

# g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob = 1.35, 2.5, 3.12, 1.56, 0.253

# g_beta_2, g_alpha_2, prob = 3.12, 1.56, 0.253

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


def DG_stats(g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob):
    mu_numerical = prob * (g_alpha_1 / g_beta_1) + (prob - 1) * (g_alpha_2 / g_beta_2)
    # p * (a/ b) + (p - 1) * (c / d)

    var_numerical = prob * ((g_alpha_1 + 1) * g_alpha_1 / (
                g_beta_1 ** 2) - 2 * mu_numerical * g_alpha_1 / g_beta_1 + mu_numerical ** 2) + \
                    (1 - prob) * ((g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 2) + 2 * mu_numerical * g_alpha_2 / g_beta_2 + mu_numerical ** 2)
    # p((a + 1) a/ (b ** 2) - 2 * (p (a /b) + (p - 1) * (c / d)) * a / b + (p * (a / b) + (p - 1) (c / d)) ** 2) + (1 - p) ((c + 1)c / (d ** 2) + 2 * (p* (a/ b) + (p - 1) * (c / d)) * c / d +(p * (a / b) + (p - 1) * (c / d)) ** 2)

    Skewness_numerical = prob * ((g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3) - 3 * mu_numerical * (
                g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) + 3 * (
                                             mu_numerical ** 2) * g_alpha_1 / g_beta_1 - mu_numerical ** 3) + \
                         (1 - prob) * (-(g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 3) - 3 * mu_numerical * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) - 3 * (
                                                   mu_numerical ** 2) * g_alpha_2 / g_beta_2 - mu_numerical ** 3)

    Kurtosis_numerical = prob * (
                (g_alpha_1 + 3) * (g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 4) - 4 * mu_numerical * (
                    g_alpha_1 + 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 3)
                + 6 * (mu_numerical ** 2) * (g_alpha_1 + 1) * g_alpha_1 / (g_beta_1 ** 2) - 4 * (
                            mu_numerical ** 3) * g_alpha_1 / g_beta_1 + mu_numerical ** 4) + \
                         (1 - prob) * ((g_alpha_2 + 3) * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (
                g_beta_2 ** 4) + 4 * mu_numerical * (g_alpha_2 + 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 3)
                                       + 6 * (mu_numerical ** 2) * (g_alpha_2 + 1) * g_alpha_2 / (g_beta_2 ** 2) + 4 * (
                                                   mu_numerical ** 3) * g_alpha_2 / g_beta_2 + mu_numerical ** 4)
    print("g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob: ", g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob)
    print("mu_numerical: ", mu_numerical)
    print("var_numerical: ", var_numerical)
    print("Skewness: ", Skewness_numerical)
    print("Kurtosis: ", Kurtosis_numerical)
    return mu_numerical, var_numerical, Skewness_numerical, Kurtosis_numerical


# g_beta_1, g_alpha_1, g_beta_2, g_alpha_2, prob
# mu_numerical, var_numerical, Skewness_numerical, Kurtosis_numerical = DG_stats(2, 1.5, 3, 2, 0.5)
# print("----"*10)
# mu_numerical_1, var_numerical_1, Skewness_numerical_1, Kurtosis_numerical_1 = DG_stats(2, 4.78768939065119, 3, 0.659059342886310, 0.1)
# print("----"*10)
# mu_numerical_2, var_numerical_2, Skewness_numerical_2, Kurtosis_numerical_2 = DG_stats(2, 3.07195203324355, 3, 0.995732012466332, 0.2)
# print("----"*10)
# DG_solve_eq(2, 0, 3, 0, 0.2, "b1,b2,p", 0.041666666666666685, 0.8003472222222223)
# wolframe alpha
# 0.5(a/ 2.5) + (0.5 - 1)(c / 3) = -0.033333333333333326
# 0.5((a + 1) a/ (2.5 ** 2) - 2 * (0.5(a /2.5) + (0.5 - 1) * (c / 3)) * a / 2.5 + (0.5 * (a / 2.5) + (0.5 - 1) (c / 3)) ** 2) + (1 - 0.5) ((c + 1)c / (3 ** 2) + 2 * (0.5* (a/2.5) + (0.5- 1) * (c / 3)) * c / 3 +(0.5 * (a / 2.5) + (0.5 - 1) * (c / 3)) ** 2) = 0.6322222222222222

