from statistics import NormalDist
from math import sqrt, log, exp

"""
Call: O_c,0 = S_0 * N(d_1) - X*e^(-rT) * N(d_2)
Put: O_p,0 = Xe**(−rT) *  N(−d2) − S_0 * N(−d1)

S_0 = Stock price at time 0
N(d_1) = Option delta, (hedge ratio, sensitivity, moneyness)
X*e^(-rT) = Present value, exercise price = X/()
r = Risk-free interest rate
T = Time
N(d_2) = Probability of exercise
"""

"""
    option_type = None  # "put" or "call"
    S_0 = None  # Stock price at time 0
    X = None  # Exercise price
    u = None  # Drift coefficient, representing the stock's return
    sigma = None  # Diffusion coefficient, representing the stock's volatility
    r = None  # Risk-free interest rate
    T = None  # Time
"""


def first_determinant(stock_price, exercise_price, interest_rate, volatility, time) -> float:
    """
    d_1 = (ln(S_0 / X) + (r + 1/2 * sigma**2 ) * T) / (sigma * sqrt(T))
    """
    print("d_{1}=\\frac{\ln \left(S_{0} / X\\right)+\left(r+\\frac{1}{2} \sigma^{2}\\right) T}{\sigma \sqrt{T}}")
    print("d_{1}=\\frac{\ln \left(%s / %s\\right)+\left(%s+\\frac{1}{2} %s^{2}\\right) %s}{%s \sqrt{%s}}" % (
    stock_price, exercise_price, interest_rate, volatility, time, volatility, time))

    det = float(format((log(stock_price / exercise_price) + (interest_rate + 1/2 * volatility**2)*time) / (volatility * sqrt(time)), ".4f"))
    print('d_{1}= %s \n\n' % (det))
    return det


def second_determinant(determinant1, volatility, time) -> float:
    """
    d_2 = d_1 - sigma * sqrt(T)
    """
    print("d_{2}= d_{1} - \sigma \sqrt{T}")
    print("d_{2}= %s - %s \sqrt{%s}" % (determinant1, volatility, time))

    det = float(format(determinant1 - volatility * sqrt(time), ".4f"))
    print('d_{2}= %s \n\n' % (det))
    return det


def normal_distribution(d) -> float:
    return NormalDist().cdf(d)


def put_option(exercise_price, interest_rate, time, stock_price, determinant1, determinant2) -> float:
    """
     O_p,0 = Xe**(−rT) *  N(−d2) − S_0 * N(−d1)
    """
    print("O_{p, 0}=X \cdot e^{-r \cdot T} \cdot N\left(-d_{2}\\right)-S_{0} \cdot N\left(-d_{1}\\right)")
    print("O_{p, 0}=%s \cdot e^{-%s \cdot %s} \cdot N\left(-%s\\right)-%s \cdot N\left(-%s\\right)" % (
        exercise_price, interest_rate, time, determinant2, stock_price, determinant1))

    option_price = float(format(exercise_price * exp(-interest_rate * time) * normal_distribution(
        -determinant2) - stock_price * normal_distribution(-determinant1), ".4f"))
    print('O_{p, 0}= %s \n\n' % (option_price))
    return option_price


def call_option(exercise_price, interest_rate, time, stock_price, determinant1, determinant2) -> float:
    """
    O_c,0 = S_0 * N(d_1) - X*e^(-rT) * N(d_2)
    """
    print("O_{c, 0}=S_{0} \cdot N(d_{1}) - X \cdot e^{-r \cdot T} \cdot N(d_{2})")
    print("O_{c, 0}=%s \cdot N(%s) - %s \cdot e^{-%s \cdot %s} \cdot N(%s)" % (
        stock_price, determinant1, exercise_price, interest_rate, time, determinant2))

    option_price = float(format(stock_price * normal_distribution(determinant1) - exercise_price * exp(
        -interest_rate * time) * normal_distribution(determinant2), ".4f"))
    print('O_{c, 0}= %s \n\n' % (option_price))
    return option_price


if __name__ == '__main__':
    #  Input values:
    option_type = "call"  # "put" or "call"
    S_0 = None  # Stock price at time 0
    X = None  # Exercise price
    sigma = None  # Diffusion coefficient, representing the stock's volatility
    r = None  # Risk-free interest rate
    T = None  # Time

    #  Calculate determinants
    d_1 = first_determinant(S_0, X, r, sigma, T)
    d_2 = second_determinant(d_1, sigma, T)
    if not (option_type == "put" or option_type == "call"):
        print(f'{option_type} is an invalid option type. Legal values are ("put", "call")')
    elif option_type == "put":
        print("Calculating put option:")
        option_price = put_option(X, r, T, S_0, d_1, d_2)
    elif option_type == "call":
        print("Calculating call option:")
        option_price = call_option(X, r, T, S_0, d_1, d_2)
    else:
        print("You should not be here")
