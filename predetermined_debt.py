def print_num(num):
    return format(num, ".4f")

def calculate_equity_return(occ, debt_return, tax, debt, equity):
    r_e = occ + (occ-debt_return)*(1-tax)*(debt/equity)
    print(f'r_e = {print_num(r_e)}')
    return r_e

def calculate_occ(debt_return, equity_return, debt, equity, tax, value):
    occ = debt_return*(1-tax)*(debt)/(value - tax*debt) + equity_return*equity/(value - tax*debt)
    print(f'occ = {print_num(occ)}')
    return occ

def calculate_beta_equity(debt, equity, tax, beta_assets, beta_debt):
    beta_e = beta_assets + (1-tax)*(beta_assets - beta_debt)*(debt/equity)
    print(f'beta_e = {print_num(beta_e)}')
    return beta_e


def calculate_beta_assets(beta_debt, beta_equity, debt, equity, value, tax):
    beta_a = beta_debt*(1-tax)*debt/(value - tax*debt) + beta_equity*equity/(value - tax*debt)
    print(f'beta_a = {print_num(beta_a)}')
    return beta_a

def yearly_interest_charge(loan, interest_rate):
    charge = interest_rate*loan
    print(f'Yearly interest charge = Loan * Interest Rate = {print_num(charge)}')
    return charge

def tax_advantage(tax, interest_charge):
    t_a = tax*interest_charge
    print(f'Yearly tax advantage = Tax rate * Yearly Interest Charge = {print_num(t_a)}')
    return t_a

def tax_shield(debt, interest_rate, tax_rate):
    interest_charge = yearly_interest_charge(debt, interest_rate)
    tax_advg = tax_advantage(tax_rate, interest_charge)
    tax_shield = tax_advg/interest_rate
    print(f'Discounted tax advantage = Tax shield = {print_num(tax_shield)}')
    return tax_shield

def unlevered_cash_flow(cash_flow, occ, tax_rate=None, tax_done=True):
    if tax_done:
        c_flow = cash_flow/occ
    else:
        c_flow = (1-tax_rate)*cash_flow/occ
    print(f'Value of \'unlevered\' cash flow = {print_num(c_flow)}')
    return c_flow

def npv(cash_flow, investment):
    npv = cash_flow - investment
    print(f'NPV = {print_num(npv)}')
    return npv

def apv(npv, tax_shield):
    apv = npv + tax_shield
    print(f'APV = {print_num(apv)}')
    return apv

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
    #value = debt + equity  # Total value of assets

    tax_rate = None  # Corporate tax rate

    # Is this needed, or is value = investment?
    investment = None  # Value of investment for project
    cash_flow = None

    # r_e = calculate_equity_return(r_a, r_d, tax_rate, debt, equity)
    # r_a = calculate_occ(r_d, r_e, debt, equity, tax_rate, value)

    # b_e = calculate_beta_equity(debt, equity, tax_rate, b_a, b_d)
    # b_a = calculate_beta_assets(b_d, b_e, debt, equity, value, tax_rate)

    unlevered_c_flow = unlevered_cash_flow(cash_flow=cash_flow, occ=r_a, tax_rate=tax_rate, tax_done=False)
    apv = apv(
            npv(cash_flow=unlevered_c_flow, investment=investment),
            tax_shield(debt=debt, interest_rate=r_d, tax_rate=tax_rate)
            )



