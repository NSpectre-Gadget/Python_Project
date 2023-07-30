"Helper function to load CSV data."
import csv

def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def calculate_loan_to_value_ratio(loan_amount, home_value):
    # @TODO Implement loan_to_value_ratio calculation
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio

def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio