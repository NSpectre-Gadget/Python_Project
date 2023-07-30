"""Racking up the profit."""

# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
total_dividend_income = 0.0

# @TODO: Create a for loop to calculated and add up all the dividend income
for dividend in dividend_yields:
    dividend_income = stock_price * dividend
    total_dividend_income = dividend_income + total_dividend_income

    print(f"The dividend income is ${dividend_income: 2f}")
# @TODO: Once it's all done, print the dividend income for the entire portfolio
print("The profit income is: ", total_dividend_income)
