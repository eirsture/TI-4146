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
    det = (log(stock_price / exercise_price) + (interest_rate + 1/2 * volatility**2)*time) / (volatility * sqrt(time))
    print(f'First determinant: {det}')
    print(f'Formatted first determinant: {format(det, ".4f")} \n')
    return det


def second_determinant(determinant1, volatility, time) -> float:
    """
    d_2 = d_1 - sigma * sqrt(T)
    """
    det = determinant1 - volatility * sqrt(time)
    print(f'Second determinant: {det}')
    print(f'Formatted second determinant: {format(det, ".4f")} \n')
    return det


def normal_distribution(d) -> float:
    return NormalDist().cdf(d)


def put_option(exercise_price, interest_rate, time, stock_price, determinant1, determinant2) -> float:
    """
     O_p,0 = Xe**(−rT) *  N(−d2) − S_0 * N(−d1)
    """

    return exercise_price * exp(-interest_rate * time) * normal_distribution(
        -determinant2) - stock_price * normal_distribution(-determinant1)


def call_option(exercise_price, interest_rate, time, stock_price, determinant1, determinant2) -> float:
    """
    O_c,0 = S_0 * N(d_1) - X*e^(-rT) * N(d_2)
    """

    return stock_price * normal_distribution(determinant1) - exercise_price * exp(
        -interest_rate * time) * normal_distribution(determinant2)


if __name__ == '__main__':
    #  Input values:
    option_type = "call"  # "put" or "call"
    S_0 = 100  # Stock price at time 0
    X = 100  # Exercise price
    sigma = 0.2  # Diffusion coefficient, representing the stock's volatility
    r = 0.1  # Risk-free interest rate
    T = 1  # Time

    #  Calculate determinants
    d_1 = first_determinant(S_0, X, r, sigma, T)
    d_2 = second_determinant(d_1, sigma, T)
    if not (option_type == "put" or option_type == "call"):
        print(f'{option_type} is an invalid option type. Legal values are ("put", "call")')
        option_price = ''
    elif option_type == "put":
        print("Calculating put option:")
        option_price = put_option(X, r, T, S_0, d_1, d_2)
    elif option_type == "call":
        print("Calculating call option:")
        option_price = call_option(X, r, T, S_0, d_1, d_2)
    else:
        print("You should not be here")

    print(f'Option price: {option_price}')
    print(f'Formatted option price: {format(option_price, ".4f")}')
