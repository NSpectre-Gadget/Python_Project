from os import remove


stock_tickers = ["AMZN", "CSCO", "FB","GOOG","INTC","MSFT","SQ","TWTR", "WRK"]
print(stock_tickers)

stock_tickers [8] = "WORK"
print[stock_tickers]

stock_tickers.append = ["ZM"]
print(stock_tickers)

print_tickers = [stock_tickers]
print(stock_tickers)

stock_tickers = [0]
print(stock_tickers)

stock_tickers = [-1]
print(stock_tickers)

stock_tickers.insert(-,"aapl")
print(stock_tickers)

stock_tickers.insert("3,""Dell")
print(stock_tickers)

stock_tickers.remove("INTC")
print(stock_tickers)
stock_tickers.pop(7)
print(stock_tickers)

stock_tickers_slice = stock_tickers[2:6]
print(stock_tickers_slice)


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

    * `current_price`

    * `increase`

    * `percent_increase`

2. Calculate `increase`.

3. Calculate `percent_increase`.

4. Print `original_price`, `current_price`, and `percent_increase` to the screen.

5. Use a [format specifier](https://www.python.org/dev/peps/pep-0498/#format-specifiers) with the f-string to print the percent increase with two decimal places (e.g., `27.88%`).

## Hint

For additional information on f-strings, see this [guide to Python 3's f-strings](https://realpython.com/python-f-strings/).

