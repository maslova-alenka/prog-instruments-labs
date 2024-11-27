import numpy as np
import scipy.stats as sts
import statistics as st


GAMMA = 0.90
A = 3
SIGMA2 = 2
N = 17


def find_expectation(data: np.ndarray, gamma: float, sigma: float) -> tuple:
    """
    Computes the confidence interval for the expected value of a sample
    from a normal population with known variance.

    Parameters:
        data: A sample from a normal population.
        gamma: The confidence level.
        sigma: The standard deviation.

    Returns:
        A tuple containing the lower and upper bounds of the confidence interval.
    """
    t_gamma = sts.norm.ppf((1 + gamma) / 2, loc=0, scale=1)
    delta = t_gamma * sigma / np.sqrt(len(data))
    a_left = data.mean() - delta
    a_right = data.mean() + delta
    return a_left, a_right


def find_expectation_no_dis(data: np.ndarray, gamma: float) -> tuple:
    """
    Computes the confidence interval for the expected value of a sample
    from a normal population with unknown variance.

    Parameters:
        data: A sample from a normal population.
        gamma: The confidence level.

    Returns:
        A tuple containing the lower and upper bounds of the confidence interval.
    """
    t = sts.t.ppf((1 + gamma) / 2, df=len(data) - 1)
    s = np.sqrt(st.pvariance(data))
    delta = t * s / np.sqrt(len(data))
    a_left = data.mean() - delta
    a_right = data.mean() + delta
    return a_left, a_right


if __name__ == "__main__":
    arr = np.random.normal(loc=A, scale=np.sqrt(SIGMA2), size=N)
    print(find_expectation(arr, GAMMA, np.sqrt(SIGMA2)))
    print(sts.norm.interval(GAMMA, loc=arr.mean(), scale=np.sqrt(SIGMA2) / np.sqrt(N)))
    print(find_expectation_no_dis(arr, GAMMA))
    print(sts.t.interval(GAMMA, df=N - 1, loc=arr.mean(), scale=np.sqrt(st.pvariance(arr)) / np.sqrt(N)))
