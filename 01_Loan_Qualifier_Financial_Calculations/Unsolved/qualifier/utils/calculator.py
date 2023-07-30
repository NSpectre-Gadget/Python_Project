"This script contains a variety of financial caclulator functions needed to determine loan qualifications"
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    "Calculates user's monthly debt-to-income ratio"
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio
    "Calcualtes user's loan-value-ration"
def calculate_loan_to_value_ratio(loan_amount, home_value):
    # @TODO Implement loan_to_value_ratio calculation
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio

    