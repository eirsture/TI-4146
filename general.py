def print_num(num):
    return format(num, ".4f")

def capm(r_f, r_m, b_p, variable_name="p", market_premium=None):
    if market_premium:
        print("r_{%s}=r_{f}+MRP \cdot \\beta_{%s}" % (variable_name, variable_name))
        print("r_{%s}=%s+%s \cdot %s" % (variable_name, r_f, market_premium, b_p))
        r_p = float(format(r_f + market_premium * b_p, ".4f"))
    else:
        print("r_{%s}=r_{f}+\left(r_{m}-r_{f}\\right) \cdot \\beta_{%s}" % (variable_name, variable_name))
        print("r_{%s}=%s+\left(%s-%s\\right) \cdot %s" % (variable_name, r_f, r_m, r_f, b_p))
        r_p = float(format(r_f + (r_m-r_f)*b_p, ".4f"))

    print("r_{%s} = %s" % (variable_name, r_p))
    return r_p

def wacc_after_tax(r_d, r_e, D, E, V, tax):
    wacc = float(format(r_e*(E/V) + r_d*(1-tax)*(D/V), ".4f"))
    print(f'WACC: {print_num(wacc)}')
    return wacc

if __name__ == '__main__':
    r_f = None  # Risk-free interest rate
    r_m = None  # Return of market
    b_p = None  # Beta of return you need calculated, e.g. asset

    capm(r_f, r_m, b_p, variable_name="a")
