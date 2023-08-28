# Budget Tracker CLI

The Budget Tracker CLI is a Python-based command-line application designed to help you manage your finances and track your expenses easily. This tool utilizes the SQLAlchemy library for database management and provides various features to handle your financial data effectively.

## Installation

To use the Budget Tracker CLI, follow these steps:

1. Fork and clone the repository to your local computer:

   ```console
   git clone git@github.com:<your_username>/python-p3-cli-project-budget-tracker.git
   ```

2. Navigate to the project directory:

   ```console
   cd <app_directory>
   ```

3. Install the required dependencies using pipenv:

   ```console
   pipenv install
   ```

## Usage

To run the app, you need to write the following commands:

1. Activate the virtual environment:

   ```console
   pipenv shell
   ```

2. Run the CLI script:

   ```console
   python lib/cli.py
   ```

The CLI will display a menu with various options for managing your financial data. You can select options to add expenses, create categories, sort expenses, calculate sums, and more. The menu-driven interface makes it easy to interact with the application and perform different financial tasks.

## External Libraries

The Budget Tracker CLI utilizes the following Python libraries:

- **SQLAlchemy**: A powerful and flexible Object-Relational Mapping (ORM) library for working with databases.
- **simple-term-menu**: A library for creating simple terminal menus to enhance user interaction.
- **rich**: A library for adding rich text and formatting to terminal output.

## Files and Modules

The Budget Tracker CLI consists of several Python files, each serving a specific purpose:

- **`models.py`**: Contains SQLAlchemy classes for the Expense and Category tables and initializes them when run.
- **`functions.py`**: Defines functions used throughout the application for database operations and data processing.
- **`seed_categories.py`**: Populates the Category table with sample category data for testing purposes.
- **`seed_expenses.py`**: Populates the Expense table with sample expense data for testing purposes.
- **`cli.py`**: The main entry point of the application that provides the command-line interface and menu options.
- **`budget_tracker.db`**: The database file where all the data is saved.

## Features

- Add, view, and categorize expenses.
- Create and manage expense categories.
- Sort and display expenses in ascending or descending order.
- Calculate the sum of expenses.
- Filter and display expenses by month.
- Get the sum of monthly expenses.
- Retrieve expenses by category and month.
- Update expense and category records.
- Delete expense and category records.
- Seed sample data for testing purposes.

## Function Descriptions

Here's a detailed overview of the key functions in `functions.py` file provided in the lib directory:

- **`create_expense(amount, description, category_id, date)`**
  Allows you to create a new expense record. Provide the amount, description, category ID, and date for the expense. The function validates the category ID against existing categories and adds the expense to the database.

- **`create_category(name)`**
  Enables the creation of new expense categories. Simply provide the name of the category, and it will be added to the database.

- **`delete_all_records(model_cls)`**
  Deletes all records from the specified table. Useful for cleaning up data during testing or resetting the application.

- **`delete_record(model_cls, id)`**
  Deletes a specific record of the given model class (Expense or Category) by ID.

- **`display_data(model_cls, all_data)`**
  Displays the data from the specified model class (Expense or Category) in a tabular format. Provides a visual representation of the stored data.

- **`sum_expenses(month = None, year = None)`**
  Calculates and displays the sum of expenses. If provided with a specific month and year, it calculates the sum for that period.

- **`expense_by_month(month, year)`**
  Retrieves and returns a list of expenses for a specific month and year.

- **`get_expenses_by_category_month(category_id, month = None, year = None)`**
  Retrieves expenses by category and optionally filters them by month and year.

- **`update_record(model_cls, id, new_data)`**
  Updates the data of a specific record in the given model class (Expense or Category) by ID. Pass a dictionary new_data containing the updated values.
- **`delete_all(delete_expenses=True, delete_categories=True)`**
  Deletes all records from the database. This function allows you to remove all expense and category records or choose to delete only one type of records. The user can choose to either delete all the tabels records or one of the tables records.

## Contributing

Contributions to the Budget Tracker CLI are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the [MIT License](https://github.com/mohamedmhussein/python-p3-cli-project-budget-tracker/blob/main/LICENSE).
