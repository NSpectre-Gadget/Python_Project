from fileinput import close


#words = ["cool!", "awesome", "why am I shouting?"]

#for word in words:
 #   print("Original Word: ", word)
  #  print("Uppercase Word: ", word.upper())
   # print("Titlecase Word: ", word.title())
#print("I'm outside of the loop, so I only print once after all the words have been selected!")

#principle = 103208.56
#interest_rates = [.103, .067, .099, .10]
#total_interest = 0.0
#for rate in interest_rates:
 #   interest = rate * principle
  #  total_interest = total_interest + interest
   # print("Your interest will be: ", interest)

#print("The total interest is: ", total_interest)

#table_data = [
#    ["Ticker", "Open", "Close"],
 #   ["AAPL", 363.25, 363.4],
  #  ["AMZN", 2756.0, 2757.99],
 #   ["GOOG", 1409.1, 1408.2]
#]
#goog_data = table_data[3]
#print(goog_data)

#amazon_data = table_data[2]
#amazon_opening_price = amazon_data[1]
#print(amazon_opening_price)

#amazon_opening_price = table_data[2][1]
#print(amazon_opening_price)

#for row in table_data:
 #   ticker = row[0]
  #  close = row[2]
   # print(ticker, close)
table_data = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]
for item in table_data:
    ticker = item["Ticker"]
    print(ticker)

for item in table_data:
    print(item)