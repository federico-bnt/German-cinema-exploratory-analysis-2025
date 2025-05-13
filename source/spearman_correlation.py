# spearman_correlation_utils.py

from scipy import stats

def print_spearman_correlation(x, y, label=""):
    """
    Calculate and print Spearman correlation coefficient and p-value with interpretation.

    Parameters:
        x (array-like or pd.Series): First variable (e.g., ticket prices).
        y (array-like or pd.Series): Second variable (e.g., attendance).
        label (str): Optional label for the analysis context.
    """
    correlation_result = stats.spearmanr(x, y)
    r = correlation_result.correlation
    p = correlation_result.pvalue

    print(f"Spearman Correlation Analysis{f' ({label})' if label else ''}:")
    print("-" * (35 + len(label)))
    print(f"Spearman correlation coefficient (r): {r:.3f}")
    print(f"P-value: {p:.3f}")

    if r < 0:
        print("The correlation coefficient is negative, indicating a tendency toward anticorrelation.")
    else:
        print("The correlation coefficient is positive, indicating a tendency toward correlation.")

    if p < 0.05:
        print("The correlation is statistically significant.")
    else:
        print("The correlation is not statistically significant.")

    