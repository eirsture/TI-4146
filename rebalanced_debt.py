def print_num(num):
    return format(num, ".4f")

def calculate_occ(debt_return, equity_return, debt, equity, value, periodically=False):
    "Step 1: unlever, calculate occ from existing operations"
    if periodically:
        return None
    else:
        occ = debt_return*debt/value + equity_return*equity/value
    print(f'occ = {print_num(occ)}')
    return occ

def calculate_equity_return(occ, debt_return, debt, equity):
    "Step 2: Calcluate project's cost of equity, using project's debt and equity"
    r_e = occ + (occ-debt_return)*(debt/equity)
    print(f'r_e = {print_num(r_e)}')
    return r_e

def calculate_wacc(debt_return, equity_return, debt, equity, value, tax):
    "NOTE: THIS METHOD REQUIRES CONTINUOUS REBALANCING"
    "Step 3: relever, calculate after-tax WACC using project's cost and weights"
    wacc = equity_return*equity/value + debt_return*(1-tax)*debt/value
    print(f'wacc = {print_num(wacc)}')
    return wacc

def yearly_interest_charge(loan, interest_rate):
    charge = interest_rate*loan
    print(f'Yearly interest charge = Loan * Interest Rate = {print_num(charge)}')
    return charge

def tax_advantage(tax, interest_charge):
    t_a = tax*interest_charge
    print(f'Yearly tax advantage = Tax rate * Yearly Interest Charge = {print_num(t_a)}')
    return t_a

def tax_shield(debt, interest_rate, occ, tax_rate, rebalanced_periodically=False):
    interest_charge = yearly_interest_charge(debt, interest_rate)
    tax_advg = tax_advantage(tax_rate, interest_charge)
    tax_shield = tax_advg/occ
    if rebalanced_periodically:
        print(f'Debt is rebalanced periodically')
        tax_shield = tax_shield*(1+occ)/(1+interest_rate)
    else:
        print(f'Debt is rebalanced continuously')

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
    r_m = None  # Return of market

    debt = None  # Value of debt
    equity = None  # Value of equity
    value = debt + equity  # Total value of assets

    tax_rate = None  # Corporate tax rate

    investment = None  # Value of investment for project
    cash_flow = None  # Annual cash flow from project

    # Step 1 - Has to be calculated either way
    # r_a = calculate_occ(debt_return=r_d, equity_return=r_e, debt=debt, equity=equity, value=value)

    # Method 1 - Step 2 & 3 following the WACC 'unlever' and 'relever' method - Requires continuous rebalancing
    # r_e = calculate_equity_return(occ, debt_return, debt, equity)
    # wacc = calculate_wacc(debt_return, equity_return, debt, equity, value, tax)

    # Method 2 - Step 2+++ following the APV - Adjusted Present Value method
    # unlevered_c_flow = unlevered_cash_flow(cash_flow=cash_flow, occ=r_a, tax_rate=tax_rate, tax_done=True)
    # npv = npv(cash_flow=unlevered_c_flow, investment=investment)
    # tax_shield = tax_shield(debt=debt, occ=r_a, interest_rate=r_d, tax_rate=tax_rate, rebalanced_periodically=False)
    # apv = apv(npv, tax_shield)

