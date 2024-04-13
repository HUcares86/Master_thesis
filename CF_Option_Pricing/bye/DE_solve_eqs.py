import sympy as sym


def DE_solve_eq(e_alpha_1, e_alpha_2, prob, fix, mean, var, Skewness, Kurtosis):
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
    mu_numerical = prob * (1 / e_alpha_1) + (prob - 1) * (1 / e_alpha_2)
    # p * (a/ b) + (p - 1) * (c / d)
    var_numerical = prob * (e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical - 2) + 2)/(e_alpha_1**2) \
                    + (1 - prob) * (e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical + 2) + 2)/(e_alpha_2**2)
    Skewness_numerical = prob * (6 - e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical - 3) + 6))/(e_alpha_1**3) \
                         + (1 - prob) * (-1)*(6 + e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical + 3) + 6))/(e_alpha_2**3)

    Kurtosis_numerical = prob * (e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical*(e_alpha_1*mu_numerical - 4) + 12) - 24) + 24)/(e_alpha_1**4) \
                         + (1 - prob) * (e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical*(e_alpha_2*mu_numerical + 4) + 12) + 24) + 24)/(e_alpha_2**4)


    print("e_alpha_1, e_alpha_2, prob: ", e_alpha_1, e_alpha_2, prob)
    print("mu_numerical: ", mu_numerical)
    print("var_numerical: ", var_numerical)
    print("Skewness: ", Skewness_numerical)
    print("Kurtosis: ", Kurtosis_numerical)
    return mu_numerical, var_numerical, Skewness_numerical, Kurtosis_numerical
