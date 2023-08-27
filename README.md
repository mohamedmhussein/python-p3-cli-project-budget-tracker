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

## Contributing

Contributions to the Budget Tracker CLI are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the [MIT License](https://github.com/mohamedmhussein/python-p3-cli-project-budget-tracker/blob/main/LICENSE).

### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

```

```
