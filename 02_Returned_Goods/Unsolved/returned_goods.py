"""Returned Goods."""


# @TODO: Define a new function called process_claims
# Inside of the function:
# Create a variable called `total_claims`, that is the sum of all claims
# Calculate a total payout, which is 30% of total_claims:
# Return only the total_payout amount
from concurrent.futures import process


def process_claims (claims):
    total_claims = sum(claims)
    total_payout = total_claims * .30
    return total_payout

# @TODO Paste the list of weekly claims:
weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]

# What's the total insurance payout?
# Use the print() statement to print the returned value from the function.
# @TODO: Call the function using `weekly_claims` as the function argument
total_insurance_payout = process_claims(weekly_claims) 

print(f"The total payout is ${total_insurance_payout: .2f}")