from general import format_float, capm, unlevered_cash_flow, npv, tax_shield, apv


def print_num(num):
    return format(num, ".4f")


def calculate_equity_return(occ, debt_return, tax, debt, equity):
    r_e = occ + (occ-debt_return)*(1-tax)*(debt/equity)
    print(f'r_e = {print_num(r_e)}')
    return r_e


def calculate_occ(debt_return, equity_return, debt, equity, tax, value):
    occ = format_float(debt_return*(1-tax)*(debt)/(value - tax*debt) + equity_return*equity/(value - tax*debt))
    print("r_{a}=r_{d} \cdot (1-\\tau) \cdot \\frac{D}{V-\\tau D}+r_{e} \cdot \\frac{E}{V-\\tau D}")
    print("r_{a}=%s \cdot (1-%s) \cdot \\frac{%s}{%s-%s \cdot %s}+%s \cdot \\frac{%s}{%s-%s \cdot %s}" % (debt_return, tax, debt, value, tax, debt, equity_return, equity, value, tax, debt))
    print('r_{a}=%s' % (occ))
    return occ


def calculate_beta_equity(debt, equity, tax, beta_assets, beta_debt):
    beta_e = beta_assets + (1-tax)*(beta_assets - beta_debt)*(debt/equity)
    print(f'beta_e = {print_num(beta_e)}')
    return beta_e


def calculate_beta_assets(beta_debt, beta_equity, debt, equity, value, tax):
    beta_a = beta_debt*(1-tax)*debt/(value - tax*debt) + beta_equity*equity/(value - tax*debt)
    print(f'beta_a = {print_num(beta_a)}')
    return beta_a


if __name__ == '__main__':
    b_a = None  # Beta of assets
    b_e = None  # Beta of equity
    b_d = None  # Beta of debt

    r_a = None  # Opportunity cost of capital = Return of assets
    r_d = None  # Return of debt
    r_e = None  # Return of equity
    r_f = None  # Risk-free interest rate

    debt = None  # Value of debt
    equity = None  # Value of equity
    value = debt + equity  # Total value of assets

    tax_rate = None  # Corporate tax rate

    # Is this needed, or is value = investment?
    investment = None  # Value of investment for project
    cash_flow = None  # Annual cash flow from project

    # r_e = calculate_equity_return(r_a, r_d, tax_rate, debt, equity)
    # r_a = calculate_occ(r_d, r_e, debt, equity, tax_rate, value)

    # b_e = calculate_beta_equity(debt, equity, tax_rate, b_a, b_d)
    # b_a = calculate_beta_assets(b_d, b_e, debt, equity, value, tax_rate)

    # unlevered_c_flow = unlevered_cash_flow(cash_flow=cash_flow, occ=r_a, tax_rate=tax_rate, tax_done=True)
    # npv = npv(cash_flow=unlevered_c_flow, investment=investment)
    # tax_shield = tax_shield(debt=debt, interest_rate=r_d, tax_rate=tax_rate, debt_type="predetermined")
    # apv = apv(npv, tax_shield)



