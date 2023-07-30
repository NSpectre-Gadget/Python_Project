original_price = 198.87
current_price = 254.32
increase = current_price - original_price
percent_increase = increase/ original_price * 100

print(f"The original price is:{original_price}.")
print(f"The current price is: {current_price}.")
print(f"The percent of increase is $:{increase}.")
print(f"The percent_increase is : {percent_increase: .2f}%.")




# Hello, Variable World

In this activity, you'll create a Python program to do percent increase calculations.

## Background

For the past week, you've been watching your coworker Harold use a calculator to manually track stock price fluctuations. Harold spends three hours every day tracking his stocks this way, logging the stock's original price (from the day before), the current price, and the percentage of increase or decrease. You know that automating this calculation would streamline Harold's daily process, leaving more time for making investment decisions. Your new Python skills can help you achieve this for him.

In this activity, create a Python program to automate Harold's process by programmatically implementing the percent increase calculation.

Start small by identifying the percent increase in price for Apple stock. Yesterday at 9:00 a.m., Apple's stock price was \$198.87. At close of market today, the stock price was \$254.32. Calculate the percent increase using the following formulas:

* Increase = Current Price - Original Price

* Percent Increase = Increase / Original x 100

## Instructions

Using the [starter file](Unsolved/percent_increase.py), complete the following steps:

1. Create variables for the following:

    * `original_price`
original_price = 198.87
print(f"The original price is ${original_price}")
    * `current_price`
current_price = $254.32
print(f"The current price is ${current_price}")
    * `increase`

    * `percent_increase`

2. Calculate `increase`.
increase = current_price - original_price
print(f"The amount of the increase is ${increase}")
3. Calculate `percent_increase`.
percent_increase = increase / original_price * 100
print(f"The percent increase in the stock is:{percent_increase: .2f}")
4. Print `original_price`, `current_price`, and `percent_increase` to the screen.

5. Use a [format specifier](https://www.python.org/dev/peps/pep-0498/#format-specifiers) with the f-string to print the percent increase with two decimal places (e.g., `27.88%`).

## Hint

For additional information on f-strings, see this [guide to Python 3's f-strings](https://realpython.com/python-f-strings/).
