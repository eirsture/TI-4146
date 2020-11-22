def print_num(num):
    return format(num, ".4f")

def capm(r_f, r_m, b_p, variable_name="p"):
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
    r_f = 1  # Risk-free interest rate
    r_m = 1  # Return of market
    b_p = 1  # Beta of return you need calculated, e.g. asset

    capm(r_f, r_m, b_p, variable_name="a")
