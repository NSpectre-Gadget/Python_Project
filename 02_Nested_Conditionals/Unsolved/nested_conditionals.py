"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
ad_price = 10
company_type = "Startup"

# @TODO: Convert the following decision logic into valid Python code.
if ad_price < 20:
     if company_type == "Startup":
         print("the expected profit is 500")
     elif(company_type) == "Existing":
         print("The expected profit is, 100")
     else:
         print("The company type is not_specified.")
else:
     print("The ad_price is too expensive")
