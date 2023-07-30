import questionary

answer = questionary.text("Is cereal soup?").ask()
message = "Try again"

if answer == "yes":
    message = "Yes, good job, cereal is soup"

print(message)
