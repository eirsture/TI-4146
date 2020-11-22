def print_tree(tree):
    for item in tree:
        print(item)
    print('\n\n')


def create_matrix(length) -> list:
    matrix = []
    for i in range(length + 1):
        row = []
        for j in range(length + 1):
            row.append(None)
        matrix.append(row)

    return matrix


def create_binomial_tree(period, stock_price, upwards_factor, downwards_factor) -> list:
    stock_values = create_matrix(period)
    stock_values[0][0] = stock_price
    for i in range(1, periods + 1):
        stock_values[i][0] = stock_values[i - 1][0] * upwards_factor
        for j in range(1, i + 1):
            stock_values[i][j] = stock_values[i - 1][j - 1] * downwards_factor

    return stock_values


def final_node_price(period, stock_values, put_or_call, exercise_price) -> list:
    option_values = create_matrix(period)
    for j in range(period + 1):
        if put_or_call == "call":
            option_values[period][j] = max(0, stock_values[period][j] - exercise_price)
        elif put_or_call == "put":
            option_values[period][j] = max(0, exercise_price - stock_values[period][j])

    return option_values


def calculate_option_price(period, stock_values, put_or_call, exercise_price, p_value, rate_factor) -> float:
    option_values = final_node_price(period, stock_values, put_or_call, exercise_price)

    for i in range(period - 1, -1, -1):
        for j in range(i + 1):
            if put_or_call == "put":

                option_values[i][j] = max(0,
                                          exercise_price - stock_values[i][j],
                                          (p_value * option_values[i + 1][j] + (1 - p_value) * option_values[i + 1][
                                              j + 1]) / rate_factor)

            elif put_or_call == "call":
                option_values[i][j] = max(0,
                                          stock_values[i][j] - exercise_price,
                                          (p_value * option_values[i + 1][j] + (1 - p_value) * option_values[i + 1][
                                              j + 1]) / rate_factor)
    return option_values


if __name__ == '__main__':
    #  Input values:
    option_type = "call"  # "put" or "call"
    periods = None  # Determines the depth of the binomial tree. Most likely 1 or 2.
    S_0 = None  # Stock price at time 0
    X = None  # Exercise price
    rate = None  # Risk-free rate, 0<= x <= 1
    up = None  # Upwards probability, 0<= x <= 1
    down = None  # Downwards probability, 0<= x <= 1

    # Factors
    u = 1 + up  # Upwards factor
    d = 1 - down  # Downwards factor
    r = 1 + rate  # Risk-free rate factor
    p = (r - d) / (u - d)  # Probability of upwards

    print("O=\\frac{p \cdot O_{u}+(1-p) \cdot O_{d}}{r}")
    print("O=\\frac{%s \cdot O_{u}+(1-%s) \cdot O_{d}}{%s}" % (p, p, r))

    binomial_tree = create_binomial_tree(periods, S_0, u, d)
    print_tree(binomial_tree)
    option_values = calculate_option_price(periods, binomial_tree, option_type, X, p, r)
    print_tree(option_values)
