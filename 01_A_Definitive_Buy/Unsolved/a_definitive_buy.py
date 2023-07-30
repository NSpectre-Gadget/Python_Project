"""A Definitive Buy."""


# @TODO: Create a function that prints two messages.
# The first message should state the cost of the transaction.
# THe second message should state that the payment has been processed.
def process_payment():
    print("The total cost of this transaction will be 78 cents.")
    print("Ka-ching! Payment has been processed.")

# Call the function to run the code in the function.
process_payment()
def average_number(numbers):
    average = sum(numbers) / len(numbers)
    return average

first_average = average_number([1,2,3])
second_average = average_number([4,5,6])
print(first_average, second_average)