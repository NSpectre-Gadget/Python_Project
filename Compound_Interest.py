# Invest w/ initial and continuous compounded interest
def compound_int():
    deposit = float(input("Enter the amount of money deposited for this investment: $"))
    rate = float(input("Enter the interest rate percentage of the investment: "))
    n = float(input("Number of times the investment is compounded annually: "))
    t = float(input("Enter the number of years the investment is held: "))
    PMT = float(input("Enter the amount of the monthly contributions made: $"))

    int = rate / 100

    # A = ((deposit * (1 + (int / 12))) ** (n * t)) + (
    #    ((PMT * ((1 + (int / n)) ** (n * t))) - 1) / (int / n)
    # )

    P = (PMT * (((1 + int) * (n - 1)) / int)) * (1 + int)

    # print(f"The future value of your investment is: ${A: .02f}")
    print(f"The future value of your investment is: ${P: .02f}")


compound_int()

# Compounded continuously
# A = P * e ^ rt
