import numpy as np
from scipy.stats import chi2

def chi_square_test(observed, expected):
    chi_squared = np.sum((observed - expected) ** 2 / expected)
    df = len(observed) - 1
    p_value = 1 - chi2.cdf(chi_squared, df)
    return chi_squared, df, p_value

observed = np.array([10, 20, 30, 40])
expected = np.array([15, 15, 25, 25])

chi_squared, df, p_value = chi_square_test(observed, expected)

print("Chi-square statistic:", chi_squared)
print("Degrees of freedom:", df)
print("P-value:", p_value)
