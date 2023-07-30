import fire

def run_crud(message="Running CRUD"):
	print(message)

if __name__ == '__main__':
	fire.Fire(run_crud)

import questionary
#table_name = questionary.text("What is the name of the database table that you would like to create?").ask()
#print(table_name)

#def confirm_tables(engine):
#    tables = engine.table_names()
#    print(f"The tables in the database are: {tables}")

#def run():

    # Prompt the user for the table name
#    table_name = questionary.text("What name would you like to use for your table?").ask()

    # Create the table in the database
#    create_table(engine, table_name, stocks_dataframe)

    # Confirm the table in the database
#    confirm_tables(engine) 

#if __name__ == "__main__":
#    fire.Fire(run)

def run():
    """The main function for running the application."""

    # Dynamically load data into a DataFrame
    csv_name = questionary.text("What is the name of your CSV file?").ask()
    csvpath = Path(csv_name)
    stocks_dataframe = pd.read_csv(csvpath)

    # Prompt the user for the table name
    table_name = questionary.text("What name would you like to use for your table?").ask()

    # Create the table in the database
    create_table(engine, table_name, stocks_dataframe)

    # Confirm the table in the database
    confirm_tables(engine)

if __name__ == "__main__":
    fire.Fire(run)

