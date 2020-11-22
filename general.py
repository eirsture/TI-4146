def print_num(num):
    return format(num, ".4f")

def capm(r_f, r_m, b_p):
    r_p = r_f + (r_m-r_f)*b_p
    print(f'r_p from CAPM: {print_num(r_p)}')
    return r_p


def wacc(r_d, r_e, D, E, V, tax):
    wacc = r_e*(E/V) + r_d*(1-tax)*(D/V)
    print(f'WACC: {print_num(wacc)}')
    return wacc

if __name__ == '__main__':
    r_f = None  # Risk-free interest rate
    r_m = None  # Return of market
    b_p = None  # Beta of return you need calculated, e.g. asset

    capm(r_f, r_m, b_p)
