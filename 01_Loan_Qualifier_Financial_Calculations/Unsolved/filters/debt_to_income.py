#filters the bank files for approval to debt-to-income list

def filter_debt_to_income(monthly_debt_ratio, bank_list):
    debt_to_income_approval_list = []

    for bank in bank_list:
        if (monthly_debt_ratio) <= float(bank[3]):
            debt_to_income_approval_list.append(bank)
    return monthly_debt_ratio_list