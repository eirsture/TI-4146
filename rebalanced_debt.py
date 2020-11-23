from general import format_float, capm, unlevered_cash_flow, npv, tax_shield, apv


def calculate_occ(debt_return, equity_return, debt, equity, value, tax=None, periodically=False):
    "Step 1: unlever, calculate occ from existing operations"
    if periodically:
        print("Debt is periodically rebalanced")
        print("r_{a}=\\frac{r_{E}+r_{D} \cdot y}{1+y}")
        print("\\text{Where y}=\\frac{D}{E} \cdot \left(1-\\frac{T_{C} \cdot r_{D}}{1+r_{D}}\\right)")
        print("y=\\frac{%s}{%s} \cdot \left(1-\\frac{%s \cdot %s}{1+%s}\\right)" % (debt, equity, tax, debt_return, debt_return))
        y = format_float(debt/equity * (1 - (tax*debt_return/(1+debt_return))))
        print(f'y = {y}')
        print("r_{a}=\\frac{%s+%s \cdot %s}{1+%s}" % (equity_return, debt_return, y, y))
        occ = ((equity_return+debt_return*y)/(1+y))
    else:
        print("Debt is continuously rebalanced")
        print("r_{a}= r_{e} \cdot \\frac{E}{V} + r_{d} \cdot \\frac{D}{V}")
        print("r_{a}= %s \cdot \\frac{%s}{%s} + %s \cdot \\frac{%s}{%s}" % (equity_return, equity, value, debt_return, debt, value))
        occ = debt_return*debt/value + equity_return*equity/value
    occ = format_float(occ)
    print('r_{a} = %s' % (occ))
    return occ


def calculate_equity_return(occ, debt_return, debt, equity):
    "Step 2: Calcluate project's cost of equity, using project's debt and equity"
    r_e = format_float(occ + (occ-debt_return)*(debt/equity))
    print(f'r_e = {r_e}')
    return r_e


def calculate_wacc(debt_return, equity_return, debt, equity, value, tax):
    "NOTE: THIS METHOD REQUIRES CONTINUOUS REBALANCING"
    "Step 3: relever, calculate after-tax WACC using project's cost and weights"
    wacc = format_float(equity_return*equity/value + debt_return*(1-tax)*debt/value)
    print(f'wacc = {wacc}')
    return wacc


if __name__ == '__main__':
    b_a = None  # Beta of assets
    b_e = None  # Beta of equity
    b_d = None  # Beta of debt

    r_a = None  # Opportunity cost of capital = Return of assets
    r_d = None  # Return of debt
    r_e = None  # Return of equity
    r_f = None  # Risk-free interest rate
    r_m = None  # Return of market

    debt_type = None  # debt_type can be: ("periodically", "continuously")
    debt = None  # Value of debt
    equity = None  # Value of equity
    value = debt + equity  # Total value of assets

    tax_rate = None  # Corporate tax rate

    investment = None  # Value of investment for project
    cash_flow = None  # Annual cash flow from project

    # Step 1 - Has to be calculated either way, tax is only needed if periodically = True
    # r_a = calculate_occ(debt_return=r_d, equity_return=r_e, debt=debt, equity=equity, value=value, tax=tax_rate, periodically=False)

    # Method 1 - Step 2 & 3 following the WACC 'unlever' and 'relever' method - Requires continuous rebalancing
    # r_e = calculate_equity_return(occ, debt_return, debt, equity)
    # wacc = calculate_wacc(debt_return, equity_return, debt, equity, value, tax)

    # Method 2 - Step 2+++ following the APV - Adjusted Present Value method
    # unlevered_c_flow = unlevered_cash_flow(cash_flow=cash_flow, occ=r_a, tax_rate=tax_rate, tax_done=True)
    # npv = npv(cash_flow=unlevered_c_flow, investment=investment)
    # tax_shield = tax_shield(debt=debt, occ=r_a, interest_rate=r_d, tax_rate=tax_rate, debt_type=debt_type)
    # apv = apv(npv, tax_shield)

